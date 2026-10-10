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

# Protocol v2 (written 2026-10-10, before any cage run on the v2 test set)

**Why v2:** in v1 the gold authors saw the full repo page while judges saw only the digest, and the 12 test repos are
now used up. On the dev set, one run per repo proved too noisy to rank designs: the same cage2 algorithm, run again
(`cage2r`), beat the frozen cage2 scripts 9/12 and gold 50 % (`results/dev-v6.jsonl`). So v2 decides on 20 fresh repos.

## Test set v2 (fixed in commit c45acb3, before any cage run on it)
Rule: most-starred GitHub repos created after 2026-03-01, pushed after 2026-09-15, English README, no lists, not in v1.
career-ops, cli-anything, colibri, dbx, deepseek-harness, ds4, freellmapi, gods-eye-view, graphify, herdr, hyperframes,
i-have-adhd, mempalace, obscura, odysseus, orca, paperclip, pretext, understand-anything, voicestudio.

## Arms
- **gold2** – narration by Opus 5.5 from the digest only (the same input as the cage), written once, not edited.
- **cage2** – the v1 cage algorithm, unchanged (writer and fact-checker `qwen3.5:9b`).
- **cage6** – cage2 + code pairing check (every number of a line must stand in its receipt sentence next to the words
  the line puts around it) + fact-checker `gemma4:12b-it-qat` (another model family). Chosen on `data/checker-bank.jsonl`
  (23 dev pairs): qwen3.5:9b caught 3/12 wrong lines, gemma4:12b 11/12 while rejecting 1/11 true ones.
Judges as in v1 (codex gpt-5.6-sol, Gemini, Grok), Latin-square order, 60 verdicts.

## Success, decided in advance
- **Parity:** cage2 or cage6 beats gold2 in >= 45 % of pairwise judgments.
- **Accuracy:** that arm has no more judge-flagged errors per script than gold2.
- **Checker:** cage6 has fewer flagged errors per script than cage2 (the claim behind v6).
- **Stop:** both cages beat gold2 in < 30 % – report it as it is.
