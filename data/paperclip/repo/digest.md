# paperclipai/paperclip
The open-source app everyone uses to manage agents at work
stars 99088 · forks 16722 · TypeScript · licence MIT · release v2026.1005.0 (2026-10-06) · pushed 2026-10-09 · topics 
languages {'TypeScript': 93.1, 'Rust': 2.9, 'JavaScript': 2.6, 'PLpgSQL': 0.5, 'Shell': 0.4}

## README by section
### (intro)
Quickstart &middot; Docs &middot; GitHub &middot; Discord &middot; Twitter &middot; Website Sign up for the Paperclip Cloud waitlist →
### Paperclip is the app people use to manage AI agents for work.
Open-source orchestration for teams of AI agents.
| | Step | Example |
| **01** | Define the goal | _"Build the #1 AI note-taking app to $1M MRR."_ |
| **02** | Hire the team | CEO, CTO, engineers, designers, marketers — any bot, any provider. |
| **03** | Approve and run | Review strategy. Set budgets. Hit go. Monitor from the dashboard. |
### Paperclip is right for you if
- ✅ You want to build **autonomous AI organizations** - ✅ You **coordinate many different agents** (OpenClaw, Codex, Claude, Cursor) toward a common goal - ✅ Yo
### The four pillars
Four things have to work for an organization of AI agents to actually produce: the tasks, the org, the training, and the infrastructure.
| Pillar | Built for | What it covers |
| **Agentic Task Manager** — Declare intent. Agents work. You verify the output. | Everyone, daily | Tasks, approvals & review gat
| **Org Chart for Agents** — Roles, permissions & boundaries for humans and agents. | Managers | Mixed human + agent org chart · r
| **Agent Employee Training** — Design, train & evaluate your AI employees. | Enablers | Skill Studio & shared org-wide skills · e
| **Agentic OS** — The infrastructure that makes the work run. | IT & platform | Cross-provider runtime: any model, any agent · sa
### Features
🔌 Bring Your Own Agent Any agent, any runtime, one org chart.
### Problems Paperclip solves
| Without Paperclip | With Paperclip |
| ❌ You have 20 Claude Code tabs open and can't track which one does what. On reboot you lose everything. | ✅ Tasks are ticket-bas
| ❌ You manually gather context from several places to remind your bot what you're actually doing. | ✅ Context flows from the task
| ❌ Folders of agent configs are disorganized and you're re-inventing task management, communication, and coordination between age
| ❌ Runaway loops waste hundreds of dollars of tokens and max your quota before you even know what happened. | ✅ Spend tracking, b
| ❌ You have recurring jobs (customer support, social, reports) and have to remember to manually kick them off. | ✅ Routines creat
|...
### Why Paperclip is special
Paperclip handles the hard orchestration details correctly.
| **Atomic task checkout.** | A single assignee and execution locks prevent competing runs from claiming the same task. |
| **Persistent work context.** | Tasks, comments, and documents stay in Paperclip. Supporting adapters resume saved sessions acros
| **Runtime skill injection.** | Agents can learn Paperclip workflows and project context at runtime, without retraining. |
| **Governance with rollback.** | Approval gates are enforced, config changes are revisioned, and bad changes can be rolled back s
| **Accountable connections.** | Human access, agent eligibility, and gateway action permissions are separate controls. Approve a 
| **Goal-aware execution.** | Linked tasks and projects carry goal ancestry so agents see the "why," not just a title. |
|...
### What's Under the Hood
Paperclip is a full control plane, not a wrapper.
```
┌──────────────────────────────────────────────────────────────┐
│                       PAPERCLIP SERVER                       │
│                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  │
...
```
### The Systems
**Identity & Access** — Two deployment modes (trusted local or authenticated), human roles and permissions, agent API keys, short-lived run JWTs, company member
### What Paperclip is not
| **Not just a chatbot.** | Conversations stay attached to tasks, plans, decisions, and outputs. Experimental Agent Chat can hand 
| **Not an agent framework.** | We don't tell you how to build agents. We tell you how to run a company made of them. |
| **Not just a workflow builder.** | Routines and experimental pipelines operate within an organization, with roles, goals, budget
| **Not a prompt manager.** | Agents bring their own prompts, models, and runtimes. Paperclip manages the organization they work i
| **Not limited to one agent.** | Start with one agent and grow into a team with shared skills, delegation, and review. |
| **Not only for code review.** | Coding and PR review fit alongside research, operations, content, and other work. |
### Quickstart
Open source.
### Just ask your agent to install Paperclip
Share the installation guide with your agent.
### Or install it yourself
With **Node.js 24.11 or newer** installed: The CLI runs from npm's cache; your instance configuration and data persist locally.
```
npx paperclipai@latest onboard --yes
```
```
ANTHROPIC_API_KEY=... npx paperclipai test-drive
OPENAI_API_KEY=... npx paperclipai test-drive --harness codex
OPENROUTER_API_KEY=... npx paperclipai test-drive \
  --harness opencode \
...
```
### FAQ
**Q: Is this project maintained or just slop?** **A:** Paperclip is maintained by the Paperclip team.
### Development
`pnpm test` does not run Playwright.
```
pnpm dev              # Full dev (API + UI, watch mode)
pnpm dev:once         # Full dev without file watching
pnpm dev:server       # Server only
pnpm dev:mobile       # Serve prebuilt UI on :3101 for phones/tablets (proxies /api → :3100)
...
```
### Roadmap
- ✅ Plugin system (e.g.
### Community & Plugins
Find Plugins and more at awesome-paperclip
### Observability
Paperclip ships with opt-in OpenTelemetry auto-instrumentation for the server (traces only).
### Telemetry
Paperclip collects anonymous usage telemetry to help us understand how the product is used and improve it.
| Method | How |
| Environment variable | `PAPERCLIP_TELEMETRY_DISABLED=1` |
| Standard convention | `DO_NOT_TRACK=1` |
| CI environments | Automatically disabled when `CI=true` |
| Config file | Set `telemetry.enabled: false` in your Paperclip config |
### Contributing
We welcome contributions.
### Community
- Discord — Join the community - Twitter / X — Follow updates and announcements - GitHub Issues — bugs and feature requests - GitHub Discussions — ideas and RFC
### License
MIT &copy; 2026 Paperclip Labs, Inc
### Star History
--- Open source under MIT.

## Sentences with numbers (verbatim)
- **Manage business goals, not pull requests.** | | Step | Example | | ------ | --------------- | ------------------------------------------------------------------ | | **01** | Defi
- ## Paperclip is right for you if - ✅ You want to build **autonomous AI organizations** - ✅ You **coordinate many different agents** (OpenClaw, Codex, Claude, Cursor) toward a commo
- We've merged over 2,700 pull requests.

## Page blocks (id kind y: text)
b000 header 172: paperclip Public Notifications Fork16.7k (16.7k) Star99.1k (
b001 star 192: Star99.1k (99.1k)
b002 about 250: About The open-source app everyone uses to manage agents at 
b003 files 368: Name Last commit message Last commit date .agents/skills doc
b006 text 3015: Quickstart · Docs · GitHub · Discord · Twitter · Website
b012 text 3790: Sign up for the Paperclip Cloud waitlist →
b015 heading 3878: Paperclip is the app people use to manage AI agents for work
b017 text 3985: Open-source orchestration for teams of AI agents.
b018 text 4025: If OpenClaw is an employee, Paperclip is the company.
b019 text 4065: Paperclip is a Node.js server and React UI that orchestrates
b020 text 4153: It looks like a task manager. Under the hood: org charts, bu
b021 text 4217: Manage business goals, not pull requests.
b022 table 4257: rows 0-3 (0 = header) Step Example 01 Define the goal "Build the #1 AI note-taking
b024 text 4446: Works with OpenClaw Claude Code Codex Cursor + Cloud Gemini 
b025 table 4446: rows 0-1 (0 = header) Works with OpenClaw Claude Code Codex Cursor + Cloud Gemini 
b026 text 4663: If it can receive a heartbeat, it's hired.
b027 text 4703: Custom processes, HTTP endpoints, and external adapter packa
b030 heading 4815: Paperclip is right for you if
b032 list 4869: ✅ You want to build autonomous AI organizations ✅ You coordi
b035 heading 5197: The four pillars
b037 text 5251: Four things have to work for an organization of AI agents to
b039 table 5793: rows 0-4 (0 = header) Pillar Built for What it covers Agentic Task Manager — Decla
b042 heading 6355: Features
b044 table 6410: rows 0-4 (0 = header) 🔌 Bring Your Own Agent Any agent, any runtime, one org chart
b045 text 7443: Experimental Agent Chat and chat/email connectors add conver
b048 heading 7579: Problems Paperclip solves
b050 table 7633: rows 0-6 (0 = header) Without Paperclip With Paperclip ❌ You have 20 Claude Code t
b053 heading 8269: Why Paperclip is special
b055 text 8323: Paperclip handles the hard orchestration details correctly.
b056 table 8363: rows 0-8 (0 = header) Atomic task checkout. A single assignee and execution locks 
b059 heading 8929: What's Under the Hood
b061 text 8983: Paperclip is a full control plane, not a wrapper. Before you
b063 code 9047: ┌───────────────────────────────────────────────────────────
b066 heading 9556: The Systems
b068 table 9597: rows 0-5 (0 = header) Identity & Access — Two deployment modes (trusted local or a
b071 heading 10772: What Paperclip is not
b073 table 10826: rows 0-6 (0 = header) Not just a chatbot. Conversations stay attached to tasks, pl
b076 heading 11270: Quickstart
b078 text 11325: Open source. Self-hosted. No Paperclip account required. Fol
b080 heading 11397: Just ask your agent to install Paperclip
b082 text 11438: Share the installation guide with your agent.
b084 heading 11486: Or install it yourself
b086 text 11527: With Node.js 24.11 or newer installed:
b087 code 11567: npx paperclipai@latest onboard --yes
b090 text 11635: The CLI runs from npm's cache; your instance configuration a
b091 text 11675: See the installation guide for managed installs, pinned vers
b092 text 11739: For an isolated manual test instance that is already initial
b093 code 11827: ANTHROPIC_API_KEY=... npx paperclipai test-drive OPENAI_API_
b096 text 11973: Each run without --data-dir gets a unique, retained temporar
b097 quote 12085: Troubleshooting: private npm registry .npmrc If this fails w
b098 text 12429: That quickstart path now defaults to trusted local loopback 
b099 code 12493: npx paperclipai@latest onboard --yes --bind lan # or: npx pa
b102 text 12600: If you already have Paperclip configured, rerunning onboard 
b104 code 12704: git clone https://github.com/paperclipai/paperclip.git cd pa
b107 text 12831: This starts the UI and API at http://localhost:3100. An embe
b108 quote 12895: Requirements: Node.js 24.11+, pnpm 9.15+
b109 text 12935: Local Claude and Codex subscription sign-in also needs Pytho
b110 text 12999: Source development also builds the native Paperclip Runner w
b113 heading 13111: FAQ
b115 text 13165: Q: Is this project maintained or just slop?
b116 text 13205: A: Paperclip is maintained by the Paperclip team. We've merg
b118 text 13269: Q: What does a typical setup look like?
b119 text 13309: A: Locally, a single Node.js process manages an embedded Pos
b120 text 13397: For remote access, use authenticated mode with a private-net
b122 text 13485: Q: Can I run multiple companies?
b123 text 13525: A: Yes. A single deployment can host multiple organizations 
b125 text 13613: Q: How is Paperclip different from agents like OpenClaw or C
b126 text 13653: A: Paperclip uses those agents. It orchestrates them into a 
b128 text 13741: Q: Why should I use Paperclip instead of just pointing my Op
b129 text 13781: A: Agent orchestration has subtleties in how you coordinate 
b130 text 13845: (Bring-your-own-ticket-system is on the Roadmap)
b132 text 13909: Q: Do agents run continuously?
b133 text 13949: A: Agents wake for assigned work and follow-up messages. Opt
b136 heading 14109: Development
b138 code 14163: pnpm dev # Full dev (API + UI, watch mode) pnpm dev:once # F
b141 text 14448: pnpm test does not run Playwright. Browser suites stay separ
b142 text 14512: See doc/DEVELOPING.md for the full development guide.
b145 heading 14600: Roadmap
b147 list 14654: ✅ Plugin system (e.g. add a knowledge base, custom tracing, 
b148 text 15618: This is the short roadmap preview. See the full roadmap in R
b151 heading 15706: Community & Plugins
b153 text 15760: Find Plugins and more at awesome-paperclip
b155 heading 15808: Observability
b157 text 15862: Paperclip ships with opt-in OpenTelemetry auto-instrumentati
b158 text 15998: Paperclip also ships with opt-in Sentry error monitoring for
b160 heading 16190: Telemetry
b162 text 16245: Paperclip collects anonymous usage telemetry to help us unde
b163 text 16333: Contributors changing emitted telemetry events should follow
b164 text 16397: Telemetry is enabled by default and can be disabled with any
b165 table 16437: rows 0-4 (0 = header) Method How Environment variable PAPERCLIP_TELEMETRY_DISABLED
b167 heading 16647: Contributing
b169 text 16701: We welcome contributions. See the contributing guide for det
b173 heading 16829: Community
b175 list 16883: Discord — Join the community Twitter / X — Follow updates an
b178 heading 17055: License
b180 text 17109: MIT © 2026 Paperclip Labs, Inc
b182 heading 17157: Star History
b186 text 17801: Open source under MIT. Built for people who want to get work
b187 media 2474: Paperclip is the app people use to manage AI agents for work
b188 media 3250: 
b189 media 5315: The four pillars of Paperclip
b190 media 17211: Star History Chart

## Media
m00 block b187 still 1600x1150: Paperclip is the app people use to manage AI agents for work.
m01 block b188 animated 300f@30 1280x800: 
m02 block b189 still 3840x2160: The four pillars of Paperclip
m03 block b190 still NonexNone: Star History Chart