# Egonex-AI/Understand-Anything
Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
stars 85754 · forks 7214 · TypeScript · licence MIT · release v2.9.0 (2026-07-10) · pushed 2026-10-09 · topics antigravity-skills, business-knowledge, claude-code, claude-skills, codebase-analysis, codex, codex-skills, developer-tools-ai-agent
languages {'TypeScript': 59.9, 'JavaScript': 28.5, 'Python': 8.0, 'Astro': 2.4, 'CSS': 0.4}

## README by section
### (intro)
Understand Anything Turn any codebase, knowledge base, or docs into an interactive knowledge graph you can explore, search, and ask questions about.
### ✨ Features
> [!NOTE] > **Want to skip the reading?** Try the live demo in our homepage — a fully interactive dashboard you can pan, zoom, search, and explore right in your
### Explore the structural graph
Navigate your codebase as an interactive knowledge graph — every file, function, and class is a node you can click, search, and explore.
### Understand business logic
Switch to the domain view and see how your code maps to real business processes — domains, flows, and steps laid out as a horizontal graph.
### Analyze knowledge bases
Point `/understand-knowledge` at a Karpathy-pattern LLM wiki and get a force-directed knowledge graph with community clustering.
### 🚀 Quick Start
### 1. Install the plugin
> **Using a local model?** For privacy or enterprise setups, point your platform at a local model provider such as Ollama — follow their integration guide to ch
```
/plugin marketplace add Egonex-AI/Understand-Anything
/plugin install understand-anything
```
### 2. Analyze your codebase
A multi-agent pipeline scans your project, extracts every file, function, class, and dependency, then builds a knowledge graph saved to `.ua/knowledge-graph.jso
```
/understand
```
```
# Generate Chinese content (知识图节点描述和 Dashboard UI)
/understand --language zh

# Supported languages: en (default), zh, zh-TW, ja, ko, ru, vi
```
### 3. Explore the dashboard
An interactive web dashboard opens with your codebase visualized as a graph — color-coded by architectural layer, searchable, and clickable.
```
/understand-dashboard
```
### 4. Keep learning
---
```
# Ask anything about the codebase
/understand-chat How does the payment flow work?

# Analyze impact of your current changes
...
```
### 🌐 Multi-Platform Installation
Understand-Anything works across multiple AI coding platforms.
### Claude Code (Native)
```
/plugin marketplace add Egonex-AI/Understand-Anything
/plugin install understand-anything
```
### One-line install (Codex / OpenCode / OpenClaw / Antigravity / Gemini CLI / Pi Agent / Vibe CLI / VS Code Copilot / Hermes / Cline / KIMI CLI / Trae / Nanobot / Kiro)
**macOS / Linux:** **Windows (PowerShell):** The installer clones the repo to `~/.understand-anything/repo` and creates the right symlinks for the chosen platfo
```
curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash
# or skip the prompt by passing the platform:
curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash -s
```
```
iwr -useb https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.ps1 | iex
```
### Cursor
Cursor auto-discovers the plugin via `.cursor-plugin/plugin.json` when this repo is cloned.
### VS Code + GitHub Copilot
VS Code with GitHub Copilot (v1.108+) auto-discovers the plugin via `.copilot-plugin/plugin.json` when this repo is cloned.
### Copilot CLI
```
copilot plugin install Egonex-AI/Understand-Anything:understand-anything-plugin
```
### Kiro CLI / IDE
After installation: - **Kiro CLI**: `kiro-cli chat --agent understand "Analyze this project"` - **Kiro IDE**: The skills are symlinked into `~/.kiro/skills/` an
```
curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash -s
```
### Platform Compatibility
---
| Platform | Status | Install Method |
| Claude Code | ✅ Native | Plugin marketplace |
| Cursor | ✅ Supported | Auto-discovery |
| VS Code + GitHub Copilot | ✅ Supported | Auto-discovery |
| Copilot CLI | ✅ Supported | Plugin install |
| Codex | ✅ Supported | `install.sh codex` |
|...
### 📦 Share the Graph with Your Team
The graph is just JSON — **commit it once, and teammates skip the pipeline**.
```
.ua/intermediate/
.ua/diff-overlay.json
```
```
git lfs install
git lfs track ".ua/*.json"
git add .gitattributes .ua/
```
### View the dashboard without Claude Code
Once a graph has been generated and committed, anyone on the team can open it with one command — no Claude Code, no LLM, no API key.
```
npx https://github.com/Egonex-AI/Understand-Anything/releases/latest/download/understand-anything-vi
```
### 🔧 Under the Hood
### Tree-sitter + LLM hybrid
Static analysis and LLMs do what each does best: - **Tree-sitter (deterministic)** — parses source into a concrete syntax tree and extracts structural facts: im
### Multi-Agent Pipeline
The `/understand` command orchestrates 5 specialized agents, `/understand-domain` adds a 6th, and `/understand-knowledge` adds a 7th: File analyzers run in para
| Agent | Role | Used By |
| `project-scanner` | Discovers files, detects languages and frameworks | `/understand` |
| `file-analyzer` | Extracts functions, classes, imports; produces graph nodes and edges | `/understand` |
| `architecture-analyzer` | Identifies architectural layers | `/understand` |
| `tour-builder` | Generates guided learning tours | `/understand` |
| `graph-reviewer` | Validates graph completeness and referential integrity. Runs inline by default; use `--review` for full LLM r
|...
### 🎥 Community
A community-made walkthrough by **Better Stack**.
### 🤝 Contributing
Contributions are welcome!
### Star History
Thanks to everyone who's used and contributed — knowing this saves people time is what made it worth building.

## Sentences with numbers (verbatim)
- The codebase is 200,000 lines of code.
- 📚 Language Concepts 12 programming patterns (generics, closures, decorators, etc.) explained in context wherever they appear.
- **Large graphs (10 MB+):** track with **git-lfs**.
- ### Multi-Agent Pipeline The `/understand` command orchestrates 5 specialized agents, `/understand-domain` adds a 6th, and `/understand-knowledge` adds a 7th: | Agent | Role | Used
- Runs inline by default; use `--review` for full LLM review | `/understand` | | `domain-analyzer` | Extracts business domains, flows, and process steps | `/understand-domain` | | `a

