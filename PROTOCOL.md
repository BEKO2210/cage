# cage – protocol (written before the test run, 2026-10-09)

**Claim to test:** a free local 8-9B model on an 8 GB consumer GPU (RTX 3070), held in a cage, writes reel narration that
blind judges rate as good as the published narration written with frontier models (Opus, GPT) and approved by a human.

## Task
Narration (spoken text only) for a 65-80 s Instagram reel about one GitHub repo. Input: the repo digest the reel
pipeline builds (`~/motion-studio/films/<repo>/repo/digest.md` + `facts.json`). 16 repos have a published reel.

## Arms
- **gold** – the published narration (`story.json`), written by Opus or codex, reviewed by Claude, approved by Belkis.
- **free** – the local model, one prompt, the same guide the frontier models get. No cage.
- **cage** – the same local model, one slot at a time (fixed arc), every line through hard rules
  (numbers verbatim from the digest, no superlatives, no code marks, no filler) and a cold fact-checker pass,
  repaired up to 3 times; 3 candidates per slot, the model picks one. A line with a wrong fact never gets in.

## Split (fixed now, never changed)
- **dev (cage and model built here):** caveman, statim-auto, archify, openclaw
- **test (untouched until the final run):** claude-mem, diagram-design, e2e, jev-ultrafast, marketingskills, mirofish,
  nullmotion, openmontage, photocraft, ponytail, starnet, strata

The model for the test run is chosen on dev only.

## Judges
Three companies, so no judge favours its own maker: codex `gpt-5.6-sol` (OpenAI), `agy` (Google Gemini), Cursor
`cursor-grok-4.5-high` (xAI). Each sees the digest and the three scripts as X/Y/Z in its own seeded order, ranks them and
lists factual errors. Known bias against the cage: some gold scripts were drafted by codex.

## Success, decided in advance
- **Parity:** cage beats gold in >= 45 % of pairwise judgments on the test set.
- **Cage works:** cage beats free in >= 70 %.
- **Accuracy:** cage has no more judge-flagged factual errors per script than gold.
- **Stop:** cage beats gold in < 30 % – report it as it is.

## Frozen for the test run (2026-10-10, before any test repo was touched)
- Model: `qwen3.5:9b` (Ollama, Q4_K_M, num_ctx >= 8192), chosen on dev: 4/4 repos passed; qwen3:8b 2/4; granite4.2:8b 0/2
  (unusable as fact-checker: rejects true lines).
- Cage = arm `cage2` at git tag `frozen-test`: 13 slots; hard rules; every factual line carries a **receipt** (verbatim
  source quote, checked by plain string search); the fact-checker compares the line with its receipt only, fails closed.
- Dev result of this design (tag `dev-v2`, 11 verdicts): cage beats free 100 %, cage beats gold 36 %, judge-flagged errors
  per script: cage 1.3, gold 3.1, free 4.1. Length was 141-146 words, so one slot (`detail2`) was added; archify re-run: 172 words.
- Observed bias, reported not fixed: the free arm copies the example from the story guide ("beats an 8B-parameter LLM").
