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

## After the test: a voice pass (dev set only, 2026-10-09) – rejected
Idea: after the cage, the same 9B model rewrites every line for the ear; numbers and receipt locked, every rewrite goes
through all bars again. Arm `cage3`, judged blind on the 4 dev repos against gold and the frozen cage (12 verdicts,
`results/dev-v3.jsonl`):

| | result |
|---|---|
| cage2 beats cage3 | 11/12 = 92 % |
| cage3 beats gold | 3/12 = 25 % (cage2: 5/12 = 42 %) |
| flagged errors per script | cage2 1.9 · gold 3.2 · cage3 2.7 |

Why it failed: "flair" is where a small model invents claims ("the only choice", "instant answers"), mostly in the
share and end lines, which carry no receipt, and the 9B fact-checker lets meaning-shifting paraphrases through.
Lesson: style cannot be bolted on after the cage; the receipt must cover every line, including the call to action.
Kept from this round: the line-count guard now covers every cage arm, and `*` (bold marks) counts as markup.

## cage4 (dev set only, 2026-10-09) – rejected
Patterns for hook/problem/end on candidates 2-3, receipts for share and end, and up to 2 extra rounds for a slot without
a candidate. Slots no longer drop (12-13 lines), but cage2 beats cage4 9/12, flagged errors 1.4 (cage2) vs 3.2 (cage4)
(`results/dev-v4.jsonl`). Lesson: every extra try is another chance for a wrong line to slip past the 9B fact-checker
(mostly pairing errors: two true numbers joined wrongly, "per model" for "per mode"). The checker is the bottleneck,
not the writer. Next: cage5 = two independent checks must both pass (receipt check + a number-pairing check).
