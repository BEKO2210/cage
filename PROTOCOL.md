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
