# HKUDS/CLI-Anything
"CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/
stars 51789 · forks 4714 · Python · licence Apache-2.0 · release v0.4.0 (2026-06-25) · pushed 2026-09-22 · topics 
languages {'Python': 97.0, 'C#': 1.6, 'Shell': 0.6, 'JavaScript': 0.4, 'PowerShell': 0.2}

## README by section
### (intro)
&nbsp; CLI-Anything: Making ALL Software Agent-Native &#32;&#32; Today's Software Serves Humans👨‍💻.
### 📰 News
> Thanks to all invaluable efforts from the community!
### 🤔 Why CLI?
CLI is the universal interface for both humans and AI agents: • **Structured & Composable** - Text commands match LLM format and chain for complex workflows • *
### 🚀 Quick Start
CLI-Anything has two equally useful starting points: Phase 1: Empower yourself — your CLI toolkit Install the CLI-Hub package manager first.
| Goal | Start Here |
| **Use the existing CLI ecosystem now** | Install `cli-anything-hub`, browse the registry, and install ready-made CLIs. |
| **Build a new agent-native CLI** | Install the CLI-Anything plugin/skill for your agent, then run the 7-phase harness generator.
| Command | What it does |
| `cli-hub list` | Browse the registry |
| `cli-hub search ` | Search by keyword |
|...
```
pip install cli-anything-hub
```
```
# Browse what is available
cli-hub list
cli-hub search image

...
```
### Pick Your Agent Platform
⚡ Claude Code **Step 1: Add the Marketplace** CLI-Anything is distributed as a Claude Code plugin marketplace hosted on GitHub.
| Command | Description |
| `/cli-anything ` | Build a complete CLI harness |
| `/cli-anything:refine [focus]` | Refine an existing CLI harness |
| `/cli-anything:test ` | Run tests for a CLI harness |
| `/cli-anything:validate ` | Validate a CLI harness |
| `/cli-anything:list [options]` | List all CLI-Anything tools |
|...
```
# Add the CLI-Anything marketplace
/plugin marketplace add HKUDS/CLI-Anything
```
```
# Install the cli-anything plugin from the marketplace
/plugin install cli-anything
```
### Use the Generated CLI
Regardless of which platform you used to build it, the generated CLI works the same way: Each in-repo harness now has a canonical `SKILL.md` at `skills/cli-anyt
```
# Install to PATH
cd gimp/agent-harness && pip install -e .