## Page blocks (id kind y: text)
b000 header 172: Understand-Anything Public Notifications Fork7.2k (7.2k) Sta
b001 star 192: Star85.8k (85.8k)
b002 about 250: About Graphs that teach > graphs that impress. Turn any code
b003 files 368: Name Last commit message Last commit date .claude-plugin fix
b006 heading 1572: Understand Anything
b008 text 1639: Turn any codebase, knowledge base, or docs into an interacti
b009 text 1727: Understand Anything. Understand Anyone. AI should help peopl
b011 text 1869: English | 简体中文 | 繁體中文 | 日本語 | 한국어 | Español | Türkçe | Русск
b014 text 2435: You just joined a new team. The codebase is 200,000 lines of
b015 text 2499: Understand Anything is a Claude Code Plugin that analyzes yo
b016 quote 2587: The goal isn't a graph that wows you with how complex your c
b018 heading 2684: ✨ Features
b020 text 2738: Note Want to skip the reading? Try the live demo in our home
b022 text 2778: Want to skip the reading? Try the live demo in our homepage 
b024 heading 2858: Explore the structural graph
b026 text 2899: Navigate your codebase as an interactive knowledge graph — e
b028 heading 2995: Understand business logic
b030 text 3036: Switch to the domain view and see how your code maps to real
b032 heading 3108: Analyze knowledge bases
b034 text 3149: Point /understand-knowledge at a Karpathy-pattern LLM wiki a
b035 table 3261: rows 0-2 (0 = header) 🧭 Guided Tours Auto-generated walkthroughs of the architectu
b037 heading 3761: 🚀 Quick Start
b040 heading 3823: 1. Install the plugin
b042 code 3864: /plugin marketplace add Egonex-AI/Understand-Anything /plugi
b045 quote 3951: Using a local model? For privacy or enterprise setups, point
b047 heading 4023: 2. Analyze your codebase
b049 code 4064: /understand
b052 text 4132: A multi-agent pipeline scans your project, extracts every fi
b053 quote 4244: Heads up on token usage: The initial /understand analyzes yo
b054 text 4356: Localized output: Use --language to generate content in your
b055 code 4396: # Generate Chinese content (知识图节点描述和 Dashboard UI) /understa
b058 text 4523: On the first run in a project — when you don't pass --langua
b059 text 4635: The --language parameter affects:
b060 list 4675: Node summaries and descriptions in the knowledge graph Dashb
b062 heading 4779: 3. Explore the dashboard
b064 code 4820: /understand-dashboard
b067 text 4888: An interactive web dashboard opens with your codebase visual
b069 heading 4984: 4. Keep learning
b071 code 5025: # Ask anything about the codebase /understand-chat How does 
b075 heading 5618: 🌐 Multi-Platform Installation
b077 text 5673: Understand-Anything works across multiple AI coding platform
b079 heading 5721: Claude Code (Native)
b081 code 5762: /plugin marketplace add Egonex-AI/Understand-Anything /plugi
b085 heading 5857: One-line install (Codex / OpenCode / OpenClaw / Antigravity 
b088 code 5988: curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Under
b091 text 6095: Windows (PowerShell):
b092 code 6135: iwr -useb https://raw.githubusercontent.com/Egonex-AI/Unders
b095 text 6203: The installer clones the repo to ~/.understand-anything/repo
b096 quote 6267: Note on invoking skills: the invocation prefix differs per p
b097 list 6379: Supported <platform> values: gemini, codex, opencode, pi, op
b099 heading 6611: Cursor
b101 text 6652: Cursor auto-discovers the plugin via .cursor-plugin/plugin.j
b102 text 6716: If auto-discovery doesn't pick it up, install it manually: o
b104 heading 6788: VS Code + GitHub Copilot
b106 text 6829: VS Code with GitHub Copilot (v1.108+) auto-discovers the plu
b107 text 6893: For personal skills (available across all projects), run the
b109 heading 6941: Copilot CLI
b111 code 6982: copilot plugin install Egonex-AI/Understand-Anything:underst
b115 heading 7058: Kiro CLI / IDE
b117 code 7099: curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Under
b121 list 7207: Kiro CLI: kiro-cli chat --agent understand "Analyze this pro
b122 text 7299: For personal skills (available across all projects), run the
b124 heading 7347: Platform Compatibility
b126 table 7388: rows 0-17 (0 = header) Platform Status Install Method Claude Code ✅ Native Plugin m
b128 heading 8104: 📦 Share the Graph with Your Team
b130 text 8158: The graph is just JSON — commit it once, and teammates skip 
b131 quote 8222: Example: GoogleCloudPlatform/microservices-demo — Go / Java 
b132 text 8286: What to commit: everything in .ua/ except intermediate/ and 
b133 code 8374: .ua/intermediate/ .ua/diff-overlay.json
b136 text 8462: Keep it fresh: enable /understand --auto-update — a post-com
b137 text 8526: Large graphs (10 MB+): track with git-lfs.
b138 code 8566: git lfs install git lfs track ".ua/*.json" git add .gitattri
b142 heading 8681: View the dashboard without Claude Code
b144 text 8722: Once a graph has been generated and committed, anyone on the
b145 code 8786: npx https://github.com/Egonex-AI/Understand-Anything/release
b148 text 8854: The terminal prints a tokenized URL (http://127.0.0.1:5173/?
b149 text 8966: Working from a clone instead? pnpm install && pnpm --filter 
b151 heading 9063: 🔧 Under the Hood
b154 heading 9125: Tree-sitter + LLM hybrid
b156 text 9166: Static analysis and LLMs do what each does best:
b157 list 9206: Tree-sitter (deterministic) — parses source into a concrete 
b158 text 9418: This split is why the graph is reproducible on the structura
b160 heading 9490: Multi-Agent Pipeline
b162 text 9531: The /understand command orchestrates 5 specialized agents, /
b163 table 9595: rows 0-7 (0 = header) Agent Role Used By project-scanner Discovers files, detects 
b164 text 10028: File analyzers run in parallel, up to 5 concurrent workers a
b165 text 10068: The pipeline also supports incremental updates: only files c
b167 heading 10141: 🎥 Community
b169 text 10195: A community-made walkthrough by Better Stack.
b171 text 10552: Made a video, blog post, or tutorial? Open an issue or PR — 
b173 heading 10625: 🤝 Contributing
b175 text 10679: Contributions are welcome! Here's how to get started:
b176 list 10719: Fork the repository Create a feature branch (git checkout -b
b177 text 10843: Please open an issue first for major changes so we can discu
b178 text 10916: Stop reading code blind. Start understanding everything.
b180 heading 10964: Star History
b183 text 11559: Thanks to everyone who's used and contributed — knowing this
b184 text 11623: MIT License © Yuxiang Lin and Infinite Universe, Inc.
b185 media 1979: Understand Anything — Turn any codebase into an interactive 
b186 media 10235: Community walkthrough by Better Stack — watch on YouTube
b187 media 11019: Star History Chart

## Media
m00 block b185 still 1774x887: Understand Anything — Turn any codebase into an interactive knowledge graph
m01 block b186 still 1280x720: Community walkthrough by Better Stack — watch on YouTube
m02 block b187 still 800x533: Star History Chart