"""cage: a small local model writes reel narration inside a cage (fixed arc, per-slot jobs, validators, repair loop).

python3 cage.py <film-dir> <arm> [--model qwen3:8b]
  arm = gold   the published narration (story.json)
        free   the local model with the same guide the big models get, no cage
        cage   the local model, one slot at a time, every slot validated and repaired
Writes out/<arm>/<model>/<film>.json = {"lines": [...], "log": [...]}"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GUIDE = Path.home() / "motion-studio/films/_reel/story-guide.md"


def llm(prompt, model, temperature=0.7, fmt=None):
    req = {"model": model, "prompt": prompt, "stream": False, "think": False, "keep_alive": "10m",
           "options": {"temperature": temperature, "num_ctx": min(16384, max(8192, len(prompt) // 3 + 1500))}}
    if fmt:
        req["format"] = fmt
    r = subprocess.run(["ssh", "pop", "mkdir -p ~/reel && flock ~/reel/gpu.lock curl -s http://localhost:11434/api/generate -d @-"],
                       input=json.dumps(req), capture_output=True, text=True, timeout=900, check=True)
    return json.loads(r.stdout)["response"].strip()


# ---------- facts: the only numbers a line may say ----------

NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")


def norm(n):
    return n.replace(",", "").rstrip(".")


def allowed_numbers(source, facts):
    ok = {norm(n) for n in NUM.findall(source)}
    stars = facts.get("stars") or 0
    for step in (1000, 10000, 100000):                                     # "past 100,000 stars" for 110,358
        if stars >= step:
            r = stars // step * step
            ok.add(str(r))
    return ok


def numbers_in(text):
    return [norm(n) for n in NUM.findall(text)]


def fact_sheet(digest, facts):
    sec = re.search(r"## Sentences with numbers \(verbatim\)\n(.*?)\n## ", digest, re.S)
    lines = [l[2:].strip()[:400] for l in (sec.group(1) if sec else "").splitlines() if l.startswith("- ")]
    head = [f"{facts['repo']}: {facts.get('description', '')}", f"{facts.get('stars', 0):,} GitHub stars, main language {facts.get('language')}"]
    return [f"F{i}: {t}" for i, t in enumerate(head + lines)]


def readme(digest, limit=14000):
    sec = re.search(r"## README by section\n(.*?)\n## Sentences", digest, re.S)
    return (sec.group(1) if sec else digest)[:limit]


# ---------- the cage ----------

NAME = lambda f: f["repo"].split("/")[1]
SLOTS = [  # id, job, min words, max words, needs a sourced number
    ("hook", "Open with the single most surprising sourced number about {name}. A viewer must stop scrolling. Name what the number measures.", 10, 18, True),
    ("problem", "Name the problem {name} solves: the pain a developer feels today, from the README.", 12, 22, False),
    ("what", "Say in plain words what {name} is and who it is for. No number needed.", 12, 20, False),
    ("how", "Explain how it works: the one mechanism that makes it different. Concrete, no buzzwords.", 14, 24, False),
    ("how2", "Show it in action: one concrete example of input and result from the README.", 14, 24, False),
    ("proof", "Give proof: a benchmark or measured result with its number, and against what.", 14, 24, True),
    ("proof2", "Give a second, different proof or a striking detail with its number (not one already used).", 12, 22, True),
    ("detail", "One more concrete thing it does that the lines so far did not mention, from the README.", 12, 22, False),
    ("trust", "Build trust: stars, licence, who uses it or who made it. Use the real star count rounded down if you round.", 10, 18, False),
    ("start", "How to start: name the install command or the first step from the README, in spoken words.", 10, 18, False),
    ("share", "Ask the viewer to share or save it. Start with 'Send this to someone who' or 'Save this for'. Never ask to follow.", 8, 14, False),
    ("end", "Close with a short punchline that names {name}.", 4, 10, False),
]
FILLER = re.compile(r"\b(revolutionary|game[- ]?chang\w*|unleash\w*|seamless\w*|supercharg\w*|cutting[- ]edge|next[- ]level|"
                    r"powerful|ultimate|incredible|amazing|mind[- ]blowing|insane|journey|elevate|delve|harness)\b", re.I)


TENS = r"(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
SPELLED = re.compile(rf"\b({TENS}([- ]\w+)?|(zero|one|two|three|four|five|six|seven|eight|nine) point \w+|(eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)|"
                     r"\w+ (hundred|thousand|million|billion)|(two|three|four|five|six|seven|eight|nine|ten)|"
                     r"(hundreds|thousands|millions|billions|dozens|half|twice|double|triple|tenfold))\b", re.I)


def check_line(say, slot, ok_nums, used_nums):
    _, _, lo, hi, needs_num = slot
    errs = []
    words = len(say.split())
    if not lo <= words <= hi:
        errs.append(f"has {words} words, must have {lo}-{hi}")
    nums = numbers_in(say)
    bad = [n for n in nums if n not in ok_nums]
    if bad:
        errs.append(f"numbers not in the facts: {', '.join(bad)} (copy numbers verbatim from the facts)")
    if needs_num and not nums:
        errs.append("must contain a number from the facts")
    again = [n for n in nums if n in used_nums and len(n) > 1]
    if again:
        errs.append(f"repeats a number already said: {', '.join(again)}")
    if FILLER.search(say):
        errs.append(f"marketing filler word: {FILLER.search(say).group(0)}")  # type: ignore[union-attr]
    if re.search(r"[^\x00-\x7F×→·–—’‘“”]", say):
        errs.append("English only, no foreign characters")
    if slot[0] == "share" and not re.match(r"(Send this to someone|Save this for)", say):
        errs.append("must start with 'Send this to someone who' or 'Save this for'")
    if re.search(r"\b(ever|best|biggest|fastest|most|largest|top|leading|number one|only one|world'?s)\b", say, re.I):
        errs.append("no superlatives unless the facts say exactly that")
    if "`" in say or re.search(r"\d+(\.\d+)?[kKmM]\b", say):
        errs.append("spoken words only: no code marks, no 15k-style shortcuts (say the full number from the facts)")
    if SPELLED.search(say):                                                # "thirty-three point two" slips past the number check
        errs.append("write every number in digits exactly as in the facts, never in words")
    if re.search(r"\bfollow\b", say, re.I):
        errs.append("never ask to follow")
    return errs


def ask_line(slot, facts, sheet, rd, story, used, model, errs=None, prev=None):
    sid, job, lo, hi, _ = slot
    so_far = "\n".join(f"{i}: {s}" for i, s in story) or "(nothing yet)"
    p = f"""You write one spoken line of a 70-second Instagram reel about the GitHub repo {facts['repo']}.