# Use from anywhere
...
```
### 🤖 Empower Your Agents with CLI-Hub
CLI-Hub lets agents autonomously discover, install, and use the CLIs they need.
```
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
```
```
Find appropriate CLI software in CLI-Hub and complete the task: ...
```
### 💡 CLI-Anything's Vision: Building Agent-Native Software
• 🌐 **Universal Access** - Every software becomes instantly agent-controllable through structured CLI.
### 🔧 When to Use CLI-Anything
---
| Category | How to be Agent-native | Notable Examples |
| **📂 GitHub Repositories** | Transform any open-source project into agent-controllable tools through automatic CLI generation | V
| **🤖 AI/ML Platforms** | Automate model training, inference pipelines, and hyperparameter tuning through structured commands | St
| **📊 Data & Analytics** | Enable programmatic data processing, visualization, and statistical analysis workflows | JupyterLab, Ap
| **💻 Development Tools** | Streamline code editing, building, testing, and deployment processes via command interfaces | Jenkins,
| **🎨 Creative & Media** | Control content creation, editing, and rendering workflows programmatically | Blender, GIMP, OBS Studio
|...
### CLI-Anything's Key Features
### The Agent-Software Gap
AI agents are great at reasoning but terrible at using real professional software.
| **Current Pain Point** | **CLI-Anything's Fix** |
| 🤖 "AI can't use real tools" | Direct integration with actual software backends (Blender, LibreOffice, FFmpeg) — full professiona
| 💸 "UI automation breaks constantly" | No screenshots, no clicking, no RPA fragility. Pure command-line reliability with structur
| 📊 "Agents need structured data" | Built-in JSON output for seamless agent consumption + human-readable formats for debugging |
| 🔧 "Custom integrations are expensive" | One Claude plugin auto-generates CLIs for ANY codebase through proven 7-phase pipeline |
| ⚡ "Prototype vs Production gap" | 2,280+ tests with real software validation. Battle-tested across 18 major applications |
### 🎯 What Can You Do with CLI-Anything?
### 🛠️ Let Agents Take Your Workflows
Professional or everyday — just throw the codebase at `/cli-anything`.
### 🔗 Unify Scattered APIs into One CLI
Tired of juggling fragmented web service APIs?
### 🚀 Replace or Supercharge GUI Agents
CLI-Anything can flat-out **replace GUI-based agent approaches** — no more screenshots, no brittle pixel-clicking.
### ✨ ⚙️ How CLI-Anything Works
### 🏗️ Fully Automated 7-Phase Pipeline
From codebase analysis to PyPI publishing — the plugin handles architecture design, implementation, test planning, test writing, and documentation completely au
### 🎯 Authentic Software Integration
Direct calls to real applications for actual rendering.
### 🔁 Smart Session Management
Persistent project state with undo/redo capabilities, plus unified REPL interface (ReplSkin) that delivers consistent interactive experience across all CLIs.
### 📦 Zero-Config Installation
Simple pip install -e .
### 🧪 Production-Grade Testing
Multi-layered validation: unit tests with synthetic data, end-to-end tests with real files and software, plus CLI subprocess verification of installed commands.
### 🐍 Clean Package Architecture
All CLIs organized under cli_anything.* namespace — conflict-free, pip-installable, with consistent naming: cli-anything-gimp, cli-anything-blender, etc.
### 🤖 SKILL.md Generation
Each generated CLI now has a canonical `SKILL.md` at `skills/cli-anything-/SKILL.md`.
### 🎬 Real-World Demos
AI agents using generated CLIs to produce complete, useful artifacts — no GUI needed.
### FreeCAD &mdash; Curiosity Rover via Preview, Live Preview, and Trajectory
> **Harness:** `cli-anything-freecad` | **Preview Stack:** `preview` + `preview live` + `trajectory.json` | **Artifact:** Agent-built Curiosity-style rover An a
### Blender &mdash; Orbital Relay Drone via Preview, Live Preview, and Trajectory
> **Harness:** `cli-anything-blender` | **Preview Stack:** `preview` + `preview live` + `trajectory.json` | **Artifact:** Agent-built orbital relay drone An age
### Draw.io &mdash; HTTPS Handshake Diagram
> **Harness:** `cli-anything-drawio` | **Time:** ~4 min | **Artifact:** `.drawio` + `.png` An agent creates a full HTTPS connection lifecycle diagram from scrat
### Slay the Spire II &mdash; Game Automation
> **Harness:** `cli-anything-slay-the-spire-ii` | **Artifact:** Automated gameplay session An agent plays through a Slay the Spire II run using the CLI harness 
### VideoCaptioner &mdash; Auto-Generated Subtitles
> **Harness:** `cli-anything-videocaptioner` | **Artifact:** Captioned video frames An agent uses the VideoCaptioner CLI to automatically generate and overlay s
### ArcGIS Pro &mdash; Live Agent Cartography via the MCP Bridge
> **Harness:** `arcgis-pro` (registered in `public_registry.json`) | **Mode:** live-Pro MCP bridge | **Artifact:** Agent-driven map navigation in a running ArcG
### 🎬 Demonstrations
### 🎯 General-Purpose
CLI-Anything works on any software with a codebase — no domain restrictions or architectural limitations.
### 🏭 Professional-Grade Testing
Tested across 18 diverse, complex applications spanning creative, productivity, communication, diagramming, AI image generation, AI content generation, network 
### 🎨 Diverse Domain Coverage
From creative workflows (image editing, 3D modeling, vector graphics) to production tools (audio, office, live streaming, video editing).
### ✅ Full CLI Generation
Each application received complete, production-ready CLI interfaces — not demos, but comprehensive tool access preserving full capabilities.
### 📊 Test Results
Each CLI harness undergoes rigorous multi-layered testing to ensure production reliability: ---
| Layer | What it tests | Example |
| **Unit tests** | Every core function in isolation with synthetic data | `test_core.py` — project creation, layer ops, filter par
| **E2E tests (native)** | Project file generation pipeline | Valid ODF ZIP structure, correct MLT XML, SVG well-formedness |
| **E2E tests (true backend)** | Real software invocation + output verification | LibreOffice → PDF with `%PDF-` magic bytes, Blen
| **CLI subprocess tests** | Installed command via `subprocess.run` | `cli-anything-gimp --json project new` → valid JSON output |
```
================================ Test Summary ================================
gimp          107 passed  ✅   (64 unit + 43 e2e)
blender       208 passed  ✅   (150 unit + 58 e2e)
inkscape      202 passed  ✅   (148 unit + 54 e2e)
...
```
### 🏗️ CLI-Anything's Architecture
### 🎯 Core Design Principles
1.
### 📂 Project Structure
Each `agent-harness/` contains an installable Python package under `cli_anything./` with Click CLI, core modules, utils (including `repl_skin.py` and backend wr
```
cli-anything/
├── 📄 README.md                          # You are here
├── 📁 assets/                            # Images and media
│   ├── icon.png                          # Project icon
...
```
### 🎯 Plugin Commands
| Command | Description |
| `/cli-anything ` | Build complete CLI harness — all 7 phases |
| `/cli-anything:refine [focus]` | Refine an existing harness — expand coverage with gap analysis |
| `/cli-anything:test ` | Run tests and update TEST.md with results |
| `/cli-anything:validate ` | Validate against HARNESS.md standards |
### Examples
---
```
# Build a complete CLI for GIMP from local source
/cli-anything /home/user/gimp

