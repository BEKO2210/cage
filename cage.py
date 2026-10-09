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
GUIDE = HERE / "data/story-guide.md"


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
    ("hook", "Open with the single most surprising sourced number about {name}. A viewer must stop scrolling. Name what the number measures.", 12, 20, True),
    ("problem", "Name the problem {name} solves: the pain a developer feels today, from the README.", 14, 24, False),
    ("what", "Say in plain words what {name} is and who it is for. No number needed.", 14, 22, False),
    ("how", "Explain how it works: the one mechanism that makes it different. Concrete, no buzzwords.", 16, 26, False),
    ("how2", "Show it in action: one concrete example of input and result from the README.", 16, 26, False),
    ("proof", "Give proof: a benchmark or measured result with its number, and against what.", 16, 26, True),
    ("proof2", "Give a second, different proof or a striking detail with its number (not one already used).", 14, 24, True),
    ("detail", "One more concrete thing it does that the lines so far did not mention, from the README.", 14, 24, False),
    ("detail2", "One more fact a developer would want to know before trying it (setup, limits, platforms, numbers), not said yet.", 12, 22, False),
    ("trust", "Build trust: licence, who made it, who uses or tested it. Name the star count only if it is 1,000 or more (rounded down if you round).", 12, 20, False),
    ("start", "How to start: name the install command or the first step from the README, in spoken words.", 12, 20, False),
    ("share", "Ask the viewer to share or save it. Start with 'Send this to someone who' or 'Save this for'. Never ask to follow.", 10, 16, False),
    ("end", "Close with a short punchline that names {name}.", 6, 12, False),
]
FILLER = re.compile(r"\b(revolutionary|game[- ]?chang\w*|unleash\w*|seamless\w*|supercharg\w*|cutting[- ]edge|next[- ]level|"
                    r"powerful|ultimate|incredible|amazing|mind[- ]blowing|insane|journey|elevate|delve|harness)\b", re.I)


TENS = r"(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)"
SPELLED = re.compile(rf"\b({TENS}([- ]\w+)?|(zero|one|two|three|four|five|six|seven|eight|nine) point \w+|(eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen)|"
                     r"\w+ (hundred|thousand|million|billion)|(two|three|four|five|six|seven|eight|nine|ten)|"
                     r"(hundreds|thousands|millions|billions|dozens|half|twice|double|triple|tenfold))\b", re.I)


