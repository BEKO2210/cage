"""python3 checker-bench.py <model> [<model> ...]: how well each model guards the cage on data/checker-bank.jsonl
(dev repos only, labelled by hand from the judges' findings). Caught = wrong lines rejected, lost = true lines rejected."""
import json
import sys
from pathlib import Path

from cage import pairing, verify

HERE = Path(__file__).resolve().parent
bank = [json.loads(l) for l in (HERE / "data/checker-bank.jsonl").read_text().splitlines()]
wrong, true = sum(not b["supported"] for b in bank), sum(b["supported"] for b in bank)
for model in sys.argv[1:]:
    tally = {"verify": [0, 0], "pairing": [0, 0], "both": [0, 0]}
    for b in bank:
        facts = {"repo": f"BEKO2210/{b['film']}"}
        v = bool(verify(b["line"], b["receipt"], facts, model))
        p = bool(pairing(b["line"], b["receipt"], facts, model))
        for name, rejected in (("verify", v), ("pairing", p), ("both", v or p)):
            tally[name][0 if not b["supported"] else 1] += rejected
    print(model, " | ".join(f"{k}: caught {c}/{wrong}, lost {l}/{true}" for k, (c, l) in tally.items()), flush=True)
