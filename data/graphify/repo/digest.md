# Graphify-Labs/graphify
Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
stars 124917 · forks 12061 · Python · licence Apache-2.0 · release v0.9.82 (2026-10-09) · pushed 2026-10-09 · topics ai-agents, antigravity, ast, claude-code, code-analysis, code-search, codex, cursor
languages {'Python': 100.0, 'Dockerfile': 0.0}

## README by section
### (intro)
Read this in other languages 🇺🇸 English | 🇨🇳 简体中文 | 🇯🇵 日本語 | 🇰🇷 한국어 | 🇩🇪 Deutsch | 🇫🇷 Français | 🇪🇸 Español | 🇮🇳 हिन्दी | 🇧🇷 Português | 🇷🇺 Русский | 🇸🇦 العربية
```
uv tool install graphifyy      # install the CLI (or: pipx install graphifyy)
graphify install               # register the skill with your AI assistant
```
```
/graphify .
```
### See it in action
Once the graph is built you query it instead of reading files.
```
$ graphify explain "APIRouter"
Node: APIRouter
  Source:    routing.py L2210
  Community: 2
...
```
### What it does
What you get out of the box: ---
| Capability | What you get |
| **God nodes** | The most-connected concepts, so you see what everything flows through |
| **Communities** | The graph split into subsystems (Leiden), with LLM-free labels |
| **Cross-file links** | `calls` / `imports` / `inherits` / `mixes_in` resolved across ~40 languages via tree-sitter AST |
| **Query, path, explain** | Ask a question, trace the path between two things, or explain one concept, all against `graph.json` |
| **Rationale + doc refs** | `# NOTE:` / `# WHY:` comments and ADR/RFC citations become first-class nodes linked to the code |
|...
### Benchmarks
Every system ran on the same harness with the same model and budgets, scored by a judge blind-validated against a second judge (90.6% agreement, Cohen's kappa 0
| Benchmark | Metric | graphify | Field |
| LOCOMO (n=300) | recall@10 | **0.497** | mem0 0.048, supermemory 0.149 |
| LOCOMO (n=300) | QA accuracy | 45.3% | supermemory 49.7%, mem0 27.3% |
| LongMemEval-S (n=50) | QA accuracy | **76%** | tied with dense RAG |
| ERPNext cross-tool (n=6) | key-fact coverage | **82.0%** | grep/read baseline 70.8% |
| Graph build | LLM credits | **0** | per-token for most systems |
### Prerequisites
**macOS quick install (Homebrew):** **Windows quick install:** **Ubuntu/Debian:** ---
| Requirement | Minimum | Check | Install |
| Python | 3.10+ | `python --version` | python.org |
| uv *(recommended)* | any | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternative)* | any | `pipx --version` | `pip install pipx` |
```
brew install python@3.12 uv
```
```
winget install astral-sh.uv
```
### Install
> **Official package:** The PyPI package is `graphifyy` (double-y).
| Platform | Install command |
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install` (auto-detected) or `graphify install --platform windows` |
| CodeBuddy | `graphify install --platform codebuddy` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
|...
```
# Recommended (isolated env; if 'graphify' isn't found after, run: uv tool update-shell):
uv tool install graphifyy

