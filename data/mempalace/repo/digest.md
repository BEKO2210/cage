# MemPalace/mempalace
The best-benchmarked open-source AI memory system. And it's free.
stars 59486 · forks 7564 · Python · licence MIT · release v3.10.0 (2026-09-16) · pushed 2026-10-09 · topics ai, chromadb, llm, mcp, memory, python
languages {'Python': 94.7, 'Shell': 1.7, 'JavaScript': 0.9, 'HTML': 0.8, 'CSS': 0.6}

## README by section
### (intro)
### MemPalace
Local-first AI memory.
### What it is
MemPalace stores your conversation history as verbatim text and retrieves it with semantic search.
### Install
### Agent-guided setup
Install the MemPalace skills first, then ask your coding agent to set up MemPalace.
```
npx skills add MemPalace/mempalace
```
### Direct CLI setup
MemPalace ships a CLI, so install it in an isolated environment to avoid PEP 668 errors on Debian/Ubuntu/Homebrew Pythons and to keep mempalace's deps (`chromad
```
uv tool install mempalace
mempalace init ~/projects/myapp
```
```
python -m venv .venv && source .venv/bin/activate
pip install mempalace
```
### Android / Termux
Native Termux installation is not currently supported because compiled dependencies such as ChromaDB and ONNX Runtime publish Linux wheels, not Android wheels.
### Docker
A container image is also available for running the MCP server or the CLI without a local Python toolchain.
```
docker pull ghcr.io/mempalace/mempalace:latest
```
```
# MCP server over stdio — note the `-i` flag (JSON-RPC needs stdin)
docker run -i --rm -v mempalace-data:/data ghcr.io/mempalace/mempalace

# Run any CLI command instead. The container only sees what you mount, so
...
```
### Storage backends
ChromaDB is the default and needs no configuration.
| Backend | Mode | Install | Namespaces | Lexical | Configure with |
| `chroma` _(default)_ | Local (embedded) | bundled | – | ✓ | – |
| `sqlite_exact` | Local (exact NumPy) | bundled | – | ✓ | – |
| `rust_exact` | Local (native vectors) | wheel / compiled | – | ✓ | – |
| `milvus` | Local (Lite) · Server opt-in | `mempalace[milvus]` | ✓ | ✓ | `MEMPALACE_MILVUS_URI` |
| `qdrant` | Server (REST) | bundled | ✓ | ✓ | `MEMPALACE_QDRANT_URL` |
|...
### Native vector search
`rust_exact` and the standalone `mempalace-native` CLI scan the same `sqlite_exact` database with a native Rust engine.
### Quickstart
For Claude Code, Gemini CLI, Antigravity, MCP-compatible tools, and local models, see mempalaceofficial.com/guide/getting-started.
```
# Mine content into the palace
mempalace mine ~/projects/myapp                    # project files
mempalace mine ~/.claude/projects/ --mode convos   # Claude Code sessions (scope with --wing per pro

...
```
### Benchmarks
All numbers below are reproducible from this repository with the commands in `benchmarks/BENCHMARKS.md`.
| Mode | R@5 | LLM required |
| Raw (semantic search, no heuristics, no LLM) | **96.6%** | None |
| Hybrid v4, held-out 450q (tuned on 50 dev, not seen during training) | **98.4%** | None |
| Hybrid v4 + LLM rerank (full 500) | ≥99% | Any capable model |
| Benchmark | Metric | Score | Notes |
| LoCoMo (session, top-10, no rerank) | R@10 | 60.3% | 1,986 questions |
|...
```
git clone https://github.com/MemPalace/mempalace.git
cd mempalace
uv sync --extra dev   # or: pip install -e ".[dev]"
# see benchmarks/README.md for dataset download commands
...
```
### Knowledge graph
MemPalace includes a temporal entity-relationship graph with validity windows — add, query, invalidate, timeline — backed by local SQLite.
### MCP server
45 MCP tools cover palace reads/writes, knowledge-graph operations, cross-wing navigation, drawer management, agent diaries, and agent coordination (logstream e
### Agents
Each specialist agent gets its own wing and diary in the palace.
### Auto-save hooks
Auto-save hooks for **Claude Code, Codex CLI, and Cursor IDE** save periodically and before context compression: - Claude Code + Codex → mempalaceofficial.com/g
### Requirements
- Python 3.9+ - A vector-store backend (ChromaDB by default) - ~300 MB disk for the embedding model.
### Docs
- Getting started → mempalaceofficial.com/guide/getting-started - CLI reference → mempalaceofficial.com/reference/cli - Python API → mempalaceofficial.com/refer
### Contributing
PRs welcome.
### License
MIT — see LICENSE.

## Sentences with numbers (verbatim)
- Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.
- > [!IMPORTANT] > **Claude Code sessions expire in 30 days without auto-save hooks wired.** Read this → > > Need the shortest recovery/setup path?
- ### Direct CLI setup MemPalace ships a CLI, so install it in an isolated environment to avoid PEP 668 errors on Debian/Ubuntu/Homebrew Pythons and to keep mempalace's deps (`chroma
- Android ARM64 users can run the regular Linux packages in an isolated Debian PRoot container instead.
- Multi-arch (amd64 + arm64), so it runs natively on Apple Silicon: Everything persists under `/data` — palace, config, and the cached embedding model — so mount a volume there and r
- See `crates/` for the core workspace, PyO3 bindings, and native CLI.
- **LongMemEval — retrieval recall (R@5, 500 questions):** | Mode | R@5 | LLM required | |---|---|---| | Raw (semantic search, no heuristics, no LLM) | **96.6%** | None | | Hybrid v4
- The hybrid pipeline adds keyword boosting, temporal-proximity boosting, and preference-pattern extraction; the held-out 98.4% is the honest generalisable figure.
- The rerank pipeline promotes the best candidate out of the top-20 retrieved sessions using an LLM reader.
- The gap between raw and reranked is model-agnostic; we do not headline a "100%" number because the last 0.6% was reached by inspecting specific wrong answers, which `benchmarks/BEN
- **Other benchmarks (full results in `benchmarks/BENCHMARKS.md`):** | Benchmark | Metric | Score | Notes | |---|---|---|---| | LoCoMo (session, top-10, no rerank) | R@10 | 60.3% | 1
- --- ## Requirements - Python 3.9+ - A vector-store backend (ChromaDB by default) - ~300 MB disk for the embedding model.
- Onboarding (`python -m mempalace.onboarding`) offers `embeddinggemma-300m` (multilingual, 100+ languages, recommended) or `all-MiniLM-L6-v2` (English-only, ~30 MB).

## Page blocks (id kind y: text)
b000 header 172: mempalace Public Notifications Fork7.6k (7.6k) Star59.5k (59
b001 star 192: Star59.5k (59.5k)
b002 about 250: About The best-benchmarked open-source AI memory system. And
b003 files 368: Name Last commit message Last commit date .agents/plugins fi
b005 text 2474: MemPalace Local-first AI memory. Verbatim storage, pluggable
b008 text 2812: Local-first AI memory. Verbatim storage, pluggable backend, 
b010 text 2919: Caution Beware of impostor sites. MemPalace has no other off
b012 text 2959: Beware of impostor sites. MemPalace has no other official we
b013 text 3079: Important Claude Code sessions expire in 30 days without aut
b015 text 3119: Claude Code sessions expire in 30 days without auto-save hoo
b016 text 3159: Need the shortest recovery/setup path? Use the Claude Code r
b018 heading 3240: What it is
b020 text 3294: MemPalace stores your conversation history as verbatim text 
b021 text 3406: The retrieval layer is pluggable. The current default is Chr
b022 text 3494: Nothing leaves your machine unless you opt in.
b023 text 3534: Architecture, concepts, and mining flows: mempalaceofficial.
b025 heading 3607: Install
b028 heading 3669: Agent-guided setup
b030 text 3710: Install the MemPalace skills first, then ask your coding age
b031 code 3798: npx skills add MemPalace/mempalace
b034 text 3866: The repository exposes three skills: mempalace for guided in
b035 text 3978: During guided setup the agent can offer weekly stable-releas
b037 heading 4146: Direct CLI setup
b039 text 4187: MemPalace ships a CLI, so install it in an isolated environm
b040 text 4275: We recommend uv — uv tool install puts the mempalace CLI in 
b041 code 4339: uv tool install mempalace mempalace init ~/projects/myapp
b044 text 4426: pipx works the same way if you prefer it: pipx install mempa
b045 text 4466: Prefer plain pip only inside an activated virtualenv where y
b046 code 4530: python -m venv .venv && source .venv/bin/activate pip instal
b050 heading 4626: Android / Termux
b052 text 4667: Native Termux installation is not currently supported becaus
b054 heading 4787: Docker
b056 text 4828: A container image is also available for running the MCP serv
b057 code 4892: docker pull ghcr.io/mempalace/mempalace:latest
b060 text 4960: Everything persists under /data — palace, config, and the ca
b061 code 5024: # MCP server over stdio — note the `-i` flag (JSON-RPC needs
b064 text 5249: The first command that needs embeddings downloads the model 
b065 text 5337: Wire it into an MCP client (e.g. Claude Code) as a stdio ser
b066 code 5401: { "mcpServers": { "mempalace": { "command": "docker", "args"
b069 text 5705: Use a real absolute path there — ~ and $HOME are not expande
b070 text 5769: Mount permissions on Linux. The image runs as uid 1000 and b
b071 text 5929: docker compose run --rm mcp works too (see docker-compose.ym
b072 code 6017: docker build -t mempalace . # CPU docker build --build-arg E
b075 text 6124: The GPU image is x86_64-only: onnxruntime-gpu publishes no a
b076 text 6212: Note that a build from a clone uses whatever branch you chec
b078 heading 6284: Storage backends
b080 text 6339: ChromaDB is the default and needs no configuration. MemPalac
b081 table 6427: rows 0-6 (0 = header) Backend Mode Install Namespaces Lexical Configure with chrom
b082 text 6895: Select with --backend <name>, MEMPALACE_BACKEND=<name>, or "
b084 heading 7015: Native vector search
b086 text 7056: rust_exact and the standalone mempalace-native CLI scan the 
b088 heading 7224: Quickstart
b090 code 7278: # Mine content into the palace mempalace mine ~/projects/mya
b093 text 7562: For Claude Code, Gemini CLI, Antigravity, MCP-compatible too
b095 heading 7659: Benchmarks
b097 text 7713: All numbers below are reproducible from this repository with
b098 text 7777: LongMemEval — retrieval recall (R@5, 500 questions):
b099 table 7817: rows 0-3 (0 = header) Mode R@5 LLM required Raw (semantic search, no heuristics, n
b100 text 8030: The raw 96.6% requires no API key, no cloud, and no LLM at a
b101 text 8118: The rerank pipeline promotes the best candidate out of the t
b102 text 8254: Other benchmarks (full results in benchmarks/BENCHMARKS.md):
b103 table 8294: rows 0-4 (0 = header) Benchmark Metric Score Notes LoCoMo (session, top-10, no rer
b104 text 8496: We deliberately do not include a side-by-side comparison aga
b105 text 8608: Reproducing every result:
b106 code 8648: git clone https://github.com/MemPalace/mempalace.git cd memp
b110 heading 8828: Knowledge graph
b112 text 8882: MemPalace includes a temporal entity-relationship graph with
b114 heading 8978: MCP server
b116 text 9032: 45 MCP tools cover palace reads/writes, knowledge-graph oper
b118 heading 9128: Agents
b120 text 9182: Each specialist agent gets its own wing and diary in the pal
b122 heading 9254: Auto-save hooks
b124 text 9309: Auto-save hooks for Claude Code, Codex CLI, and Cursor IDE s
b125 list 9373: Claude Code + Codex → mempalaceofficial.com/guide/hooks Curs
b126 text 9465: If you are installing under time pressure, start with the Cl
b127 text 9553: For per-message recall on top of the file-level chunks the h
b129 heading 9674: Requirements
b131 list 9728: Python 3.9+ A vector-store backend (ChromaDB by default) ~30
b132 text 10068: No API key is required for the core benchmark path.
b134 heading 10116: Docs
b136 list 10170: Getting started → mempalaceofficial.com/guide/getting-starte
b138 heading 10358: Contributing
b140 text 10412: PRs welcome. See CONTRIBUTING.md.
b142 heading 10460: License
b145 media 2474: MemPalace

## Media
m00 block b145 still 1024x1024: MemPalace