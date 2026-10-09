# career-ops-hq/career-ops
Open-source AI job search agent and job finder: scan job boards, score each job 1-5 against your CV before you apply, tailor an ATS-friendly resume and cover letter, get interview prep and a job application tracker. It helps you fill in each application; you press Submit. Runs locally in your AI coding CLI (Claude Code, Codex, OpenCode and more).
stars 73887 · forks 13865 · JavaScript · licence MIT · release career-ops-v1.35.0 (2026-10-01) · pushed 2026-10-09 · topics agent-skills, ai-agent, ai-job-search, ats, career, career-ops, careerops, claude-code
languages {'JavaScript': 88.6, 'TypeScript': 6.7, 'Go': 3.2, 'HTML': 0.9, 'Shell': 0.5}

## README by section
### (intro)
The open-source AI job search agent.
### Your turn
Paste one job you were about to apply to tonight.
```
npx @santifer/career-ops init
```
### You don't have to search alone
The silence after you hit send is not about you.
### Sponsors
career-ops is free for candidates, forever.
### What career-ops does for you
Paste a job.
### What career-ops will not do
- **Auto-submit an application.** It drafts the answer to every field; you review and click Submit.
### Features
Everything else it does
| Feature | Description |
| **A-H Evaluation** | Role summary, CV match (with how much each requirement matters for this posting, and whether that weight ca
| **Human-in-the-Loop** | AI evaluates and recommends, you decide and act. The system never submits an application -- you always h
| **ATS PDF Generation** | ATS-readable CVs tailored to each JD from your own experience, in Space Grotesk + DM Sans design |
| **Cover Letter Generator** | Research-backed cover letters with keyword mirroring, four interactive angle prompts (why/problems/
| **Beyond the CV** | Company research (`deep`) surfaces AI strategy, recent moves, engineering culture, and the angle your profil
|...
### Quick Start
**Fastest way, one command:** > 💡 `npx` ships with Node.js: it runs the installer once, > without installing anything globally.
```
npx @santifer/career-ops init
```
```
cd career-ops
claude   # or codex / qwen / opencode / agy / grok — open your AI CLI here
```
### Scanning through an outbound proxy
Node's ordinary `fetch()` may ignore `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` in a proxy-only sandbox.
### Global install
This installs the `career-ops` binary globally so you can run it directly instead of via `npx`.
```
npm i -g @santifer/career-ops
```
### Usage
career-ops uses a shared command router.
```
/career-ops           → Show all available commands
/career-ops {JD}      → AUTO-PIPELINE: evaluate + report + PDF + tracker (paste text or URL)
/career-ops pipeline  → Process pending URLs from inbox (data/pipeline.md)
/career-ops oferta    → Evaluation only, blocks A to H (no auto PDF)
...
```
### How It Works
```
You paste a job URL or description
        │
        ▼
┌──────────────────┐
...
```
### Antigravity CLI Integration
career-ops supports Antigravity CLI natively, the same way it supports Claude Code and OpenCode.
### Native Antigravity CLI
The skill is defined using the open standard in `.agents/skills/career-ops/SKILL.md` and symlinked/referenced for each supported CLI (e.g.
```
# 1. Run in the career-ops directory
cd career-ops
agy

...
```
### Codex Integration
career-ops supports Codex through the same shared router, but the invocation model is different from CLIs that auto-register slash commands.
### Interactive Codex
Slash commands are not guaranteed in Codex.
```
cd career-ops
codex
```
```
Evaluate this JD with career-ops auto-pipeline: https://company.com/jobs/123
Run the career-ops scan mode and summarize new matches.
Run the career-ops pipeline mode for data/pipeline.md.
Run the career-ops pdf mode for the latest evaluated role.
...
```
### One-shot Codex (`codex exec`)
```
codex exec "Evaluate this JD with career-ops auto-pipeline: https://company.com/jobs/123"
codex exec "Run career-ops scan mode in this repo and summarize new matches."
codex exec "Run career-ops pipeline mode for data/pipeline.md."
codex exec "Run career-ops pdf mode for the latest evaluated role."
...
```
### Grok Build CLI Integration
career-ops supports Grok Build CLI natively, the same way it supports Claude Code and OpenCode.
### Native Grok Build CLI
For headless batch workers, use `grok -p "prompt"` (add `--yolo` to auto-approve tool executions).
```
# 1. Run in the career-ops directory
cd career-ops
grok

...
```
### Pi Integration
career-ops supports Pi natively, with no wrapper file to maintain: Pi reads `AGENTS.md` from the repo root as project context and discovers the shared skill at 
### Native Pi
```
# 1. Run in the career-ops directory
cd career-ops
pi

...
```
### One-shot Pi (`pi -p`)
If a Pi build gates project resources behind a trust decision, run `/trust` once inside the repo and restart `pi` so the project skill loads (`/trust` applies t
```
pi -p "Evaluate this JD with career-ops auto-pipeline: https://company.com/jobs/123"
pi -p "Run career-ops scan mode and summarize new matches."
pi -p "Run career-ops tracker mode and summarize the current statuses."
```
### Standalone Gemini API Script (No CLI install needed)
> **Free tier:** Both options work without billing.
```
# 1. Get a free API key at https://aistudio.google.com/apikey
cp .env.example .env
# Edit .env, set GEMINI_API_KEY=your_key_here

...
```
### Pre-configured Portals
The scanner comes with **100+ companies** ready to scan and **35+ search queries** across major job boards.
```
node scan.mjs --verify          # zero-token discovery + Playwright liveness check
```
### Dashboard TUI
The built-in terminal dashboard lets you browse your pipeline visually: Features: 6 filter tabs, 4 sort modes, grouped/flat view, lazy-loaded previews, inline s
```
npm run serve:dashboard   # launch the TUI
npm run build:dashboard   # optional: build the standalone binary
```
### Project Structure
```
career-ops/
├── AGENTS.md                    # Canonical agent instructions (all CLIs)
├── CLAUDE.md                    # Claude Code wrapper (imports AGENTS.md)
├── CODEX.md                     # Codex wrapper (imports AGENTS.md)
...
```
### External Data Directory (Optional)
By default, user-layer data (such as `cv.md`, `portals.yml`, and `data/` / `reports/` / `output/` folders) lives inside the project root folder.
### Tech Stack
- **Agent**: AI coding CLI with shared skills and modes (`AGENTS.md` + CLI wrapper) - **PDF**: Playwright + HTML template - **Cover letters**: HTML template + P
### Also Open Source
- **cv-santiago** -- The portfolio website (santifer.io) with AI chatbot, LLMOps dashboard, and case studies.
### FAQ
**What is career-ops?** career-ops (career-ops.org, also known as **careerops**) is an open-source AI job search that runs locally in your AI coding CLI (Claude
### About the Author
I'm Santiago Fernández de Valderrama Aparicio (santifer), a former founder: I built and sold a business that still runs with my name on it.
### Disclaimer
**career-ops is a local, open-source tool, NOT a hosted service.** By using this software, you acknowledge: 1.
### Contributors
Every person who has shipped code, docs, translations or tests is listed in CONTRIBUTORS.md, including non-code contributions, which the graph above cannot show
### License & Trademark
The code is licensed under MIT.
### Star history
Created and maintained by Santiago Fernández de Valderrama Aparicio (@santifer)
### Let's Connect
![Website](https://santifer.io) ![LinkedIn](https://linkedin.com/in/santifer) ![X](https://x.com/santifer) ![Discord](https://discord.gg/8pRpHETxa4) ![Email](ma

## Sentences with numbers (verbatim)
- | | **Pattern Analysis** | Rejection patterns and per-ATS-channel advance rates (`analyze-patterns.mjs`), lifetime funnel stats (`stats.mjs`), repost detection, a possible sign of 
- | | **Portal Scanner** | 100+ companies pre-configured (Anthropic, OpenAI, ElevenLabs, Retool, n8n...) + custom queries across Ashby, Greenhouse, Lever, Wellfound | | **Funded Comp
- ## Pre-configured Portals The scanner comes with **100+ companies** ready to scan and **35+ search queries** across major job boards.
- Copy `templates/portals.example.yml` to `portals.yml` and add your own: **AI Labs:** Anthropic, OpenAI, Mistral, Cohere, LangChain, Pinecone **Voice AI:** ElevenLabs, PolyAI, Parlo
- ## Dashboard TUI The built-in terminal dashboard lets you browse your pipeline visually: Features: 6 filter tabs, 4 sort modes, grouped/flat view, lazy-loaded previews, inline stat

## Page blocks (id kind y: text)
b000 header 172: career-ops Public Sponsor Notifications Fork13.9k (13.9k) St
b001 star 192: Star73.9k (73.9k)
b002 about 250: About Open-source AI job search agent and job finder: scan j
b003 files 368: Name Last commit message Last commit date .agents/skills/car
b006 text 10589: The open-source AI job search agent.
b007 text 10629: English | Español | Deutsch | Français | Português (Brasil) 
b009 text 10757: Months of sending CVs into silence. So I built the filter I 
b010 text 10821: 740 listings evaluated. 68 applied. 12 interviews. 1 offer. 
b011 text 10885: Paste a job. On your machine, it tells you if it's still ope
b013 text 11491: My own search, partway through, with the UI in Spanish.
b014 text 11531: Companies use AI to filter candidates. I just gave candidate
b015 text 11595: Six months later, I left that job. Now we build career-ops, 
b016 text 11659: Try it on one job ↓ · Read the full story →
b019 text 11774: The people who came after me wrote down how they got hired.
b021 text 11995: Every card is a public issue you can open. Landed yours? Lea
b022 text 12035: ⭐ If career-ops helped you, a star helps the next person fin
b028 heading 12287: Your turn
b030 text 12341: Paste one job you were about to apply to tonight. If it come
b031 code 12405: npx @santifer/career-ops init
b034 text 12473: Open source. Local. In the AI CLI you already use. Free and 
b036 heading 12521: You don't have to search alone
b038 text 12576: The silence after you hit send is not about you. Enough peop
b039 quote 12640: Apply better to fewer. Signal over volume. Evidence over key
b041 text 12755: A few of them, in their own words.
b043 text 12976: Every signature is a commit you can audit. Read them all, or
b045 text 13040: Hiring will not fix itself. The people going through it can,
b048 heading 13187: Sponsors
b050 text 13241: career-ops is free for candidates, forever. These companies 
b052 text 13352: SerpApi · Build a portfolio project with live search data. S
b053 quote 13416: Sponsorship buys clearly labeled visibility, never influence
b055 heading 13512: What career-ops does for you
b057 text 13566: Paste a job. It tells you whether that night is worth it.
b058 list 13606: Still open? It checks that the posting is still live before 
b059 text 13786: The first runs are rough. It does not know you yet. Talk to 
b060 text 13850: On first launch it asks for all that in chat. Nothing to con
b062 heading 13898: What career-ops will not do
b064 list 13952: Auto-submit an application. It drafts the answer to every fi
b065 text 14124: It reformulates your CV; it must never fabricate it. A check
b067 heading 14220: Features
b069 table 14275: rows 0-6 (0 = header) Feature Description A-H Evaluation Role summary, CV match (w
b070 text 15007: Everything else it does
b072 heading 15055: Quick Start
b074 text 15109: Fastest way, one command:
b075 code 15149: npx @santifer/career-ops init
b078 quote 15217: 💡 npx ships with Node.js: it runs the installer once, withou
b079 text 15281: This clones the latest release into ./career-ops and install
b080 code 15321: cd career-ops claude # or codex / qwen / opencode / agy / gr
b083 text 15408: On first launch, career-ops walks you through setup (your CV
b084 text 15472: Prefer to set it up manually? (git clone)
b086 heading 15520: Scanning through an outbound proxy
b088 text 15561: Node's ordinary fetch() may ignore HTTP_PROXY, HTTPS_PROXY a
b089 text 15673: Set this flag only when the configured proxy itself blocks c
b091 heading 15913: Global install
b093 code 15954: npm i -g @santifer/career-ops
b096 text 16022: This installs the career-ops binary globally so you can run 
b097 text 16110: Which one should you use?
b098 list 16150: npx @santifer/career-ops init: best for first use; creates a
b099 quote 16242: The system is designed to be customized by your AI coding CL
b100 text 16330: See docs/SETUP.md for the full setup guide, docs/RUNNING_ON_
b102 heading 16546: Usage
b104 text 16600: career-ops uses a shared command router. In CLIs that regist
b106 code 16640: /career-ops → Show all available commands /career-ops {JD} →
b108 text 17476: Or just paste a job URL or description directly -- career-op
b109 text 17516: In Codex, slash commands are not guaranteed. Use the same mo
b111 heading 17588: How It Works
b114 code 17643: You paste a job URL or description │ ▼ ┌──────────────────┐ 
b117 heading 18034: Antigravity CLI Integration
b119 text 18088: career-ops supports Antigravity CLI natively, the same way i
b120 text 18176: Google has transitioned consumer Gemini CLI access to Antigr
b122 heading 18272: Native Antigravity CLI
b124 code 18313: # 1. Run in the career-ops directory cd career-ops agy # 2. 
b127 text 18558: The skill is defined using the open standard in .agents/skil
b129 heading 18654: Codex Integration
b131 text 18708: career-ops supports Codex through the same shared router, bu
b133 heading 18780: Interactive Codex
b135 code 18821: cd career-ops codex
b138 text 18908: Slash commands are not guaranteed in Codex. If /career-ops i
b140 code 18972: Evaluate this JD with career-ops auto-pipeline: https://comp
b143 heading 19127: One-shot Codex (codex exec)
b145 code 19168: codex exec "Evaluate this JD with career-ops auto-pipeline: 
b149 heading 19322: Grok Build CLI Integration
b151 text 19377: career-ops supports Grok Build CLI natively, the same way it
b153 heading 19473: Native Grok Build CLI
b155 code 19514: # 1. Run in the career-ops directory cd career-ops grok # 2.
b158 text 19759: For headless batch workers, use grok -p "prompt" (add --yolo
b160 heading 19807: Pi Integration
b162 text 19861: career-ops supports Pi natively, with no wrapper file to mai
b164 heading 19957: Native Pi
b166 code 19998: # 1. Run in the career-ops directory cd career-ops pi # 2. U
b170 heading 20251: One-shot Pi (pi -p)
b172 code 20292: pi -p "Evaluate this JD with career-ops auto-pipeline: https
b175 text 20399: If a Pi build gates project resources behind a trust decisio
b177 heading 20495: Standalone Gemini API Script (No CLI install needed)
b179 code 20536: # 1. Get a free API key at https://aistudio.google.com/apike
b182 quote 20820: Free tier: Both options work without billing. Native CLI use
b184 heading 20916: Pre-configured Portals
b186 text 20971: The scanner comes with 100+ companies ready to scan and 35+ 
b187 text 21035: AI Labs: Anthropic, OpenAI, Mistral, Cohere, LangChain, Pine
b188 text 21171: Job boards searched: 55+ provider modules cover ATS APIs, bo
b189 text 21235: By default node scan.mjs (a.k.a. npm run scan) trusts what e
b190 code 21347: node scan.mjs --verify # zero-token discovery + Playwright l
b193 text 21415: The verification is sequential and only runs against new off
b195 heading 21463: Dashboard TUI
b197 text 21517: The built-in terminal dashboard lets you browse your pipelin
b198 code 21557: npm run serve:dashboard # launch the TUI npm run build:dashb
b201 text 21644: Features: 6 filter tabs, 4 sort modes, grouped/flat view, la
b202 text 21684: There is also an experimental web UI (alpha and opt-in: noth
b204 heading 21756: Project Structure
b207 code 21810: career-ops/ ├── AGENTS.md # Canonical agent instructions (al
b210 heading 22517: External Data Directory (Optional)
b212 text 22571: By default, user-layer data (such as cv.md, portals.yml, and
b213 text 22635: To separate your personal data from the code (making it easi
b214 list 22699: Environment Variables: Set the CAREER_OPS_ROOT or CAREER_OPS
b215 text 22883: Once resolved, all user files are resolved and written relat
b216 list 22947: Tracker Override: You can also set CAREER_OPS_TRACKER to ove
b217 text 23391: The Go dashboard TUI, Node.js scripts, and AI agent modes al
b219 heading 23463: Tech Stack
b222 list 23560: Agent: AI coding CLI with shared skills and modes (AGENTS.md
b225 text 23842: Also runs on any agent-skill-standard CLI. See Supported CLI
b227 heading 23944: Also Open Source
b229 list 23998: cv-santiago -- The portfolio website (santifer.io) with AI c
b231 heading 24070: FAQ
b233 text 24124: What is career-ops? career-ops (career-ops.org, also known a
b234 text 24260: Can the tailored CV invent things? It must not, and the prom
b235 text 24396: Can I run career-ops for free, or on a cheaper / local model
b236 text 24484: I pay for Claude Pro/Max but career-ops is burning API credi
b237 text 24644: Which AI CLIs does career-ops work with? career-ops runs on 
b238 text 24732: How do I install career-ops on Windows? career-ops runs on W
b239 text 24844: Does career-ops auto-apply to jobs for me? No. career-ops is
b240 text 24932: Is career-ops free and open source? Yes. career-ops is free 
b242 heading 25028: About the Author
b244 text 25083: I'm Santiago Fernández de Valderrama Aparicio (santifer), a 
b245 text 25195: Curious how a repo this size is maintained with a fleet of A
b246 text 25259: My portfolio and other open source projects → santifer.io
b247 text 25299: Wikidata: Santiago Fernández de Valderrama Aparicio · career
b249 heading 25347: Disclaimer
b251 text 25401: career-ops is a local, open-source tool, NOT a hosted servic
b252 list 25465: You control your data. Your CV, contact info, and personal d
b253 text 25781: See LEGAL_DISCLAIMER.md for full details. This software is p
b255 heading 25853: Contributors
b258 text 26522: Every person who has shipped code, docs, translations or tes
b259 text 26586: Got hired using career-ops? Share your story!
b261 heading 26634: License & Trademark
b263 text 26688: The code is licensed under MIT. The "career-ops" name and br
b265 heading 26760: Star history
b268 text 27257: Created and maintained by Santiago Fernández de Valderrama A
b270 heading 27305: Let's Connect
b273 media 10949: The author's own search in the career-ops dashboard: scored 
b274 media 11814: Hired stories you can open and read
b275 media 12795: Three signatures of the CareerOps manifesto, in their own wo
b276 media 25907: 
b277 media 26814: Live star telemetry of career-ops-hq/career-ops

## Media
m00 block b273 animated 150f@10.0 800x519: The author's own search in the career-ops dashboard: scored listings, a red coun
m01 block b274 still NonexNone: Hired stories you can open and read
m02 block b275 still NonexNone: Three signatures of the CareerOps manifesto, in their own words
m03 block b276 still NonexNone: 
m04 block b277 still NonexNone: Live star telemetry of career-ops-hq/career-ops