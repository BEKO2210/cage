"""Blind judges from three companies rank narrations of the same repo.

python3 judge.py <tag> <film> [<film> ...] --arms out/gold/gold out/cage/qwen3_8b ... [--judges codex,gemini,grok]
Each judge sees the repo digest and the scripts as X/Y/Z, never which arm wrote which. The order is a Latin square:
over every 3 judges each arm sits once in each position, and odd films reverse it, so position bias cancels out. Appends to results/<tag>.jsonl one row per (film, judge): ranking by arm + factual errors by arm."""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILMS = HERE / "data"


def codex(p):
    with tempfile.NamedTemporaryFile("r", suffix=".txt") as out:
        subprocess.run(["codex", "exec", "--skip-git-repo-check", "--ephemeral", "-m", "gpt-5.6-sol", "-s", "read-only", "-o", out.name, "-"],
                       input=p, text=True, capture_output=True, timeout=900)
        return Path(out.name).read_text()


# The digest is untrusted README text: every judge runs read-only in its own empty throwaway folder.
def gemini(p):
    with tempfile.TemporaryDirectory() as empty:
        return subprocess.run(["agy", "-p", p], text=True, capture_output=True, timeout=900, cwd=empty).stdout


def grok(p):
    with tempfile.TemporaryDirectory() as empty:
        return subprocess.run(["cursor-agent", "-p", "--trust", "--mode", "ask", "--model", "cursor-grok-4.5-high", "--output-format", "text", p],
                              text=True, capture_output=True, timeout=900, cwd=empty).stdout


JUDGES = {"codex": codex, "gemini": gemini, "grok": grok}
LABELS = "XYZWV"


def prompt(digest, scripts):
    body = "\n\n".join(f"SCRIPT {LABELS[i]}:\n" + "\n".join(lines) for i, lines in enumerate(scripts))
    return f"""Do not run any tool or command; only read this message and answer. You judge narration scripts for a 65-80 second Instagram reel about one GitHub repository. The narrator reads
each script aloud over the repo page. The REPO DIGEST below is the only truth about the repo.

Judge like a demanding social-media editor who also checks facts:
1. Accuracy: every claim and number must be supported by the digest. An invented or distorted claim is a serious flaw.
2. Hook: does the first line make a scroller stop?
3. Clarity: would a developer who never heard of the repo understand what it is and why it matters?
4. Flow and voice: natural spoken English, no filler, no repetition, a clear arc to a call to share or save.
5. Length: 150-190 words fits the reel; much shorter or longer is a flaw.

REPO DIGEST:
{digest}

{body}

Answer with JSON only, no code fence:
{{"ranking": ["<best label>", ..., "<worst label>"], "errors": {{"<label>": ["<each unsupported or wrong claim>"]}}, "why": "<two sentences>"}}"""


def parse(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    try:
        return json.loads(m.group(0)) if m else None
    except json.JSONDecodeError:
        return None


if __name__ == "__main__":
    tag = sys.argv[1]
    films = sys.argv[2:sys.argv.index("--arms")]
    rest = sys.argv[sys.argv.index("--arms") + 1:]
    arms = [a for a in rest[:rest.index("--judges")] if a] if "--judges" in rest else rest
    judges = rest[rest.index("--judges") + 1].split(",") if "--judges" in rest else list(JUDGES)
    out = HERE / "results" / f"{tag}.jsonl"
    out.parent.mkdir(exist_ok=True)
    done = {(r["film"], r["judge"]) for r in map(json.loads, out.read_text().splitlines())} if out.exists() else set()
    for fi, film in enumerate(films):
        digest = (FILMS / film / "repo/digest.md").read_text()
        scripts = {a: json.loads((HERE / a / f"{film}.json").read_text())["lines"] for a in arms}
        for ji, judge in enumerate(judges):
            if (film, judge) in done:
                continue
            base = arms[::-1] if fi % 2 else list(arms)
            k = (fi + ji) % len(arms)
            order = base[k:] + base[:k]
            lab = {LABELS[i]: a for i, a in enumerate(order)}
            label = lambda l: lab.get(re.sub(r"(?i)^\s*script\s*", "", str(l)).strip()[:1].upper())
            row = None
            for _ in range(2):
                res = parse(JUDGES[judge](prompt(digest, [scripts[a] for a in order])))
                ranking = [label(l) for l in (res or {}).get("ranking", [])]
                if sorted(filter(None, ranking)) == sorted(arms) and len(ranking) == len(arms):   # a full, clean ranking only
                    row = {"film": film, "judge": judge, "order": order, "ranking": ranking,
                           "errors": {label(k) or k: v for k, v in (res.get("errors") or {}).items()}, "why": res.get("why", "")}
                    break
            if not row:
                print(f"{film} {judge}: no clean verdict - not saved, rerun to retry")
                continue
            with out.open("a") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"{film} {judge}: {' > '.join(row['ranking'])}")
