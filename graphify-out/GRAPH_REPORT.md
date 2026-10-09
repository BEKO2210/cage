# Graph Report - cage  (2026-10-09)

## Corpus Check
- 116 files · ~162,906 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: .jsonl 4, (none) 2)

## Summary
- 444 nodes · 484 edges · 19 communities (18 shown, 1 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 9 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `467a6508`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- cage.py
- README by section
- README by section
- cage – protocol (written before the test run, 2026-10-09)
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- README by section
- story-guide.md

## God Nodes (most connected - your core abstractions)
1. `README by section` - 39 edges
2. `README by section` - 30 edges
3. `README by section` - 28 edges
4. `README by section` - 27 edges
5. `README by section` - 23 edges
6. `README by section` - 23 edges
7. `README by section` - 16 edges
8. `cage()` - 15 edges
9. `README by section` - 15 edges
10. `README by section` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Honest limits` --references--> `cage()`  [INFERRED]
  RESULTS.md → cage.py
- `Run it` --references--> `llm()`  [INFERRED]
  README.md → cage.py
- `cage` --references--> `cage()`  [INFERRED]
  README.md → cage.py
- `Run it` --references--> `codex()`  [INFERRED]
  README.md → judge.py

## Import Cycles
- None detected.

## Communities (19 total, 1 thin omitted)

### Community 0 - "cage.py"
Cohesion: 0.10
Nodes (26): allowed_numbers(), ask_line(), cage(), check_line(), check_receipt(), fact_sheet(), flat(), free() (+18 more)

### Community 1 - "README by section"
Cohesion: 0.05
Nodes (43): Add API Keys (optional — more keys = more tools), Adding a New Pipeline, Adding a New Tool, Agent Compatibility, Architecture, Budget Controls, calesthio/OpenMontage, Contact (+35 more)

### Community 2 - "README by section"
Cohesion: 0.06
Nodes (34): Available Skills, Content & Copy, Contributing, Conversion Optimization, coreyhaines31/marketingskills, Full rename map, Growth Engineering, How Skills Work Together (+26 more)

### Community 3 - "cage – protocol (written before the test run, 2026-10-09)"
Cohesion: 0.14
Nodes (11): Arms, cage – protocol (written before the test run, 2026-10-09), Frozen for the test run (2026-10-10, before any test repo was touched), Judges, Split (fixed now, never changed), Success, decided in advance, Task, After the test: a voice pass (dev set only, 2026-10-09) – rejected (+3 more)

### Community 4 - "README by section"
Cohesion: 0.06
Nodes (32): About, Accessible by default, Architecture, cathrynlavery/diagram-design, Contrast checks happen automatically, Contributing, Contributing / skin lint, Editable install (+24 more)

### Community 5 - "README by section"
Cohesion: 0.06
Nodes (31): 1. Install, 2. Start from a description — no repository required, 3. Refine in chat, Choose the right diagram, Community, Community and recognition, Contributing, Download it. Open it. Explore it. (+23 more)

### Community 6 - "README by section"
Cohesion: 0.07
Nodes (27): Architecture, Best Practices, Bug Reports, Configuration, Configuration & Development, Contributing, Development, Documentation (+19 more)

### Community 7 - "README by section"
Cohesion: 0.07
Nodes (27): Against ONNX Runtime on CPU, API, At a glance, Authentication, limits, and operations, BEKO2210/statim, Client SDKs, CPU performance, GPU performance (+19 more)

### Community 8 - "README by section"
Cohesion: 0.09
Nodes (21): 1. Wuhan University Public Opinion Simulation + MiroFish Project Introduction, 2. Dream of the Red Chamber Lost Ending Simulation, 666ghj/MiroFish, 📄 Acknowledgments, 🎬 Demo Videos, (intro), 📬 Join the Conversation, 🌐 Live Demo (+13 more)

### Community 9 - "README by section"
Cohesion: 0.10
Nodes (19): Big rock: the proxy, Cite, Everything else, How caveman talks, In the wild, Install, (intro), JuliusBrussee/caveman (+11 more)

### Community 10 - "README by section"
Cohesion: 0.11
Nodes (18): blixvip/NullMotion, Bring your own references, Community, Contributing, FAQ and troubleshooting, How it works, (intro), Media (+10 more)

### Community 11 - "README by section"
Cohesion: 0.11
Nodes (18): Built for agents, Documentation, Everything in the box, Features, Get started, (intro), License and credits, Media (+10 more)

### Community 12 - "README by section"
Cohesion: 0.11
Nodes (17): Community, Contributors, Development, Documentation, Donors and sponsors, Governance, How it fits together, Install (+9 more)

### Community 13 - "README by section"
Cohesion: 0.11
Nodes (17): Already built with Ponytail, Before / after, Commands, DietrichGebert/ponytail, FAQ, How it works, Install, (intro) (+9 more)

### Community 14 - "README by section"
Cohesion: 0.11
Nodes (17): Credits and license, How does it work?, How fast is it?, Install, (intro), Let your AI set it up, Media, Niko1221/Strata (+9 more)

### Community 15 - "README by section"
Cohesion: 0.12
Nodes (16): androoAGI/starnet, Architecture, Coming from OpenClaw or Hermes?, Contributing and security, Download, Features, (intro), License (+8 more)

### Community 16 - "README by section"
Cohesion: 0.12
Nodes (15): Contributing, Documentation, e2e, (intro), Made by TesterArmy, Media, Packages, Page blocks (id kind y: text) (+7 more)

### Community 17 - "README by section"
Cohesion: 0.13
Nodes (14): browser-use/jev-ultrafast, Development, Evidence and limits, (intro), Jev Ultrafast ⚡, Media, Page blocks (id kind y: text), README by section (+6 more)

## Knowledge Gaps
- **343 isolated node(s):** `Task`, `Arms`, `Split (fixed now, never changed)`, `Judges`, `Success, decided in advance` (+338 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 371 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `cage()` connect `cage.py` to `cage – protocol (written before the test run, 2026-10-09)`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **What connects `Task`, `Arms`, `Split (fixed now, never changed)` to the rest of the system?**
  _343 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `cage.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09855072463768116 - nodes in this community are weakly interconnected._
- **Should `README by section` be split into smaller, more focused modules?**
  _Cohesion score 0.045454545454545456 - nodes in this community are weakly interconnected._
- **Should `README by section` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._
- **Should `cage – protocol (written before the test run, 2026-10-09)` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `README by section` be split into smaller, more focused modules?**
  _Cohesion score 0.06060606060606061 - nodes in this community are weakly interconnected._