# Alternatives:
...
```
```
graphify install
```
### Make your assistant always use the graph
Run this once in your project after building a graph: This writes a small config file that tells your assistant to consult the knowledge graph for codebase ques
| Platform | Command |
| Claude Code | `graphify claude install` |
| CodeBuddy | `graphify codebuddy install` |
| Codex | `graphify codex install` |
| OpenCode | `graphify opencode install` |
| Kilo Code | `graphify kilo install` |
|...
### What's in the report
- **God nodes** — the most-connected concepts in your project.
### What files it handles
Terraform module calls with a literal local `source` (`./...` or `../...`) link to a directory module node through an `EXTRACTED` `module_source` edge.
| Type | Extensions |
| Code (37 tree-sitter grammars) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .hpp .cu .cuh .metal .r
| Salesforce Apex | `.cls .trigger` (regex-based; classes, interfaces, enums, methods, triggers, SOQL/DML edges) |
| Terraform / HCL | `.tf .tfvars .hcl` (requires `uv tool install graphifyy[terraform]`) |
| OCaml | `.ml .mli` (requires `uv tool install graphifyy[ocaml]`) |
| Common Lisp | `.lisp .cl .lsp .asd` (requires `uv tool install graphifyy[commonlisp]`) |
|...
```
uv tool install "graphifyy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
graphify extract ./docs --google-workspace
```
### Common commands
See the full command reference below.
```
/graphify .                        # build graph for current folder
/graphify ./docs --update          # re-extract only changed files
/graphify . --cluster-only         # rerun clustering without re-extracting
/graphify . --cluster-only --resolution 1.5      # more granular communities
...
```
### Ignoring files
Create a `.graphifyignore` in your project root — same syntax as `.gitignore`, including `!` negation.
```
# .graphifyignore
node_modules/
dist/
*.generated.py
...
```
### Team setup
For users building a team graph, the `graphify-out/` directory is gitignored by default.
```
git add -f graphify-out/graph.json
git add -f graphify-out/GRAPH_REPORT.md
# git add -f graphify-out/wiki/         # optional: if using the wiki export
# git add -f graphify-out/obsidian/     # optional: if using the Obsidian export
```
### Recommended workflow
Set this up once per clone.
| you do | graphify does |
| `graphify hook install` (once, right after cloning) | installs the hooks below, plus a merge driver so `graph.json` never shows 
| `git commit` | rebuilds automatically — AST only, no API cost |
| `git checkout` / `git switch` (branches) | rebuilds automatically (a file-only `git checkout -- ` does not) |
| `git pull` / `git merge` | run `graphify update .` right after |
| `git push` | nothing to do |
### Using the graph directly
The MCP server gives your assistant structured access: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.
```
# query the graph from the terminal
graphify query "show the auth flow"
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json