Spoken, short sentences, plain English, no marketing words. Every number must be copied exactly from FACTS.

FACTS:
{chr(10).join(sheet)}

README (for meaning, not for numbers):
{rd}

LINES SO FAR:
{so_far}

YOUR LINE "{sid}": {job.format(name=NAME(facts))}
Write it as TWO short spoken sentences, {lo}-{hi} words together. Do not repeat anything the lines so far already said.
Numbers already said (never use them again): {', '.join(sorted(used)) or 'none'}
Answer as JSON: {{"say": "..."}}"""
    if errs:
        p += f"\n\nYour last try was: {prev}\nIt broke these rules: {'; '.join(errs)}. Write it again and fix every one."
    try:
        return json.loads(llm(p, model, fmt="json")).get("say", "").strip()
    except (json.JSONDecodeError, AttributeError):
        return ""


def verify(say, facts, sheet, rd, model):
    """The second bar of the cage: a cold reader (temperature 0) lists every claim the sources do not state."""
    p = f"""You are a strict fact-checker for a reel about {facts['repo']}. Use ONLY the sources below.
FACTS:
{chr(10).join(sheet)}
README:
{rd}

LINE: {say}

Check only concrete claims about the repo: what it does, its features, numbers, who made, uses or tested it, comparisons.
Such a claim is supported only if the sources state it (same meaning, same numbers, same actor: "X studied it" is not
"X uses it"). Superlatives about the repo ("biggest", "fastest", "game-changing") are unsupported unless stated.
Do NOT flag framing that makes no claim about the repo: the problem developers face, an invitation to share or save,
a punchline, a paraphrase in simpler words.
Answer as JSON: {{"unsupported": ["<claim> - <why>", ...]}} (an empty list if every claim is supported)"""
    try:
        bad = json.loads(llm(p, model, temperature=0, fmt="json"))["unsupported"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return ["fact-check gave no answer"]                              # fail closed: an unchecked line never gets in
    if not isinstance(bad, list):
        return ["fact-check gave no answer"]
    return [f"not in the sources: {b}" for b in bad if isinstance(b, str) and b.strip()]


def pick(cands, slot, facts, story, model):
    if len(cands) == 1:
        return cands[0]
    menu = "\n".join(f"{i}: {c}" for i, c in enumerate(cands))
    p = f"""Reel about {facts['repo']}. Lines so far: {' '.join(s for _, s in story)}
