# tt-a1i/archify
Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.
stars 77286 · forks 5208 · JavaScript · licence MIT · release v3.0.1 (2026-09-28) · pushed 2026-10-04 · topics agent-skills, ai-agents, architecture-diagram, claude-code, claude-skills, codex, coding-agents, deepseek-harness
languages {'JavaScript': 89.2, 'CSS': 4.8, 'HTML': 4.5, 'Astro': 1.2, 'Shell': 0.1}

## README by section
### (intro)
Turn anything you want to understand, plan, or share into an interactive visual.
### See Archify in action
https://github.com/user-attachments/assets/78570807-ba1d-4737-953f-55504a378a87 **One sentence.
### Install, then describe your idea
Works with Cursor, Claude Code, Codex CLI, and OpenCode.
```
npx skills add tt-a1i/archify -g
```
```
Use Archify to diagram a web request: Browser calls the API,
the API checks Redis, and a cache miss queries PostgreSQL and fills the cache.
```
### ❤️ Sponsors
**Archify × Kimi Work.** Find Archify in the Kimi Work plugin store as **Interactive Architecture Diagram**.
### Show what matters
The Proof Lab contains all 11 checked-in scenarios, their JSON sources, and validation receipts.
| Explain an agent workflow | Follow a cache miss | Explore service relationships |
| ![Agent workflow tracing everything the planner drives](https://tt-a1i.github.io/archify/gallery/artifacts/agent-tool-call.workf
| Trace everything downstream of one step. | Highlight the path from web app to database. | Focus on authored backend and database
### Understand a real repository
CODE → DIAGRAM · A source-backed system map ![MCO runtime architecture generated from the public mco-org/mco repository](https://tt-a1i.github.io/archify/cases/
### Easy to extend. More ways to make it yours.
COMMUNITY STORIES · Selected examples shared by users **Keep building after the diagram is generated.** Archify is open source and its output is standalone HTML
### Download it. Open it. Explore it.
The output is a self-contained HTML file.
### Community and recognition
- **#1 on GitHub Trending's weekly, all-language repository list.** Ranking screenshot published by the creator on September 1, 2026, with all languages and “Th
### Preview
Themes, exports, and share cards Same diagram, two themes, one click to switch: The Export menu copies PNG to the clipboard and downloads static or motion forma
| Dark | Light |
| | |
### Quick start
**Current stable version:** `v3.0.1`.
### 1. Install
More installation options and update-check details For an explicit, non-interactive Cursor install: To try without installing: DSH community opt-in: `dsh plugin
```
npx skills add tt-a1i/archify -g
```
```
npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
```
### Stay updated
- **Get release notifications:** select **Watch → Custom → Releases** at the top of this GitHub repository.
### 2. Start from a description — no repository required
For source evidence, open a repository and ask:
```
Use Archify to draw: Browser -> API -> Redis cache -> PostgreSQL fallback.
```
```
Analyze this repository, then use archify to create a high-level runtime architecture diagram.
Show 8–12 core components, one primary path, external dependencies, and trust boundaries.
Put supporting detail in cards instead of adding more edges.
```
### 3. Refine in chat
Continue with focused requests such as `add Redis`, `move auth to the left`, or `highlight the rollback path`.
### Choose the right diagram
Five diagram types, architecture comparisons, and examples Architecture's optional `deployment-ownership` profile fails closed when authored owners, region plac
| Type | Best for | Include in your prompt |
| **Architecture** | Components, services, storage, boundaries | Scope, core components, primary path |
| **Workflow** | CI/CD, approvals, tool calls, runbooks | Participants, order, branches, exceptions |
| **Sequence** | API calls, cache fallback, auth, async traces | Callers, callees, returns, timing |
| **Data Flow** | Pipelines, lineage, PII, consumers | Sources, transforms, stores, boundaries |
| **Lifecycle** | States, retries, waits, terminal outcomes | States, events, retry and cancellation paths |
```
node archify/bin/archify.mjs guide "Show an API request with Redis cache miss"
node archify/bin/archify.mjs guide "Map Kafka topics, consumer groups, replay, and DLQ" --json
```
### Why Archify
The engineering behind the experience - **Layout judgment over generic auto-layout** — the agent chooses hierarchy, spacing, routes, and emphasis; shared automa
| Understand the structure | Walk through the story |
| Map components, workflows, and relationships from code or a description. | Explore nodes, follow paths, and share any view as a 
| **Extend it your way** | **Share the result** |
| Keep an editable source and build on the open-source code or generated HTML with your own interactions and use cases. | Share a 
### How it works
Generation, validation, preview, and delivery details Useful repository commands: `preview` is an explicit loopback-only desktop mode: it watches one JSON file 
| Step | What happens |
| **Generate** | The agent creates typed JSON IR from your description. |
| **Validate** | Bundled validators and layout rules check the source; failures identify the exact local repair in machine-readabl
| **Preview (optional)** | A loopback-only desktop session watches one source and reloads only verified revisions; failures keep t
| **Deliver** | A same-directory candidate is rendered and checked; only a passing artifact atomically replaces the target, then o
| **Iterate** | The agent updates the source while unrelated structure stays stable. |
```
cd archify
node bin/archify.mjs doctor
node bin/archify.mjs demo /tmp/archify-demo
node bin/archify.mjs guide "Show CI/CD checks, approval, deploy, and rollback"
...
```
```
{
  "meta": {
    "locale": "en",
    "animation": "trace",
...
```
### Explore and share the output
Stable links can restore `#focus=`, `#focus=&reach=upstream|downstream`, `#relation=`, `#route=~`, and `#lens=~`.
| Action | Control |
| Open the factual Diagram Guide | ? |
| Find and focus a semantic node | / |
| Trace upstream/downstream authored reach | Focus a node → `Upstream` / `Downstream` |
| Probe a directed route and inspect its journey | R or `PATH` |
| Compare one or two semantic roles | L or `LENS` |
|...
### Installation options
| Surface | Install location or method | Capability |
| **Claude Code** | `~/.claude/skills/` or `.claude/skills/` | Full renderer + validation workflow |
| **Codex CLI** | `~/.agents/skills/` or `.agents/skills/` | Full renderer + validation workflow |
| **opencode** | `~/.config/opencode/skills/`, `.opencode/skills/`, or `.agents/skills/` | Full renderer + validation workflow |
| **Claude.ai** | Upload `archify.zip` under Settings → Capabilities → Skills | Depends on Node.js access in the sandbox |
| **Project Knowledge** | Upload `archify.zip` to the project | Prompt-driven architecture fallback |
|...
### Reference and scope
- Schema reference · Skill · Examples · Agent cookbook - Changelog - Roadmap - Generated Proof Lab Automatic Mermaid parsing, general-purpose auto-layout, hoste
### Community
👋 **Welcome to the Archify Community!** Connect with other users and developers, share ideas, request features, report bugs, discuss development, and help make 
### License
MIT — free to use, modify, and distribute.
### Contributing
Issues, pull requests, and real-world diagrams are welcome.
### Support Archify
If Archify has been useful to you, you can support its continued development.
### Star History

## Sentences with numbers (verbatim)
- With fast, reliable service and responsive technical support, OpenLux offers base pricing for Claude, OpenAI, and Gemini models as low as 8.82%, 4%, and 8% of official rates, respe
- ## Preview Themes, exports, and share cards Same diagram, two themes, one click to switch: | Dark | Light | |---|---| | | | The Export menu copies PNG to the clipboard and download
- Successful checks wait about 24 hours (±20%); active use retries failures after 6, then 24 hours.

## Page blocks (id kind y: text)
b000 header 72: tt-a1i / archify Public Notifications Fork 5.2k Star 77.3k C
b001 star 88: Star 77.3k
b025 code 3619: npx skills add tt-a1i/archify -g
b073 list 7443: #1 on GitHub Trending's weekly, all-language repository list
b086 code 7856: npx skills add tt-a1i/archify -g
b093 list 8013: Get release notifications: select Watch → Custom → Releases 
b135 list 10564: Schema reference · Skill · Examples · Agent cookbook Changel
b142 list 10918: Discord WeChat: scan the QR code below. WeChat group codes e
b163 media 1758: Archify
b164 media 1976: Archify — interactive diagrams
b165 media 2954: 
b166 media 4020: Archify × Kimi Work collaboration banner
b167 media 5194: Agent workflow tracing everything the planner drives
b168 media 5199: Cache-miss sequence showing the Web App to Postgres route
b169 media 5189: Production architecture comparing backend and database roles
b170 media 5561: MCO runtime architecture generated from the public mco-org/m
b171 media 6528: A community-created four-day Shanghai CityWalk itinerary
b172 media 7774: Dark theme
b173 media 7773: Light theme
b174 media 8152: Export menu
b175 media 8897: Route Share Card showing the exact Users to API Server path 
b176 media 9424: MCO downstream Reach Share Card showing authored relationshi
b177 media 9235: Architecture Delta showing added, removed, changed, and move
b178 media 9897: Workflow example
b179 media 11000: Sequence example
b180 media 11841: Data Flow example
b181 media 12504: Lifecycle example
b182 media 11073: Archify Official WeChat group QR code
b184 media 11846: WeChat Pay QR code to support the Archify maintainer
b185 media 11886: Alipay QR code to support the Archify maintainer (name redac
b186 media 11964: Star History

## Media
m00 block b163 still NonexNone: Archify
m01 block b164 still 1440x810: Archify — interactive diagrams
m02 block b165 animated 300f@30 1920x1080: 
m03 block b166 still 1916x821: Archify × Kimi Work collaboration banner
m04 block b167 still 1280x720: Agent workflow tracing everything the planner drives
m05 block b168 still 1280x720: Cache-miss sequence showing the Web App to Postgres route
m06 block b169 still 1280x720: Production architecture comparing backend and database roles
m07 block b170 still 1200x630: MCO runtime architecture generated from the public mco-org/mco repository
m08 block b171 still 1680x971: A community-created four-day Shanghai CityWalk itinerary
m09 block b172 still 1400x1100: Dark theme
m10 block b173 still 1400x1100: Light theme
m11 block b174 still 1400x1100: Export menu
m12 block b175 still 1200x630: Route Share Card showing the exact Users to API Server path with the full archit
m13 block b176 still 1200x630: MCO downstream Reach Share Card showing authored relationships from Command Rout
m14 block b177 still 1265x712: Architecture Delta showing added, removed, changed, and moved authored facts
m15 block b178 still 2400x2976: Workflow example
m16 block b179 still 2752x2558: Sequence example
m17 block b180 still 2752x1968: Data Flow example
m18 block b181 still 2752x1888: Lifecycle example
m19 block b182 still 728x728: Archify Official WeChat group QR code
m20 block b183 still 794x794: Archify Official QQ group QR code
m21 block b184 still 1118x1524: WeChat Pay QR code to support the Archify maintainer
m22 block b185 still 1024x1536: Alipay QR code to support the Archify maintainer (name redacted)
m23 block b186 still NonexNone: Star History