# Build from a GitHub repo
...
```
### 🎮 Demo: Using a Generated CLI
Here's what an agent can do with `cli-anything-libreoffice`:
```
# Create a new Writer document
$ cli-anything-libreoffice document new -o report.json --type writer
✓ Created Writer document: report.json

...
```
### REPL Mode
---
```
$ cli-anything-blender
╔══════════════════════════════════════════╗
║       cli-anything-blender v1.0.0       ║
║     Blender CLI for AI Agents           ║
...
```
### 📖 The Standard Playbook: HARNESS.md
HARNESS.md is our definitive SOP for making any software agent-accessible via automated CLI generation.
### Critical Lessons
> See the full methodology: `cli-anything-plugin/HARNESS.md` ---
| Lesson | Description |
| **Use the real software** | The CLI MUST call the actual application for rendering. No Pillow replacements for GIMP, no custom r
| **The Rendering Gap** | GUI apps apply effects at render time. If your CLI manipulates project files but uses a naive export too
| **Filter Translation** | When mapping effects between formats (MLT → ffmpeg), watch for duplicate filter merging, interleaved st
| **Timecode Precision** | Non-integer frame rates (29.97fps) cause cumulative rounding. Use `round()` not `int()`, integer arithm
| **Output Verification** | Never trust that export worked because it exited 0. Verify: magic bytes, ZIP/OOXML structure, pixel an
### 📦 Installation & Usage
### For CLI-Hub Users
```
# Install the package manager
pip install cli-anything-hub

# Browse, search, inspect, and install CLIs
...
```
### For Plugin Users (Claude Code)
```
# Add marketplace & install (recommended)
/plugin marketplace add HKUDS/CLI-Anything
/plugin install cli-anything

...
```
### For Generated CLIs
```
# Install any generated CLI
cd <software>/agent-harness
pip install -e .

...
```
### Running Tests
---
```
# Run tests for a specific CLI
cd <software>/agent-harness
python3 -m pytest cli_anything/<software>/tests/ -v