def grams(t, n=4):
    w = re.findall(r"[a-z0-9']+", t.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def check_line(say, slot, ok_nums, used_nums, said=""):
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
    if "`" in say or "*" in say or re.search(r"\d+(\.\d+)?[kKmM]\b", say):
        errs.append("spoken words only: no code or bold marks, no 15k-style shortcuts (say the full number from the facts)")
    if "..." in say or "…" in say:
        errs.append("no '...' in the spoken line (that belongs in the receipt only)")
    again = grams(say) & grams(said)
    if again:
        errs.append(f"repeats words an earlier line already said: \"{sorted(again)[0]}\" - say something new")
    if SPELLED.search(say):                                                # "thirty-three point two" slips past the number check
        errs.append("write every number in digits exactly as in the facts, never in words")
    if re.search(r"\bfollow\b", say, re.I):
        errs.append("never ask to follow")
    return errs


# Cage v4: the voice goes into the first draft (rewriting afterwards invented claims, see RESULTS.md), and each of the
# candidates 2 and 3 of a slot get a pattern, so the picker chooses between real alternatives. Candidate 1 stays plain
# (a forced "you" voice on every line made lines drop and invented meaning on the dev set).
PATTERNS = {"hook": ["Contrast: the number against what it replaces (\"X instead of Y\").",
                     "A short question the viewer cannot ignore, then the number that answers it."],
            "problem": ["Describe the moment the pain hits a developer.", "Name the workaround people use today."],
            "end": ["A short punchline that names {name} and echoes the opening line's idea.", "Name {name} and its core idea in a few words."]}


def ask_line(slot, facts, sheet, rd, story, used, model, errs=None, prev=None, k=None):
    sid, job, lo, hi, _ = slot
    if k and sid in PATTERNS:                                                # cage v4
        job += " Pattern: " + PATTERNS[sid][(k - 1) % 2].format(name=NAME(facts))
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
Your line needs a receipt: copy, character for character, the sentence or table row from README or FACTS that states
every claim of your line (several pieces joined by " ... " if needed). Say nothing the receipt does not say.
Answer as JSON: {{"say": "...", "receipt": "..."}}"""
    if errs:
        p += f"\n\nYour last try was: {prev}\nIt broke these rules: {'; '.join(errs)}. Write it again and fix every one."
    try:
        out = json.loads(llm(p, model, fmt="json"))
        return str(out.get("say", "")).strip(), str(out.get("receipt", "")).strip()
    except (json.JSONDecodeError, AttributeError):
        return "", ""


NO_RECEIPT = {"share", "end"}                                               # a call to action and a punchline state no fact


def flat(t):
    return " ".join(re.sub(r"[*`_#|>\\]|\[|\]", " ", t.lower().replace("’", "'").replace("“", '"').replace("”", '"')).split())


def check_receipt(receipt, source):
    """The receipt must really be in the sources: plain string search, no model involved."""
    pieces = [flat(x) for x in re.split(r"\s*(?:\.\.\.|…)\s*", receipt) if x.strip()]
    if not pieces or sum(len(x.split()) for x in pieces) < 5:
        return ["receipt missing: copy the supporting sentence from README or FACTS"]
    lost = [x for x in pieces if x not in source]
    return [f"receipt not found word for word in the sources: \"{lost[0][:80]}\" - copy it exactly"] if lost else []


def verify(say, receipt, facts, model):
    """The second bar of the cage: a cold reader (temperature 0) compares the line with its receipt, nothing else."""
    p = f"""You are a strict fact-checker for a reel about {facts['repo']}.
RECEIPT (copied from the repo's README): {receipt}

LINE: {say}

Does the LINE claim anything the RECEIPT does not state? Check only concrete claims about the repo: what it does, its features, numbers, who made, uses or tested it, comparisons.
Such a claim is supported only if the receipt states it (same meaning, same numbers, same actor: "X studied it" is not
"X uses it"). Every number must stay attached to what the sources attach it to: the same measure, unit, hardware, input
size and comparison. Two true numbers from different measurements put side by side ("54 ms on GPU vs ORT at 266 ms",
when 266 ms was a CPU run) are unsupported. Superlatives about the repo ("biggest", "fastest", "game-changing") are unsupported unless stated. Which part does what matters: if the receipt says one component does X, the line
must not give X to another component.
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


def cage(F, model, tries=3, keep=3, with_voice=False, v4=False):
    digest, facts = (F / "repo/digest.md").read_text(), json.loads((F / "repo/facts.json").read_text())
    sheet, rd = fact_sheet(digest, facts), readme(digest)
    ok_nums = allowed_numbers("\n".join(sheet) + rd, facts)
    source = flat("\n".join(sheet) + "\n" + rd)
    story, used, log, receipts = [], set(), [], {}
    for slot in SLOTS:
        cands, near = [], []
        no_receipt = set() if v4 else NO_RECEIPT                         # v4: the call to action and the ending carry a receipt too
        for k in range(keep + (2 * keep if v4 else 0)):                    # v4: a slot without a candidate gets up to 2 more rounds
            if k >= keep and (cands or near):
                break
            say, errs = "", None
            for t in range(tries):
                say, receipt = ask_line(slot, facts, sheet, rd, story, used, model, errs, say, k if v4 else None)
                errs = check_line(say, slot, ok_nums, used, " ".join(s for _, s in story))
                if slot[0] not in no_receipt:
                    errs += check_receipt(receipt, source)
                length_only = bool(say) and all(e.startswith("has ") for e in errs)
                if length_only and slot[0] not in no_receipt:
                    errs += verify(say, receipt, facts, model)
                    length_only = all(e.startswith("has ") for e in errs)
                log.append({"slot": slot[0], "try": t, "say": say, "receipt": receipt, "errs": errs})
                if not errs:
                    cands.append((say, receipt))
                    break
                if length_only:                                     # only the length is off: kept as a fallback
                    near.append((say, receipt))
        pool = cands or near
        best = pick([c[0] for c in pool], slot, facts, story, model) if pool else None
        if best is None:                                                    # the cage holds: a line with a wrong fact never gets in
            log.append({"slot": slot[0], "dropped": True})
            continue
        story.append((slot[0], best))
        receipts[slot[0]] = next(r for s, r in pool if s == best)
        used |= set(numbers_in(best))
    if with_voice:
        story = voice(story, receipts, facts, ok_nums, source, model, log)
    return [s for _, s in story], log


VOICE = {"hook": "Lead with the number in the first five words, then the twist that makes it surprising.",
         "end": "Make it land like the last line of a trailer.",
         "share": "Name exactly who needs this, so the viewer thinks of one person."}


def voice(story, receipts, facts, ok_nums, source, model, log, n=3):
    """REJECTED on dev (results/dev-v3.jsonl): cage2 beats cage3 11/12, errors 1.9 -> 2.7. Kept for the record.
    Cage v3: rewrite each line for the ear. Numbers, names and claims are locked: the rewrite must carry the
    same receipt and pass every bar again (rules, receipt, fact-check), else the caged line stays."""
    SLOT = {s[0]: s for s in SLOTS}
    total = sum(len(s.split()) for _, s in story)
    out = list(story)
    for i, (sid, say) in enumerate(story):
        slot, receipt = SLOT[sid], receipts.get(sid, "")
        lo, hi = slot[2], slot[3]
        if total < 160:                                                 # judges count scripts under 150 words as a flaw
            lo = max(lo, len(say.split()), (lo + hi) // 2)
        before = " ".join(s for _, s in out[:i])                           # like the cage: repeats count against earlier lines
        p = f"""You are the narrator of a 70-second Instagram reel about {facts['repo']}. Rewrite ONE line so it grips
when spoken aloud: rhythm, contrast, a concrete image, active verbs, talk to the viewer as "you". {VOICE.get(sid, "")}
Locked: keep every number exactly as written, every name, and every claim. Add no claim, no number, no superlative,
no marketing word. Plain English, {lo}-{hi} words, at most two sentences.
Say the same thing as the LINE, only better: same facts, nothing from other lines.
LINE BEFORE IT: {out[i - 1][1] if i else "(none, this opens the reel)"}
LINE "{sid}": {say}
""" + (f"Its source: {receipt}\n" if receipt else "") + 'Answer as JSON: {"say": "..."}'
        cands = [say]
        for _ in range(n):
            try:
                new = str(json.loads(llm(p, model, temperature=0.9, fmt="json")).get("say", "")).strip()
            except (json.JSONDecodeError, AttributeError):
                continue
            errs = check_line(new, (sid, "", lo, hi, slot[4]), ok_nums, set(numbers_in(before)), before)
            if sorted(numbers_in(new)) != sorted(numbers_in(say)):
                errs.append("numbers changed")
            if not errs and sid not in NO_RECEIPT:
                errs = check_receipt(receipt, source) + verify(new, receipt, facts, model)
            log.append({"slot": sid, "voice": new, "errs": errs})
            if not errs:
                cands.append(new)
        if len(cands) > 1:
            menu = "\n".join(f"{k}: {c}" for k, c in enumerate(cands))
            q = f"""Reel about {facts['repo']}. Which version of the line "{sid}" would a viewer most want to keep listening to?
Spoken aloud, gripping, clear, natural. {menu}
Answer as JSON: {{"best": <index>}}"""
            try:
                out[i] = (sid, cands[int(json.loads(llm(q, model, temperature=0, fmt="json"))["best"])])
            except (KeyError, ValueError, IndexError, TypeError, json.JSONDecodeError):
                pass
        total += len(out[i][1].split()) - len(say.split())
    return out


def free(F, model):
    digest, facts = (F / "repo/digest.md").read_text(), json.loads((F / "repo/facts.json").read_text())
    p = f"""{GUIDE.read_text()}

The digest of THIS repo ({facts['url']}) - the only source of facts:
{digest}

Write only the narration: 11-13 lines, 150-190 words in all. Answer as JSON: {{"lines": [{{"id": "...", "say": "..."}}]}}"""
    for _ in range(2):                                                      # fair to the free arm: read any key, retry once
        try:
            out = json.loads(llm(p, model, fmt="json"))
        except json.JSONDecodeError:
            continue
        items = out.get("lines", []) if isinstance(out, dict) else []
        lines = [l if isinstance(l, str) else next((v for v in l.values() if isinstance(v, str) and len(v.split()) > 2), "")
                 for l in items if isinstance(l, (str, dict))]
        lines = [l.replace(" / ", " ").replace("/", " ") for l in lines if l]
        if lines:
            return lines, []
    sys.exit(f"free {F.name}: no lines")


def gold(F):
    return [l["say"].replace(" / ", " ").replace("/", " ") for l in json.loads((F / "story.json").read_text())["lines"]], []


if __name__ == "__main__":
    F, arm = Path(sys.argv[1]).resolve(), sys.argv[2]
    model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "qwen3:8b"
    lines, log = gold(F) if arm == "gold" else free(F, model) if arm == "free" else cage(F, model, with_voice=arm == "cage3", v4=arm == "cage4")
    if arm.startswith("cage") and len(lines) < 10:                       # was == "cage": let cage2 claude-mem in with 9 lines
        sys.exit(f"cage {F.name}: only {len(lines)} lines passed - not saved as a result")
    out = HERE / "out" / arm / (model.replace(":", "_").replace("/", "_") if arm != "gold" else "gold") / f"{F.name}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"lines": lines, "words": sum(len(l.split()) for l in lines), "log": log}, indent=1, ensure_ascii=False))
    print(f"{arm} {F.name}: {len(lines)} lines, {sum(len(l.split()) for l in lines)} words -> {out}")
    print("\n".join(lines))
