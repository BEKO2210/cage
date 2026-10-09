# tashfeenahmed/freellmapi
7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any custom OpenAI-compatible endpoint. Smart routing, automatic failover, encrypted keys. Personal experimentation only.
stars 32391 · forks 4495 · TypeScript · licence MIT · release v0.13.6 (2026-10-07) · pushed 2026-10-09 · topics 
languages {'TypeScript': 98.8, 'JavaScript': 0.7, 'HTML': 0.2, 'CSS': 0.1, 'Shell': 0.1}

## README by section
### (intro)
### FreeLLMAPI
**7.4 billion tokens per month.
### Contents
- Why this exists - Supported providers - Compatible CLIs & coding agents - How it compares - Features - Quick start - Desktop app - Works with OpenAI-compatibl
### Why this exists
Every serious AI lab now offers a free tier, a few million tokens a month, a few thousand requests a day.
### Supported providers
Google Groq Cerebras OpenCode Zen Mistral OpenRouter Cloudflare Cohere Z.ai (Zhipu) NVIDIA HuggingFace ModelScopeQwen3 · DeepSeek V4 · GLM-5 (needs Aliyun cn bi
### Compatible CLIs & coding agents
Claude Code Codex CLI Gemini CLI Cursor Cline Roo Code OpenCode Aider … plus Continue, Goose, Qwen Code, Kilo Code, Crush, Zed, JetBrains AI, DeepSeek Harness, 
```
npx freellmapi setup-claude --url http://localhost:3001 --api-key <unified-key>
```
### How it compares
Based on public documentation, July 2026 — corrections welcome.
### Features
- **Every OpenAI-style surface** — `/v1/chat/completions`, `/v1/responses` (what Codex CLI needs), `/v1/completions` (editor ghost-text autocomplete), `/v1/imag
### Quick start
**One-liner** (Docker required — sets up `~/freellmapi`, generates an encryption key, pulls the image, and starts the container): Prefer to read before you pipe
```
curl -fsSL https://freellmapi.co/install.sh | bash
```
### Desktop app
A native menu-bar app lives in `desktop/`: the entire router + dashboard running locally from your tray, with a glass popover showing live request stats.
### Works with OpenAI-compatible clients
Anything that can target an OpenAI-compatible base URL works: set it to `http://localhost:3001/v1` with the unified key from the dashboard.
### Languages
The dashboard ships in **60 languages** (the desktop tray menu in 6).
### Premium (live catalog)
The router keeps its model catalog fresh on its own: it pulls a signed catalog from freellmapi.co twice a day and applies new models, quota changes, and provide
### Using the API
Streaming, the `auto:*` routing strategies, tool calling, vision input, Gemini Google Search grounding, embeddings, and the Anthropic Messages surface — with cu
```
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:3001/v1",
...
```
### Screenshots
### Models
Pick a routing strategy and watch the monthly token budget fill across the whole provider fleet.
### Keys
Manage provider credentials and grab the unified API key your apps connect with.
### Playground
Send a chat completion through the router and see which provider served it, with the model ID and latency printed right on the message.
### Analytics
Request volume, success rate, tokens in and out, average latency, and per-provider breakdowns over 24h / 7d / 30d / 90d windows.
### How it works
One request in, the best free model out: the router picks the highest-priority model with a healthy key that's under all its rate limits, decrypts the key in me
### FAQ
**Do I need a password?** Not for the desktop app — the dashboard signs itself in with a hidden local account, so there is nothing to set up and nothing to forg
### Limitations
Stacking free tiers has real trade-offs: no frontier models, variable latency, no SLA — and the effective intelligence of the endpoint dips late in the day as t
### Contributing
Contributors very welcome!
### Contributors
### Disclaimer
**This project is for personal experimentation and learning, not production.** Free tiers exist so developers can prototype against them; they aren't a stable, 
### License
MIT

## Sentences with numbers (verbatim)
- # FreeLLMAPI **7.4 billion tokens per month.
- ![CI](https://github.com/tashfeenahmed/freellmapi/actions/workflows/ci.yml) ![GitHub stars](https://github.com/tashfeenahmed/freellmapi/stargazers) ![License: MIT](./LICENSE) ![PRs
- Free installs get the monthly snapshot, so a model reaches them 30 days after it joins the live feed; premium routers get it the same day.
- Stacked together, they add up to roughly **7.4 billion tokens per month** of working inference capacity, across **474 model families / 635 provider endpoints** from small-and-fast 
- Free installs track the monthly snapshot, which each model joins 30 days after it lands in the live feed; premium routers get it same-day.
- Premium → - **Sticky sessions & context handoff** — conversations stay on one model for 30 minutes; an optional compact handoff note keeps the thread coherent when a mid-chat switc
- - **Admin dashboard & analytics** — React UI to manage keys, reorder the chain, run a playground, and read p50/p95/TTFT analytics over 24h–90d windows; login-gated, dark/light them
- Install & deploy → - **Runs anywhere Node 20+ runs** — Windows, macOS, Linux servers, or a small ARM SBC (Raspberry Pi included).
- ~40 MB RSS at idle behind PM2 / systemd / whatever supervisor you prefer.
- ## Languages The dashboard ships in **60 languages** (the desktop tray menu in 6).
- The catalog currently tracks **34 providers**, **474 model families**, **635 free provider/model endpoints** (584 chat, 41 embeddings, 7 transcription, 3 video), and roughly **7.4 
- Free installs pull the same signed catalog, but from the monthly snapshot: a model joins it 30 days after it lands in the live feed, so the free build currently sits about 303 mode
- The code lasts 15 minutes.

## Page blocks (id kind y: text)
b000 header 172: freellmapi Public Notifications Fork4.5k (4.5k) Star32.4k (3
b001 star 192: Star32.4k (32.4k)
b002 about 250: About 7.4 billion tokens per month. 34 free LLM providers. 6
b003 files 368: Name Last commit message Last commit date .claude feat(contr
b005 text 1719: FreeLLMAPI 7.4 billion tokens per month. 34 free LLM provide
b007 text 1786: 7.4 billion tokens per month. 34 free LLM providers. 635 fre
b008 text 1850: Aggregate free tiers from dozens of providers, plus custom O
b010 text 2005: freellmapi.co · browse the full catalog: 474 model families,
b014 text 2663: Your router updates its own model catalog from a signed feed
b016 heading 2808: Contents
b018 list 2862: Why this exists Supported providers Compatible CLIs & coding
b019 text 3350: Guides: Install & deploy · API reference · Clients & coding 
b021 heading 3422: Why this exists
b023 text 3476: Every serious AI lab now offers a free tier, a few million t
b024 text 3588: The problem is that stacking them by hand is painful: thirty
b025 text 3700: And the free-tier landscape shifts weekly: providers launch 
b028 heading 4274: Supported providers
b030 text 4328: Google Groq Cerebras OpenCode Zen Mistral OpenRouter Cloudfl
b031 table 4328: rows 0-3 (0 = header) Google Groq Cerebras OpenCode Zen Mistral OpenRouter Cloudfl
b032 text 4790: … and 22 more free providers
b033 text 4830: Plus a custom provider — point chat, embedding, image, or au
b034 text 4894: The full, always-current list lives at freellmapi.co/models 
b036 heading 4966: Compatible CLIs & coding agents
b038 text 5020: Claude Code Codex CLI Gemini CLI Cursor Cline Roo Code OpenC
b039 table 5020: rows 0-1 (0 = header) Claude Code Codex CLI Gemini CLI Cursor Cline Roo Code OpenC
b040 text 5213: … plus Continue, Goose, Qwen Code, Kilo Code, Crush, Zed, Je
b041 text 5301: Most agents configure themselves with one command that reads
b042 code 5365: npx freellmapi setup-claude --url http://localhost:3001 --ap
b045 text 5433: All supported agents and their setup commands → · Per-tool r
b047 heading 5505: How it compares
b050 text 6177: Based on public documentation, July 2026 — corrections welco
b052 heading 6225: Features
b055 list 6740: Every OpenAI-style surface — /v1/chat/completions, /v1/respo
b056 text 8092: The scope is deliberately narrow — see what's not supported 
b058 heading 8140: Quick start
b060 text 8195: One-liner (Docker required — sets up ~/freellmapi, generates
b061 code 8259: curl -fsSL https://freellmapi.co/install.sh | bash
b064 text 8327: Prefer to read before you pipe to bash? The script is here. 
b065 text 8391: Open http://localhost:3001, add your provider keys on the Ke
b066 text 8479: On Windows, the easiest path is the desktop .exe installer f
b067 text 8543: Everything else — Docker Compose, local development, declara
b069 heading 8615: Desktop app
b071 text 8669: A native menu-bar app lives in desktop/: the entire router +
b073 text 9221: Download from Releases — the macOS .dmg and the Windows .exe
b074 text 9333: For macOS 12 Monterey or later, choose arm64 (Apple Silicon)
b076 heading 9405: Works with OpenAI-compatible clients
b078 text 9459: Anything that can target an OpenAI-compatible base URL works
b079 text 9571: ChatGPT connects to the same local router through a private 
b080 text 9707: Provider keys can be managed from the terminal too, with a d
b081 text 9795: FreeLLMAPI is local-first and single-user by design. Your pr
b083 heading 9867: Languages
b085 text 9921: The dashboard ships in 60 languages (the desktop tray menu i
b087 text 10099: The full list of locales lives in client/src/i18n/locale-con
b088 text 10139: The original six locales are human-reviewed; the newer ones 
b089 text 10203: Translations live in client/src/i18n/locales/ as flat JSON f
b091 heading 10323: Premium (live catalog)
b093 text 10377: The router keeps its model catalog fresh on its own: it pull
b094 text 10489: The catalog currently tracks 34 providers, 474 model familie
b095 text 10577: Free installs pull the same signed catalog, but from the mon
b096 text 10665: Premium keeps that signed catalog live on every router you r
b097 text 10753: Go live at freellmapi.co →
b098 list 10793: $19/year or $49 once, lifetime. Stripe checkout; cancel anyt
b099 text 10965: The catalog server never sees your prompts, completions, or 
b101 heading 11037: Using the API
b103 code 11092: from openai import OpenAI client = OpenAI( base_url="http://
b106 text 11396: Streaming, the auto:* routing strategies, tool calling, visi
b108 heading 11516: Screenshots
b111 heading 11578: Models
b113 text 11619: Pick a routing strategy and watch the monthly token budget f
b116 heading 12385: Keys
b118 text 12426: Manage provider credentials and grab the unified API key you
b121 heading 13169: Playground
b123 text 13210: Send a chat completion through the router and see which prov
b126 heading 14000: Analytics
b128 text 14041: Request volume, success rate, tokens in and out, average lat
b131 heading 14784: How it works
b134 text 15262: One request in, the best free model out: the router picks th
b136 heading 15382: FAQ
b138 text 15436: Do I need a password? Not for the desktop app — the dashboar
b139 text 15524: I forgot the password on a server install. Click Forgot pass
b140 text 15636: Where are the logs? In the container log for Docker, in the 
b141 text 15700: How do I uninstall? Remove the app (Trash on macOS, Settings
b142 text 15788: Longer answers, per install method: docs/en/install/01-insta
b144 heading 15836: Limitations
b146 text 15890: Stacking free tiers has real trade-offs: no frontier models,
b148 heading 16010: Contributing
b150 text 16064: Contributors very welcome! See CONTRIBUTING.md for the dev l
b151 list 16152: Add a provider — copy server/src/providers/openai-compat.ts 
b152 text 16448: npm install && npm run dev gets you the server on :3001 and 
b154 heading 16592: Contributors
b158 heading 17033: Disclaimer
b160 text 17088: This project is for personal experimentation and learning, n
b161 text 17248: How each provider's ToS views a personal, single-user proxy 
b163 heading 17320: License
b166 media 2156: FreeLLMAPI dashboard — Models page with the monthly token bu
b167 media 3812: The free tier, stacked — ~7.4B tokens of free inference per 
b168 media 5559: Feature comparison against OpenRouter, LiteLLM, and Portkey
b169 media 6279: Feature overview
b170 media 8733: FreeLLMAPI desktop app
b171 media 11707: Models page
b172 media 12490: Keys page
b173 media 13322: Playground page
b174 media 14105: Analytics page
b175 media 14838: One request in, the best free model out — the fallback chain

## Media
m00 block b166 still 1704x985: FreeLLMAPI dashboard — Models page with the monthly token budget
m01 block b167 still 1600x822: The free tier, stacked — ~7.4B tokens of free inference per month across 34 prov
m02 block b168 still 1600x1135: Feature comparison against OpenRouter, LiteLLM, and Portkey
m03 block b169 still 1600x837: Feature overview
m04 block b170 still 1600x888: FreeLLMAPI desktop app
m05 block b171 still 1280x989: Models page
m06 block b172 still 1280x989: Keys page
m07 block b173 still 1280x989: Playground page
m08 block b174 still 1280x989: Analytics page
m09 block b175 still 1600x765: One request in, the best free model out — the fallback chain with live scores, c