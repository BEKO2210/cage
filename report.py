"""python3 report.py <tag>: pairwise win rates, judge-flagged errors per script and words per arm from results/<tag>.jsonl."""
import json
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = [json.loads(l) for l in (HERE / "results" / f"{sys.argv[1]}.jsonl").read_text().splitlines()]
arms = sorted({a for r in rows for a in r["ranking"]})
name = lambda a: a.split("/")[1]

wins = defaultdict(int)
for r in rows:
    for i, a in enumerate(r["ranking"]):
        for b in r["ranking"][i + 1:]:
            wins[a, b] += 1
print(f"{len(rows)} verdicts, {len({r['film'] for r in rows})} repos, judges: {', '.join(sorted({r['judge'] for r in rows}))}")
for a, b in combinations(arms, 2):
    n = wins[a, b] + wins[b, a]
    print(f"  {name(a)} beats {name(b)}: {wins[a, b]}/{n} = {wins[a, b] / n:.0%}")
for a in arms:
    errs = [len(r["errors"].get(a, [])) for r in rows]
    words = [json.loads((HERE / a / f"{f}.json").read_text())["words"] for f in sorted({r["film"] for r in rows})]
    print(f"  {name(a)}: {sum(errs) / len(errs):.1f} flagged errors per script, words {min(words)}-{max(words)}")
