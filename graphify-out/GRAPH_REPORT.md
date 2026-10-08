# Graph Report - cage  (2026-10-09)

## Corpus Check
- 20 files · ~5,237 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 1 file(s) not represented in the graph (top: (none) 1)

## Summary
- 39 nodes · 75 edges · 6 communities (4 shown, 2 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.76)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e95faf0d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- cage.py
- json
- judge.py
- cage – protocol (written before the test run, 2026-10-09)
- subprocess
- run-dev.sh script

## God Nodes (most connected - your core abstractions)
1. `cage()` - 10 edges
2. `llm()` - 7 edges
3. `cage – protocol (written before the test run, 2026-10-09)` - 6 edges
4. `verify()` - 5 edges
5. `numbers_in()` - 4 edges
6. `check_line()` - 4 edges
7. `ask_line()` - 4 edges
8. `pick()` - 4 edges
9. `norm()` - 3 edges
10. `allowed_numbers()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `llm()` --calls--> `subprocess`  [EXTRACTED]
  cage.py →   _Bridges community 1 → community 4_
- `cage()` --calls--> `ask_line()`  [EXTRACTED]
  cage.py → cage.py  _Bridges community 1 → community 0_
- `parse()` --calls--> `json`  [EXTRACTED]
  judge.py →   _Bridges community 2 → community 1_
- `parse()` --calls--> `re`  [EXTRACTED]
  judge.py →   _Bridges community 2 → community 0_

## Import Cycles
- None detected.

## Communities (6 total, 2 thin omitted)

### Community 0 - "cage.py"
Cohesion: 0.44
Nodes (7): allowed_numbers(), cage(), check_line(), fact_sheet(), norm(), numbers_in(), readme()

### Community 1 - "json"
Cohesion: 0.39
Nodes (6): ask_line(), free(), gold(), llm(), pick(), verify()

### Community 3 - "cage – protocol (written before the test run, 2026-10-09)"
Cohesion: 0.29
Nodes (6): Arms, cage – protocol (written before the test run, 2026-10-09), Judges, Split (fixed now, never changed), Success, decided in advance, Task

### Community 4 - "subprocess"
Cohesion: 0.60
Nodes (3): codex(), gemini(), grok()

## Knowledge Gaps
- **5 isolated node(s):** `Task`, `Arms`, `Split (fixed now, never changed)`, `Judges`, `Success, decided in advance`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 12 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `verify()` connect `json` to `cage.py`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **What connects `Task`, `Arms`, `Split (fixed now, never changed)` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `run-dev.sh script` connect `run-dev.sh script` to `cage.py`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `cage()` connect `cage.py` to `json`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._