Which candidate for the line "{slot[0]}" is the most concrete, surprising and easiest to understand when spoken?
{menu}
Answer as JSON: {{"best": <index>}}"""
    try:
        return cands[int(json.loads(llm(p, model, temperature=0, fmt="json"))["best"])]
    except (KeyError, ValueError, IndexError, json.JSONDecodeError):
        return cands[0]


def cage(F, model, tries=3, keep=3):
    digest, facts = (F / "repo/digest.md").read_text(), json.loads((F / "repo/facts.json").read_text())
    sheet, rd = fact_sheet(digest, facts), readme(digest)
    ok_nums = allowed_numbers("\n".join(sheet) + rd, facts)
    story, used, log = [], set(), []
    for slot in SLOTS:
        cands, near = [], []
        for _ in range(keep):
            say, errs = "", None
            for t in range(tries):
                say = ask_line(slot, facts, sheet, rd, story, used, model, errs, say)
                errs = check_line(say, slot, ok_nums, used)
                length_only = bool(say) and all(e.startswith("has ") for e in errs)
                if length_only:
                    errs += verify(say, facts, sheet, rd, model)
                    length_only = all(e.startswith("has ") for e in errs)
                log.append({"slot": slot[0], "try": t, "say": say, "errs": errs})
                if not errs:
                    cands.append(say)
                    break
                if length_only:                                     # only the length is off: kept as a fallback
                    near.append(say)
        best = pick(cands or near, slot, facts, story, model) if cands or near else None
        if best is None:                                                    # the cage holds: a line with a wrong fact never gets in
            log.append({"slot": slot[0], "dropped": True})
            continue
        story.append((slot[0], best))
        used |= set(numbers_in(best))
    return [s for _, s in story], log


def free(F, model):
    digest, facts = (F / "repo/digest.md").read_text(), json.loads((F / "repo/facts.json").read_text())
    p = f"""{GUIDE.read_text()}

The digest of THIS repo ({facts['url']}) - the only source of facts:
{digest}

Write only the narration: 11-13 lines, 150-190 words in all. Answer as JSON: {{"lines": [{{"id": "...", "say": "..."}}]}}"""
    out = json.loads(llm(p, model, fmt="json"))
    return [l["say"].replace(" / ", " ").replace("/", " ") for l in out.get("lines", [])], []


def gold(F):
    return [l["say"].replace(" / ", " ").replace("/", " ") for l in json.loads((F / "story.json").read_text())["lines"]], []


if __name__ == "__main__":
    F, arm = Path(sys.argv[1]).resolve(), sys.argv[2]
    model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "qwen3:8b"
    lines, log = gold(F) if arm == "gold" else free(F, model) if arm == "free" else cage(F, model)
    if arm == "cage" and len(lines) < 10:
        sys.exit(f"cage {F.name}: only {len(lines)} lines passed - not saved as a result")
    out = HERE / "out" / arm / (model.replace(":", "_").replace("/", "_") if arm != "gold" else "gold") / f"{F.name}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"lines": lines, "words": sum(len(l.split()) for l in lines), "log": log}, indent=1, ensure_ascii=False))
    print(f"{arm} {F.name}: {len(lines)} lines, {sum(len(l.split()) for l in lines)} words -> {out}")
    print("\n".join(lines))
