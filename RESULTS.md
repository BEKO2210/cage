# cage – test result (12 untouched repos, 36 blind verdicts)

Run at git tag `frozen-test`, model `qwen3.5:9b` on one RTX 3070 (8 GB), judges codex `gpt-5.6-sol` (OpenAI),
`agy` (Google Gemini), Cursor `cursor-grok-4.5-high` (xAI). Raw verdicts: `results/test.jsonl`, `python3 report.py test`.

| Measure (decided in advance, PROTOCOL.md) | Target | Result | |
|---|---|---|---|
| cage beats gold (published narration by frontier models, human-approved) | >= 45 % | **42 %** (15/36) | missed narrowly |
| cage beats free (same small model, no cage) | >= 70 % | **94 %** (34/36) | met |
| judge-flagged factual errors per script, cage vs gold | cage <= gold | **2.7 vs 4.6** | met |
| stop line | cage beats gold < 30 % | 42 % | not hit |

Errors flagged in all 36 verdicts: gold 166, free 112, cage 97. Per judge, cage beat gold: codex 7/12, Gemini 4/12,
Grok 4/12. Per repo, cage beat gold with all three judges on openmontage and starnet, with none on claude-mem,
diagram-design and strata.

## What it means
- The cage turns a free 9B model from unusable (free arm: 9-129 words, several one-line answers) into narration that
  wins 42 % of blind comparisons against frontier-written scripts.
- The receipts (every line carries a verbatim source quote, checked by string search) make it **more accurate than the
  frontier scripts** by the judges' count. Judges prefer gold for hook and voice; the cage text is correct but plainer.

## Honest limits
- Gold authors saw the real repo page, the judges only the digest: some "errors" in gold (e.g. a cost figure) may be true
  facts the digest lacks. The accuracy gap is real in direction, its size is uncertain.
- The `< 10 lines` guard checked the arm name `cage`, not `cage2`, so claude-mem went in with 9 lines / 129 words. Kept
  as is (it can only hurt the cage). Five cage scripts are under 150 words, which judges count as a flaw.
- The free arm is a weak baseline: on long digests the model returned one line; it also copies the story guide's example.
- Narration only. Shots, music and render are not part of this test. 12 repos is a small sample.
