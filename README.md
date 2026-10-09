# cage

**A free 9B model on an 8 GB gaming GPU made 41 % fewer factual errors than frontier models,
because every line it writes has to carry a receipt.**

Small local models are cheap but sloppy: they invent numbers, mix up who did what, and drift off the source. `cage`
does not make the model smarter. It takes away the room to be wrong.

```
digest of a GitHub repo
        │
        ▼
 13 fixed slots (hook, problem, what, how, proof, ... share, end)
        │   one slot at a time, 3 candidates each
        ▼
 writer (qwen3.5:9b) ──► {"say": "...", "receipt": "<verbatim quote from the README>"}
        │
        ├─ hard rules (code)     numbers only from the source · no number words · no superlatives · no repeats
        ├─ receipt check (code)  the quote must exist word for word in the source: plain string search
        └─ fact-check (model)    does the line say anything its receipt does not?  (fails closed)
        │
   any error ──► repair (up to 3 tries) ──► a line with a wrong fact never gets in
```

The receipt is the trick. A 9B model cannot reliably check a sentence against 14,000 characters of README. It can check
a sentence against **one quoted sentence**, and code can check that the quote is real.

## Result

Task: narration for a 65-80 s Instagram reel about a GitHub repo. 16 repos with a published reel; 4 for development,
**12 untouched until the final run**. Three arms per repo, ranked blind by three judges from three companies:
codex `gpt-5.6-sol` (OpenAI), Gemini (Google), Grok (xAI). Positions balanced in a Latin square. 36 verdicts.

| | target, fixed in advance | result |
|---|---|---|
| cage beats **gold** (published scripts by frontier models, human-approved) | >= 45 % | **42 %** – missed narrowly |
| cage beats **free** (same 9B model, one prompt, no cage) | >= 70 % | **94 %** |
| factual errors flagged by the judges per script | cage <= gold | **cage 2.7 · gold 4.6** · free 3.1 |

Cost per script: 0 $, about 6 minutes on one RTX 3070. Full numbers and limits: [RESULTS.md](RESULTS.md). Success
criteria, split and model choice were written down before the test run: [PROTOCOL.md](PROTOCOL.md) (git tag `frozen-test`).

**Where it falls short:** judges still prefer the frontier scripts for hook and voice. The cage is correct, not yet
catchy. And the frontier authors saw the full repo page while the judges saw only the digest, so some "errors" in
gold may be true facts the digest lacks.

## Run it

Needs [Ollama](https://ollama.com) with `qwen3.5:9b`, reachable as `ssh pop` (edit `llm()` in `cage.py` for a local
server), and for judging the `codex`, `agy` and `cursor-agent` CLIs.

```sh
python3 cage.py data/caveman cage2 --model qwen3.5:9b   # caged narration -> out/cage2/...
python3 cage.py data/caveman free  --model qwen3.5:9b   # no cage
python3 cage.py data/caveman gold                       # the published script
python3 judge.py mytag caveman --arms out/gold/gold out/free/qwen3.5_9b out/cage2/qwen3.5_9b
python3 report.py test                                  # the published result from results/test.jsonl
```

`data/` holds the repo digests (README extracts of public repos), `out/` every generated script with its full repair
log and receipts, `results/` every verdict with the judges' reasons.

Built by [Belkis Aslani](https://github.com/BEKO2210) with Claude, codex, Cursor and Gemini. Apache-2.0.
