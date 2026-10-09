# androoAGI/starnet
A living pixel-art station where real AI agents do real work. Local-first desktop agent harness - bring your own key, watch your crew actually run.
stars 1080 · forks 193 · JavaScript · licence MIT · release v0.13.1 (2026-10-04) · pushed 2026-10-04 · topics agent-harness, ai, ai-agents, byok, desktop-app, game-ui, llm, local-first
languages {'JavaScript': 92.0, 'CSS': 5.0, 'HTML': 2.0, 'Rust': 0.6, 'Python': 0.2}

## README by section
### (intro)
**A living pixel-art station where real AI agents do real work.** ![Download](https://github.com/androoAGI/starnet-releases/releases/latest) ![Platforms](INSTAL
### Features
| **A crew, not a chatbot** | Create agents with distinct classes, personas, and loadouts. Run several at once — each gets its own
| **Bring your own models** | Paste an OpenRouter key, or sign in with supported provider accounts (Anthropic, OpenAI, Google) — k
| **Message it from anywhere** | Wire agents to Telegram, Discord, Slack, Signal, or Matrix and talk to your station away from the
| **Night Shift** | Leave the station running and agents keep working inside an explicit, adjustable leash — every away-action is 
| **Recipes, skills, schedules** | Launch proven multi-step recipes, grant reusable skills, and put work on cron schedules with vi
| **Asks before it guesses** | Task Briefs turn ambiguity into one concrete question with options — over any connected channel — i
|...
### What is real
- Model calls stream through the local Node sidecar.
### Download
Desktop builds are published on the StarNet releases page.
| Platform | Asset |
| **Windows** (10/11, 64-bit) | `StarNet__x64-setup.exe` |
| **macOS — Apple Silicon** (M1–M4) | `StarNet__aarch64.dmg` |
| **macOS — Intel** | `StarNet__x64.dmg` |
### Run from source
Requirements: Node.js 18+ (Node.js 22 matches CI), Git.
```
git clone https://github.com/androoAGI/starnet.git
cd starnet
node sidecar/index.js
```
### Run free with a local model
No key, no account, no bill: install Ollama, pull a model (`ollama pull qwen3:8b`), and pick **OLLAMA** as the provider — on the first-run brain screen, or late
```
npm ci
npm run desktop:dev     # dev shell
npm run desktop:build   # build installers locally
```
### Coming from OpenClaw or Hermes?
StarNet can import an existing agent: point it at your on-disk OpenClaw or Hermes home and it mints a StarNet agent from the persona, instructions, memory, and 
### Architecture
The frontend consumes real sidecar events over localhost HTTP/NDJSON and SSE.
| Path | Responsibility |
| `frontend/` | Vanilla JavaScript station world and desktop UI. |
| `sidecar/` | Local Node agent runtime: providers, tools, persistence, budgets, consent. |
| `shared/` | Additive cross-boundary event and schema contracts. |
| `src-tauri/` | Rust/Tauri desktop shell and bundled runtime. |
| `test/` | Unit, contract, integration, and release gates. |
|...
### Testing
The release aggregate is `npm run qa:ready`.
```
npm run test:fast          # required merge gate
npm run test:http          # live sidecar HTTP/E2E suite
npm test                   # validation + world + fast + HTTP suites
npm run security:secrets   # full-history secret scan; requires Gitleaks in PATH
```
### Contributing and security
Contributions are welcome — read CONTRIBUTING.md and follow the Code of Conduct.
### License
StarNet is open source under the MIT License.

## Sentences with numbers (verbatim)
- Honest caveat: local models are smaller than the cloud ones, so expect slower and rougher work on long tasks, and a task needs a large context window — an 8B model takes about 10 G

## Page blocks (id kind y: text)
b000 header 72: androoAGI / starnet Public Notifications Fork 193 Star 1.1k 
b001 star 88: Star 1.1k
b019 list 3655: Model calls stream through the local Node sidecar. Tools ope
b034 code 4593: git clone https://github.com/androoAGI/starnet.git cd starne
b043 code 5061: npm ci npm run desktop:dev # dev shell npm run desktop:build
b059 code 5847: npm run test:fast # required merge gate npm run test:http # 
b074 media 1758: StarNet
b075 media 2005: The StarNet station — rooms, crew, and workstations rendered

## Media
m00 block b074 still 1457x305: StarNet
m01 block b075 still 658x798: The StarNet station — rooms, crew, and workstations rendered from live harness s