...
```
### One-click install (VS Code · Smithery)
Prefer not to edit MCP config by hand?
```
# pick your client (claude, cursor, vscode, windsurf, ...)
npx -y @smithery/cli install graphify/graphify --client claude
```
### Shared HTTP server
`--transport stdio` (the default) spawns one local server per developer.
| Flag | Default | Purpose |
| `--transport {stdio,http}` | `stdio` | Transport to serve on |
| `--host` | `127.0.0.1` | HTTP bind host (use `0.0.0.0` to expose beyond localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Require `Authorization: Bearer ` (or `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
|...
```
docker build -t graphify .
docker run -p 8080:8080 -v "$(pwd)/graphify-out:/data" graphify \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```
### Environment variables
These are only needed for **headless / CI extraction** (`graphify extract`).
| Variable | Used for | When required |
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-compatible endpoint URL (LiteLLM proxy, gateways, ...) | `--backend claude` (default: `https://
| `ANTHROPIC_MODEL` | Model name for the Claude backend — for custom endpoints, use the model name/alias your server exposes | `--
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Google Gemini backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI or OpenAI-compatible APIs | `--backend openai` (local servers accept any non-empty value) |
|...
### Privacy
- **Code files** — processed locally via tree-sitter.
### Troubleshooting
**`graphify: command not found` after installing** The CLI is installed but its bin directory isn't on your shell's `PATH`.
```
python -c "import graphify; print(graphify.__file__)"
```
```
uvx --from graphifyy graphify extract . --backend openai   # names the package explicitly
pip uninstall graphifyy                                    # or remove the old system install
```
### Full command reference
`--no-dedup` also skips coalescing distinct non-AST nodes solely because they share a file and label.
```
/graphify                          # run on current directory
/graphify ./raw                    # run on a specific folder
/graphify ./raw --mode deep        # more aggressive relationship extraction
graphify extract ./raw --code-only # index code only — local AST, no API key (skips docs/PDFs/images
...
```
### Learn more
- docs.graphify.com — full documentation: guides, command reference, and integrations - How it works — the extraction pipeline, community detection, confidence 
### graphify Enterprise
**graphify Enterprise** is the always-on layer built on top of graphify — it applies the same graph approach to your entire working context: meetings, files, do
### Contributing
Contributions are welcome.
### Contributors
Made with contrib.rocks.
### Translations
The README is available in 32 languages.
### Community and links

## Sentences with numbers (verbatim)
- Read this in other languages 🇺🇸 English | 🇨🇳 简体中文 | 🇯🇵 日本語 | 🇰🇷 한국어 | 🇩🇪 Deutsch | 🇫🇷 Français | 🇪🇸 Español | 🇮🇳 हिन्दी | 🇧🇷 Português | 🇷🇺 Русский | 🇸🇦 العربية | 🇮🇷 فارسی | 🇮🇹 Ita
- **Get started** (30 seconds): Then, in your AI assistant: That's it.
- --- ## What it does What you get out of the box: | Capability | What you get | |---|---| | **God nodes** | The most-connected concepts, so you see what everything flows through | |
- With plain `pip`, add `~/.local/bin` (Linux) or `~/Library/Python/3.x/bin` (Mac) to your PATH, or run `python -m graphify`.
- Pick your platform (20+ assistants, click to expand) | Platform | Install command | |----------|----------------| | Claude Code (Linux/Mac) | `graphify install` | | Claude Code (Wi
- - **Suggested questions** — 4–5 questions the graph is uniquely positioned to answer.
- --- ## What files it handles | Type | Extensions | |------|-----------| | Code (37 tree-sitter grammars) | `.py .ts .mts .cts .js .jsx .tsx .mjs .go .rs .java .c .cpp .cc .cxx .h .
- From then on, three of your normal git commands keep the graph current by themselves, and one keeps it in sync with your team: | you do | graphify does | |---|---| | `graphify hook
- ![Install in VS Code](https://insiders.vscode.dev/redirect/mcp/install?name=graphify&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--from%22%2C%22graphifyy%5Bmcp%5D%22%2
- `LFM2.5-8B-A1B-UD-Q4_K_XL` for llama.cpp | `--backend openai` (default: `gpt-4.1-mini`) | | `DEEPSEEK_API_KEY` | DeepSeek backend | `--backend deepseek` | | `MOONSHOT_API_KEY` | Ki
- kimi); `0` disables | | `GRAPHIFY_MAX_RETRY_DEPTH` | How deep a truncated chunk may be bisected and re-extracted (default: 3, so up to 8x sub-calls for one chunk) | optional — lowe
- Off by default — nothing is written unless you opt in (#1797) | optional | | `GRAPHIFY_QUERY_LOG` | Enable the query log and write it to this path instead of the default | optional
- `700MB`, `2GB`, or plain bytes | optional — useful for very large corpora | | `GRAPHIFY_MAX_CONTEXTS` | Maximum number of non-default project graphs retained by one multi-project M
- `0.7`, or `none` to omit | optional — auto-omitted for o1/o3/o4/gpt-5 reasoning models | --- ## Privacy - **Code files** — processed locally via tree-sitter.
- - **pip** (`pip install graphifyy`): pip installs scripts to a user bin dir that may not be on `PATH` — add `~/Library/Python/3.x/bin` (macOS) or `~/.local/bin` (Linux) to your `PA
- env overrides like `OPENAI_BASE_URL` are silently ignored, so requests hit the default endpoint and fail with a 401 that looks like a bad key.
- **Graph HTML is too large to open in a browser (>5000 nodes)** Skip HTML generation and use the JSON directly: **`graph.json` has conflict markers after two devs commit at once** R
- --- ## Translations The README is available in 32 languages.

## Page blocks (id kind y: text)
b000 header 172: graphify Public Sponsor Notifications Fork12.1k (12.1k) Star
b001 star 192: Star125k (125k)
b002 about 250: About Turn any codebase, with its docs, SQL schemas, configs
b003 files 368: Name Last commit message Last commit date .github docs: add 
b007 text 1925: Read this in other languages
b010 text 2035: Try the graphify platform free for 14 days: app.graphify.com
b011 text 2075: Type /graphify in your AI coding assistant and it maps your 
b012 list 2139: Code maps for free, fully local. Code is parsed with tree-si
b013 quote 2331: Want this always-on, updating in the background across your 
b015 text 2856: The FastAPI codebase mapped by graphify. Every node is a con
b016 text 2920: Get started (30 seconds):
b017 code 2960: uv tool install graphifyy # install the CLI (or: pipx instal
b020 text 3048: Then, in your AI assistant:
b022 code 3088: /graphify .
b024 text 3155: That's it. You get three files:
b026 code 3195: graphify-out/ ├── graph.html open in any browser — click nod
b028 text 3322: The persisted graph includes graph.schema_version so integra
b029 text 3386: Works in Claude Code, Cursor, Codex, Gemini CLI, GitHub Copi
b031 heading 3459: See it in action
b034 text 3872: Once the graph is built you query it instead of reading file
b036 code 3936: $ graphify explain "APIRouter" Node: APIRouter Source: routi
b038 text 4299: Every edge carries a confidence tag (EXTRACTED = explicit in
b040 heading 4444: What it does
b042 text 4498: What you get out of the box:
b043 table 4538: rows 0-7 (0 = header) Capability What you get God nodes The most-connected concept
b045 heading 5004: Benchmarks
b047 table 5058: rows 0-5 (0 = header) Benchmark Metric graphify Field LOCOMO (n=300) recall@10 0.4
b048 text 5297: Every system ran on the same harness with the same model and
b050 heading 5418: Prerequisites
b052 table 5472: rows 0-3 (0 = header) Requirement Minimum Check Install Python 3.10+ python --vers
b053 text 5685: macOS quick install (Homebrew):
b054 code 5725: brew install python@3.12 uv
b057 text 5793: Windows quick install:
b058 code 5833: winget install astral-sh.uv
b062 code 5941: sudo apt install python3.12 python3-pip pipx # or install uv
b066 heading 6081: Install
b068 quote 6136: Official package: The PyPI package is graphifyy (double-y). 
b069 text 6200: The official source repository is Graphify-Labs/graphify.
b070 text 6240: Step 1 — install the package:
b071 code 6280: # Recommended (isolated env; if 'graphify' isn't found after
b074 text 6446: Step 2 — register the skill with your AI assistant:
b075 code 6486: graphify install
b078 text 6554: That's it. Open your AI assistant and type /graphify .
b079 text 6594: To install the assistant skill into the current repository i
b080 code 6634: graphify install --project graphify install --project --plat
b083 text 6721: Project-scoped installs write under the current directory, f
b084 quote 6857: PowerShell note: Use graphify . not /graphify . — the leadin
b085 quote 6921: graphify: command not found? uv tool install / pipx install 
b086 quote 7057: Running with uvx / uv tool run instead of installing? Name t
b087 quote 7169: Avoid pip install on Mac/Windows if possible. The skill reso
b088 quote 7281: Git hooks and uv tool / pipx: graphify hook install embeds t
b089 quote 7393: Strict mode (Claude Code): graphify install --project --stri
b090 text 7529: Pick your platform (20+ assistants, click to expand)
b091 text 7569: Optional extras (install only what you need)
b093 heading 7642: Make your assistant always use the graph
b095 text 7696: Run this once in your project after building a graph:
b096 table 7736: rows 0-22 (0 = header) Platform Command Claude Code graphify claude install CodeBud
b097 text 8604: This writes a small config file that tells your assistant to
b098 list 8692: Hook platforms (Claude Code, Gemini CLI): a hook fires autom
b099 text 8832: GRAPH_REPORT.md is still available for broad architecture re
b100 text 8872: CodeBuddy does the same two things as Claude Code: writes a 
b101 text 8984: Codex writes to AGENTS.md, which is what actually carries th
b102 text 9144: Kilo Code installs the Graphify skill to ~/.config/kilo/skil
b103 text 9280: Cursor writes .cursor/rules/graphify.mdc with alwaysApply: t
b104 text 9344: To remove graphify from all platforms at once: graphify unin
b106 heading 9441: What's in the report
b108 list 9496: God nodes — the most-connected concepts in your project. Eve
b110 heading 9753: What files it handles
b112 table 9807: rows 0-15 (0 = header) Type Extensions Code (37 tree-sitter grammars) .py .ts .mts 
b113 text 10896: Terraform module calls with a literal local source (./... or
b114 text 11032: Remote sources and source expressions are not resolved; .tfv
b115 text 11192: Code is extracted locally with no API calls (AST via tree-si
b116 text 11256: Google Drive for desktop .gdoc, .gsheet, and .gslides files 
b117 code 11344: uv tool install "graphifyy[google]" # needed for Google Shee
b120 text 11451: You can also set GRAPHIFY_GOOGLE_WORKSPACE=1. Graphify expor
b122 heading 11548: Common commands
b124 code 11602: /graphify . # build graph for current folder /graphify ./doc
b127 text 12103: See the full command reference below.
b129 heading 12176: Ignoring files
b131 text 12230: Create a .graphifyignore in your project root — same syntax 
b132 text 12270: .gitignore is respected automatically. graphify reads the .g
b133 text 12406: Pass --no-gitignore to graphify extract when git-ignored gen
b135 code 12470: # .graphifyignore node_modules/ dist/ *.generated.py # only 
b138 heading 12729: Team setup
b140 text 12783: For users building a team graph, the graphify-out/ directory
b141 text 12871: (Note: If you are contributing to the Graphify repository it
b142 text 12935: Recommended git commands to share a graph (you only need to 
b143 code 12999: git add -f graphify-out/graph.json git add -f graphify-out/G
b146 quote 13126: manifest.json is now portable — keys are stored as relative 
b147 text 13190: The remaining graphify-out/ files stay machine-local and sho
b149 heading 13334: Recommended workflow
b151 text 13375: Set this up once per clone. From then on, three of your norm
b152 table 13439: rows 0-5 (0 = header) you do graphify does graphify hook install (once, right afte
b153 text 13726: The commit and branch-switch rebuilds run in the background 
b155 list 13854: Clone the repo and run graphify hook install once. Commit an
b157 heading 14175: Using the graph directly
b159 code 14229: # query the graph from the terminal graphify query "show the
b162 text 14553: The MCP server gives your assistant structured access: query
b164 heading 14625: One-click install (VS Code · Smithery)
b166 text 14666: Prefer not to edit MCP config by hand? Register the graphify
b168 text 14773: The button adds a graphify server that launches with uvx --f
b169 code 14837: # pick your client (claude, cursor, vscode, windsurf, ...) n
b173 heading 14932: Shared HTTP server
b175 text 14973: --transport stdio (the default) spawns one local server per 
b176 table 15085: rows 0-8 (0 = header) Flag Default Purpose --transport {stdio,http} stdio Transpor
b177 text 15555: The default 127.0.0.1 bind is loopback-only. Set --host 0.0.
b178 code 15619: docker build -t graphify . docker run -p 8080:8080 -v "$(pwd
b181 quote 15726: WSL / Linux note: Ubuntu ships python3, not python. Use a ve
b183 heading 15867: Environment variables
b185 text 15922: These are only needed for headless / CI extraction (graphify
b186 table 15986: rows 0-35 (0 = header) Variable Used for When required ANTHROPIC_API_KEY Claude (An
b188 heading 18904: Privacy
b190 list 18958: Code files — processed locally via tree-sitter. Nothing leav
b192 heading 19531: Troubleshooting
b194 text 19585: graphify: command not found after installing The CLI is inst
b195 list 19649: uv (uv tool install graphifyy): the command lands in uv's to
b196 text 19841: uvx graphify … or uv tool run graphify … fails to resolve gr
b197 text 19977: uv run --with graphifyy python -m graphify silently runs an 
b198 code 20161: python -c "import graphify; print(graphify.__file__)"
b201 text 20229: Then run the installed command directly (it uses the uv-mana
b202 code 20269: uvx --from graphifyy graphify extract . --backend openai # n
b205 text 20356: python -m graphify works but graphify command doesn't Your s
b206 text 20444: /graphify . causes "path not recognized" in PowerShell Power
b207 text 20508: Graph has fewer nodes after --update or rebuild If a refacto
b208 text 20572: extract exits with "extraction was incomplete ... refusing t
b209 text 20684: Graph has duplicate nodes for the same entity (ghost duplica
b210 code 20796: graphify extract . --force
b213 text 20864: Ollama runs out of VRAM / context window exceeded The KV-cac
b214 code 20928: GRAPHIFY_OLLAMA_NUM_CTX=8192 graphify extract ./docs --backe
b217 text 20996: LLM returned invalid JSON / Unterminated string warnings The
b218 code 21132: GRAPHIFY_MAX_OUTPUT_TOKENS=16384 graphify extract . --mode d
b221 text 21220: With a cloud gateway like OpenRouter, prefer --backend opena
b222 text 21308: Graph HTML is too large to open in a browser (>5000 nodes) S
b223 code 21372: graphify cluster-only ./my-project --no-viz graphify query "
b226 text 21459: graph.json has conflict markers after two devs commit at onc
b227 text 21523: Graph doesn't reflect a teammate's recent changes Run graphi
b228 code 21635: git config --global alias.gpull '!git pull && graphify updat
b231 text 21703: Confirm the hooks are active with graphify hook status; re-r
b232 text 21767: Extraction returns empty nodes/edges for docs or PDFs Docs, 
b233 code 21831: ANTHROPIC_API_KEY=sk-... graphify extract ./docs --backend c
b236 text 21899: Skill version mismatch warning in your IDE Your installed gr
b237 code 22059: uv tool upgrade graphifyy graphify install --platform <name>
b240 text 22147: Claude Code prompt cache invalidated after every graphify ex
b242 code 22259: # .claudeignore graph.json graphify-out/
b245 heading 22399: Full command reference
b248 code 22453: /graphify # run on current directory /graphify ./raw # run o
b250 text 25456: --no-dedup also skips coalescing distinct non-AST nodes sole
b251 quote 25568: Community names: inside an agent (Claude Code, Gemini CLI) t
b253 heading 25713: Learn more
b255 list 25767: docs.graphify.com — full documentation: guides, command refe
b257 heading 25952: graphify Enterprise
b259 text 26007: graphify Enterprise is the always-on layer built on top of g
b260 text 26095: Built for people and teams whose work lives across hundreds 
b261 text 26159: Join the waitlist at graphify.com. Free trial launching soon
b263 heading 26232: Contributing
b265 text 26286: Contributions are welcome. See CONTRIBUTING.md for the devel
b266 text 26374: New here? Say hi on Discord or in GitHub Discussions.
b268 heading 26447: Contributors
b271 text 27116: Made with contrib.rocks.
b273 heading 27189: Translations
b275 text 27243: The README is available in 32 languages. Use the language sw
b277 heading 27364: Community and links
b280 media 1572: Graphify
b281 media 2419: graphify's interactive graph.html showing the FastAPI codeba
b282 media 3513: graphify path query: a terminal asks for the shortest path b
b283 media 26501: graphify contributors

## Media
m00 block b280 still 1200x630: Graphify
m01 block b281 still 1400x692: graphify's interactive graph.html showing the FastAPI codebase as a force-direct
m02 block b282 still NonexNone: graphify path query: a terminal asks for the shortest path between FastAPI and M
m03 block b283 still NonexNone: graphify contributors