...
```
### 🤝 Contributing
We welcome contributions!
### Limitations
- **Requires strong foundation models** — CLI-Anything relies on frontier-class models (e.g., Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.4) for reliable harness 
### Roadmap
- [ ] Support for more application categories (CAD, DAW, IDE, EDA, scientific tools) - [ ] Benchmark suite for agent task completion rates - [ ] Community-contr
### 📖 Documentation
Each generated harness also includes: - `.md` — Architecture SOP specific to that application - `tests/TEST.md` — Test plan and results documentation ---
| Document | Description |
| `cli-anything-plugin/HARNESS.md` | The methodology SOP — single source of truth |
| `cli-anything-plugin/README.md` | Plugin documentation — commands, options, phases |
| `cli-anything-plugin/QUICKSTART.md` | 5-minute getting started guide |
| `cli-anything-plugin/PUBLISHING.md` | Distribution and publishing guide |
### ⭐ Star History
If CLI-Anything helps make your software Agent-native, give us a star!
### 📚 Citation
If you find CLI-Anything useful, please cite our technical report: ---
```
@misc{yang2026clianythingagentnativecomputeruse,
      title={CLI-Anything: Towards Agent-Native Computer Use}, 
      author={Yuhao Yang and Tianyu Fan and Chao Huang},
      year={2026},
...
```
### 📄 License
Apache License 2.0 — free to use, modify, and distribute.

## Sentences with numbers (verbatim)
- 📚 **Calibre CLI** merged (#223) with library/search/metadata/conversion/export workflows, 41 unit tests, real-Calibre E2E evidence, and root skill validation.
- - **2026-04-13** 📓 **Obsidian CLI** merged (#211) — knowledge management harness via the Local REST API, with 48 unit tests and 7 E2E tests.
- - **2026-04-08** 🎬 **Openscreen CLI** merged (#183) — screen recording editor harness with 101 tests.
- ☁️ **CloudAnalyzer CLI** merged (#181) — cloud cost analysis harness with 27 commands.
- 🔧 **Inkscape** auto-save fix (#193, fixes #182).
- 🛰️ **IntelWatch** was added to the registry for B2B OSINT workflows.
- Phases 1–7 now contiguous.
- - **2026-03-24** 🏭 **FreeCAD CLI** added with 258 commands across 17 groups.
- This adds 5 slash commands: `/cli-anything`, `/cli-anything-refine`, `/cli-anything-test`, `/cli-anything-validate`, and `/cli-anything-list`.
- Current solutions are fragile UI automation, limited APIs, or dumbed-down reimplementations that miss 90% of functionality.
- Pure command-line reliability with structured interfaces | | 📊 "Agents need structured data" | Built-in JSON output for seamless agent consumption + human-readable formats for debu
- Battle-tested across 18 major applications | --- ## 🎯 What Can You Do with CLI-Anything?
- Software Domain CLI Command Backend Tests 🎨 GIMP Image Editing cli-anything-gimp Pillow + GEGL/Script-Fu ✅ 107 🧊 Blender 3D Modeling & Rendering cli-anything-blender bpy (Python sc
- --- ## 🎯 Plugin Commands | Command | Description | |---------|-------------| | `/cli-anything ` | Build complete CLI harness — all 7 phases | | `/cli-anything:refine [focus]` | Ref
- | | **Timecode Precision** | Non-integer frame rates (29.97fps) cause cumulative rounding.
- --- **CLI-Anything** — *Make any software with a codebase Agent-native.* A methodology for the age of AI agents | 18 professional software demos | 2,280 passing tests Thanks for vi

## Page blocks (id kind y: text)
b000 header 172: CLI-Anything Public Notifications Fork4.7k (4.7k) Star51.8k 
b001 star 192: Star51.8k (51.8k)
b002 about 250: About "CLI-Anything: Making ALL Software Agent-Native" -- CL
b003 files 368: Name Last commit message Last commit date .claude-plugin fir
b006 heading 4524: CLI-Anything: Making ALL Software Agent-Native
b012 text 4726: Today's Software Serves Humans👨‍💻. Tomorrow's Users will be 
b013 text 4790: 🌐 CLI-Hub: pip install cli-anything-hub then cli-hub install
b014 text 4854: 🎬 See Demos: Watch AI agents use generated CLIs plus preview
b015 text 4918: 🙋 [Become a Contributor, or Request a CLI]: Join us! Sign up
b018 text 5135: One Command Line: Make any software agent-ready for Pi, Open
b022 heading 5622: 📰 News
b024 quote 5676: Thanks to all invaluable efforts from the community! More up
b025 list 5740: 2026-05-30 🧭 Hermes skill proposed (#320), adding a CLI-Anyt
b026 text 6668: Earlier news (Apr 10–18)
b027 text 6708: Earlier news (Apr 1–9)
b028 text 6748: Earlier news (Mar 23–30)
b029 text 6788: Earlier news (Mar 11–22)
b031 heading 6861: 🤔 Why CLI?
b033 text 6915: CLI is the universal interface for both humans and AI agents
b034 text 6955: • Structured & Composable - Text commands match LLM format a
b035 text 6995: • Lightweight & Universal - Minimal overhead, works across a
b036 text 7035: • Self-Describing - --help flags provide automatic documenta
b037 text 7075: • Proven Success - Claude Code runs thousands of real workfl
b038 text 7115: • Agent-First Design - Structured JSON output eliminates par
b039 text 7155: • Deterministic & Reliable - Consistent results enable predi
b041 heading 7203: 🚀 Quick Start
b043 text 7257: CLI-Anything has two equally useful starting points:
b044 table 7297: rows 0-2 (0 = header) Goal Start Here Use the existing CLI ecosystem now Install c
b045 text 7473: Phase 1: Empower yourself — your CLI toolkit Install the CLI
b046 text 8252: Phase 1.5: Empower your agents — install in one command Give
b047 text 8660: Phase 3: Build a new CLI when the registry does not have one
b049 heading 12004: 🤖 Empower Your Agents with CLI-Hub
b051 text 12058: CLI-Hub lets agents autonomously discover, install, and use 
b052 code 12098: npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill
b055 text 12166: Also available on: ClawHub, SkillHub, SkillHub.cn
b058 code 12246: Find appropriate CLI software in CLI-Hub and complete the ta
b060 text 12314: The meta-skill points agents to the live CLI-Hub catalog, wh
b062 heading 12411: 💡 CLI-Anything's Vision: Building Agent-Native Software
b064 text 12465: • 🌐 Universal Access - Every software becomes instantly agen
b065 text 12505: • 🔗 Seamless Integration - Agents control any application wi
b066 text 12569: • 🚀 Future-Ready Ecosystem - Transform human-designed softwa
b068 heading 12666: 🔧 When to Use CLI-Anything
b070 table 12721: rows 0-17 (0 = header) Category How to be Agent-native Notable Examples 📂 GitHub Re
b072 heading 14493: CLI-Anything's Key Features
b075 heading 14555: The Agent-Software Gap
b077 text 14596: AI agents are great at reasoning but terrible at using real 
b078 text 14660: CLI-Anything's Solution: Transform any professional software
b079 table 14724: rows 0-5 (0 = header) Current Pain Point CLI-Anything's Fix 🤖 "AI can't use real t
b081 heading 15116: 🎯 What Can You Do with CLI-Anything?
b083 table 15170: rows 0-0 (0 = header) 🛠️ Let Agents Take Your Workflows Professional or everyday —
b085 heading 15684: ✨ ⚙️ How CLI-Anything Works
b087 table 15738: rows 0-2 (0 = header) 🏗️ Fully Automated 7-Phase Pipeline From codebase analysis t
b089 heading 16310: 🤖 SKILL.md Generation
b091 text 16351: Each generated CLI now has a canonical SKILL.md at skills/cl
b092 text 16439: What SKILL.md provides:
b093 list 16479: YAML frontmatter with name and description for agent skill d
b094 text 16603: SKILL.md files are auto-generated during Phase 6.5 of the pi
b096 heading 16772: 🎬 Real-World Demos
b098 text 16826: AI agents using generated CLIs to produce complete, useful a
b100 heading 16874: FreeCAD — Curiosity Rover via Preview, Live Preview, and Tra
b102 quote 16915: Harness: cli-anything-freecad | Preview Stack: preview + pre
b103 text 16979: An agent incrementally assembles a Curiosity-inspired rover 
b105 text 17562: README GIF generated from the full local demo video with a s
b107 heading 17610: Blender — Orbital Relay Drone via Preview, Live Preview, and
b109 quote 17651: Harness: cli-anything-blender | Preview Stack: preview + pre
b110 text 17715: An agent uses the Blender harness to grow a hard-surface orb
b112 text 18321: README GIF generated from the full local demo video with a s
b114 heading 18369: Draw.io — HTTPS Handshake Diagram
b116 quote 18410: Harness: cli-anything-drawio | Time: ~4 min | Artifact: .dra
b117 text 18450: An agent creates a full HTTPS connection lifecycle diagram f
b120 text 19004: Contributed by @zhangxilong-43
b122 heading 19052: Slay the Spire II — Game Automation
b124 quote 19093: Harness: cli-anything-slay-the-spire-ii | Artifact: Automate
b125 text 19133: An agent plays through a Slay the Spire II run using the CLI
b127 text 19565: Contributed by @TianyuFan0504
b129 heading 19613: VideoCaptioner — Auto-Generated Subtitles
b131 quote 19654: Harness: cli-anything-videocaptioner | Artifact: Captioned v
b132 text 19694: An agent uses the VideoCaptioner CLI to automatically genera
b133 table 19758: rows 0-1 (0 = header) Sub A Sub B
b134 text 20043: Contributed by @WEIFENG2333
b136 heading 20091: ArcGIS Pro — Live Agent Cartography via the MCP Bridge
b138 quote 20132: Harness: arcgis-pro (registered in public_registry.json) | M
b139 text 20196: An agent drives a live, open ArcGIS Pro session through an M
b141 text 20827: README GIF generated from the full local demo video with a h
b142 text 20867: Contributed by @Jasper0122
b143 text 20907: More CLI demos coming soon.
b145 heading 20980: 🎬 Demonstrations
b148 heading 21042: 🎯 General-Purpose
b150 text 21083: CLI-Anything works on any software with a codebase — no doma
b152 heading 21155: 🏭 Professional-Grade Testing
b154 text 21196: Tested across 18 diverse, complex applications spanning crea
b156 heading 21292: 🎨 Diverse Domain Coverage
b158 text 21333: From creative workflows (image editing, 3D modeling, vector 
b160 heading 21405: ✅ Full CLI Generation
b162 text 21446: Each application received complete, production-ready CLI int
b163 table 21510: rows 0-46 (0 = header) Software Domain CLI Command Backend Tests 🎨 GIMP Image Editi
b164 quote 24802: 100% pass rate across all 2,461 tests — 1,732 unit tests + 5
b166 heading 24899: 📊 Test Results
b168 text 24953: Each CLI harness undergoes rigorous multi-layered testing to
b169 table 24993: rows 0-4 (0 = header) Layer What it tests Example Unit tests Every core function i
b171 code 25291: ================================ Test Summary ==============
b174 heading 26023: 🏗️ CLI-Anything's Architecture
b178 heading 26526: 🎯 Core Design Principles
b180 list 26567: Authentic Software Integration — The CLI generates valid pro
b182 heading 27040: 📂 Project Structure
b185 code 27095: cli-anything/ ├── 📄 README.md # You are here ├── 📁 assets/ #
b187 text 28660: Each agent-harness/ contains an installable Python package u
b189 heading 28757: 🎯 Plugin Commands
b191 table 28811: rows 0-4 (0 = header) Command Description /cli-anything <software-path-or-repo> Bu
b193 heading 29093: Examples
b195 code 29134: # Build a complete CLI for GIMP from local source /cli-anyth
b199 heading 29550: 🎮 Demo: Using a Generated CLI
b201 text 29604: Here's what an agent can do with cli-anything-libreoffice:
b202 code 29644: # Create a new Writer document $ cli-anything-libreoffice do
b206 heading 30173: REPL Mode
b209 code 30214: $ cli-anything-blender ╔════════════════════════════════════
b212 heading 30630: 📖 The Standard Playbook: HARNESS.md
b214 text 30684: HARNESS.md is our definitive SOP for making any software age
b215 text 30748: It encodes proven patterns and methodologies refined through
b216 text 30788: The playbook distills key insights from successfully buildin
b218 heading 30836: Critical Lessons
b220 table 30877: rows 0-5 (0 = header) Lesson Description Use the real software The CLI MUST call t
b221 quote 31308: See the full methodology: cli-anything-plugin/HARNESS.md
b223 heading 31381: 📦 Installation & Usage
b226 heading 31443: For CLI-Hub Users
b228 code 31484: # Install the package manager pip install cli-anything-hub #
b232 heading 31796: For Plugin Users (Claude Code)
b234 code 31837: # Add marketplace & install (recommended) /plugin marketplac
b238 heading 32012: For Generated CLIs
b240 code 32053: # Install any generated CLI cd <software>/agent-harness pip 
b244 heading 32325: Running Tests
b246 code 32366: # Run tests for a specific CLI cd <software>/agent-harness p
b250 heading 32566: 🤝 Contributing
b252 text 32620: We welcome contributions! CLI-Anything is designed to be ext
b253 list 32660: New software targets — Use the plugin to generate a CLI for 
b255 heading 32816: Limitations
b257 list 32857: Requires strong foundation models — CLI-Anything relies on f
b259 heading 33105: Roadmap
b261 list 33146: Support for more application categories (CAD, DAW, IDE, EDA,
b263 heading 33359: 📖 Documentation
b265 table 33413: rows 0-4 (0 = header) Document Description cli-anything-plugin/HARNESS.md The meth
b266 text 33615: Each generated harness also includes:
b267 list 33655: <SOFTWARE>.md — Architecture SOP specific to that applicatio
b269 heading 33756: ⭐ Star History
b271 text 33810: If CLI-Anything helps make your software Agent-native, give 
b275 heading 34440: 📚 Citation
b277 text 34494: If you find CLI-Anything useful, please cite our technical r
b278 code 34534: @misc{yang2026clianythingagentnativecomputeruse, title={CLI-
b282 heading 34792: 📄 License
b284 text 34846: Apache License 2.0 — free to use, modify, and distribute.
b285 text 34919: CLI-Anything — Make any software with a codebase Agent-nativ
b286 text 34919: CLI-Anything — Make any software with a codebase Agent-nativ
b287 text 34959: A methodology for the age of AI agents | 18 professional sof
b290 text 35110: Thanks for visiting ✨ CLI-Anything!
b291 media 5199: CLI-Anything typing demo
b292 media 5302: CLI-Anything Teaser
b293 media 17067: FreeCAD Curiosity rover demo driven by preview, live preview
b294 media 17827: Blender orbital relay drone demo driven by preview, live pre
b295 media 18538: Draw.io CLI demo: building an HTTPS handshake diagram
b296 media 18988: HTTPS handshake sequence diagram
b297 media 19197: Slay the Spire II CLI gameplay demo
b298 media 19803: Video frame before captioning
b299 media 19802: Video frame after captioning
b300 media 20332: ArcGIS Pro live-bridge demo: an agent driving a running ArcG
b301 media 26077: CLI-Anything Architecture
b302 media 33850: Star History Chart

## Media
m00 block b291 animated 79f@7.8 800x80: CLI-Anything typing demo
m01 block b292 still 3584x1184: CLI-Anything Teaser
m02 block b293 animated 238f@10.0 960x540: FreeCAD Curiosity rover demo driven by preview, live preview, and trajectory his
m03 block b294 animated 104f@12.01 960x540: Blender orbital relay drone demo driven by preview, live preview, and trajectory
m04 block b295 animated 7f@0.65 1000x560: Draw.io CLI demo: building an HTTPS handshake diagram
m05 block b296 still 1115x1257: HTTPS handshake sequence diagram
m06 block b297 animated 120f@7.99 720x345: Slay the Spire II CLI gameplay demo
m07 block b298 still 1480x814: Video frame before captioning
m08 block b299 still 1482x824: Video frame after captioning
m09 block b300 animated 248f@14.99 860x484: ArcGIS Pro live-bridge demo: an agent driving a running ArcGIS Pro session over 
m10 block b301 still 2752x1536: CLI-Anything Architecture
m11 block b302 still NonexNone: Star History Chart