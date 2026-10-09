# calesthio/OpenMontage
World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio.
stars 63470 · forks 8080 · Python · licence AGPL-3.0 · release None () · pushed 2026-10-03 · topics agent, agentic-ai, ai, claude, copilot, cursor, elevenlabs, ffmpeg
languages {'Python': 70.1, 'HTML': 18.5, 'JavaScript': 5.5, 'TypeScript': 4.6, 'CSS': 0.7}

## README by section
### (intro)
Monty the Clapper — the official mascot of OpenMontage OpenMontage The first open-source, agentic video production system.
### Sponsors
> Want to support OpenMontage?
### Start From A Video You Already Love
Starting from a reference video is often faster than starting from a blank prompt.
```
"Here's a YouTube Short I love. Make me something like this, but about quantum computing."
```
### Watch It Happen — The Backlot Living Storyboard
Chat tells you what the agent *said*.
```
python -m backlot open                  # the library — every project on disk
python -m backlot open <project-id>     # one production's live board
python scripts/backlot_simulate_run.py  # no production yet? watch a simulated one live
```
### Quick Start
### Prerequisites
- **Python 3.10+** — python.org - **FFmpeg** — `brew install ffmpeg` / `sudo apt install ffmpeg` / ffmpeg.org - **Node.js 18+** — nodejs.org - **An AI coding as
### Install & Run
Open the project in your AI coding assistant and tell it what you want: Or if you want the real-footage path: That's it.
```
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```
```
"Make a 60-second animated explainer about how neural networks learn"
```
### If You're An OpenClaw Agent Reading This, Congratulations: You Probably Passed The Turing Test
This repo is built for agentic operation.
### Add API Keys (optional — more keys = more tools)
Have a GPU?
```
# .env — every key is optional, add what you have

# Image + video gateway:
FAL_KEY=your-key               # FLUX images + Google Veo, Kling, MiniMax video + Recraft images
...
```
```
make install-gpu

# Then add to .env:
VIDEO_GEN_LOCAL_ENABLED=true
...
```
### What You Get With Zero API Keys
You don't need paid API keys to make real videos.
| Capability | Free Tool | What It Does |
| **Narration** | Piper TTS | Free offline text-to-speech — real human-sounding narration |
| **Open footage** | Archive.org + NASA + Wikimedia Commons | Free/open archival footage, educational media, and documentary textu
| **Extra stock** | Pexels + Unsplash + Pixabay | Free stock footage/images (developer keys are free to get) |
| **Composition (React)** | Remotion | React-based rendering — spring-animated image scenes, text cards, stat cards, charts, TikTo
| **Composition (HTML/GSAP)** | HyperFrames | HTML/CSS/GSAP rendering — kinetic typography, product promos, launch reels, registry
|...
### Try These Prompts
Copy any of these into your AI coding assistant after setup.
### Start from a reference video
> "Here's a YouTube short I love.
### Zero keys needed
> "Make a 45-second animated explainer about why the sky is blue" > "Create a 60-second video about the history of the internet, with narration and captions" > 
### Free real-footage documentary path
> "Make a 90-second documentary montage about what a city feels like at 4am.
### With an image/video provider configured (~$0.15–$1.50)
> "Create a 30-second Ghibli-style animated video of a magical floating library in the clouds at golden hour" > "Make a 30-second anime-style animation of an un
### Full setup (~$1–$3)
> "Create a cinematic 30-second trailer for a sci-fi concept: humanity receives a warning from 1000 years in the future" > "Make a 90-second animated explainer 
### Pipelines
Each pipeline is a complete production workflow, from idea to finished video.
| Pipeline | What It Produces | Best For |
| **Animated Explainer** | AI-generated explainer with research, narration, visuals, music | Educational content, tutorials, topic
| **Animation** | Motion graphics, kinetic typography, animated sequences | Social media, product demos, abstract concepts |
| **Avatar Spokesperson** | Avatar-driven presenter videos | Corporate comms, training, announcements |
| **Cinematic** | Trailer, teaser, and mood-driven edits | Brand films, teasers, promotional content |
| **Clip Factory** | Batch of ranked short-form clips from one long source | Repurposing long content for social media |
|...
```
research -> proposal -> script -> scene_plan -> assets -> edit -> compose
```
### Why OpenMontage?
Most AI video tools give you a single clip from a prompt.
### How It Works
OpenMontage uses an **agent-first architecture**.
```
You: "Make an explainer video about how black holes form"
 |
 v
Agent reads pipeline manifest (YAML) -- stages, tools, review criteria, success gates
...
```
### Architecture
```
OpenMontage/
├── tools/              # 100+ registered production tools (the agent's hands)
│   ├── video/          # 20+ generation providers + compose, stitch, trim
│   ├── audio/          # 10+ speech providers + music, mixing, enhancement
...
```
### Three-Layer Knowledge Architecture
Each tool declares which Layer 3 skills it relies on.
```
Layer 1: tools/ + pipeline_defs/     "What exists" — executable capabilities + orchestration
Layer 2: skills/                     "How to use it" — OpenMontage conventions and quality bars
Layer 3: .agents/skills/             "How it works" — external technology knowledge packs
```
### Supported Providers
> **Full setup guide with pricing and free tiers:** `docs/PROVIDERS.md` Video Generation — 20+ providers Image Generation — 15+ providers Text-to-Speech — 10+ p
| Provider | Type | Notes |
| **Kling (fal.ai)** | Cloud API | High quality, fast via fal.ai gateway |
| **Kling Official** | Cloud API | Official direct API with separate `kling_official` provider |
| **Atlas Cloud** | Cloud API | Unified gateway for Seedance, MiniMax, Hunyuan, and other multimodal models |
| **Seedance 2.0 (Volcengine Ark)** | Cloud API | Official direct API with separate `seedance_ark` provider |
| **Seedance 2.5 / 2.0** | Cloud API | Text, image, and reference-driven video workflows through supported gateways |
|...
### Style System
Style playbooks define the visual language for your productions: Playbooks control typography, color palettes, motion styles, audio profiles, and quality rules.
| Playbook | Best For |
| **Clean Professional** | Corporate, educational, SaaS |
| **Flat Motion Graphics** | Social media, TikTok, startups |
| **Minimalist Diagram** | Technical deep-dives, architecture |
### Platform Output Profiles
Built-in render profiles for every major platform: ---
| Profile | Resolution | Aspect Ratio |
| YouTube Landscape | 1920x1080 | 16:9 |
| YouTube 4K | 3840x2160 | 16:9 |
| YouTube Shorts | 1080x1920 | 9:16 |
| Instagram Reels | 1080x1920 | 9:16 |
| Instagram Feed | 1080x1080 | 1:1 |
|...
### Production Governance
OpenMontage treats video production like real engineering — with quality gates, audit trails, and enforcement at every stage.
### Quality Gates
- **Human approval gates are enforced, not suggested** — proposal, script, scene plan, generated assets, and publish all pause for your sign-off.
### Scored Provider Selection
Every tool selection (video generation, image generation, TTS, music) runs through a 7-dimension scoring engine: task fit (30%), output quality (20%), control f
### Decision Audit Trail
Every major creative and technical choice — provider selection, style/playbook choice, music track, voice selection, renderer family, any fallback or downgrade 
### Budget Controls
- **Estimate** before execution — see what it will cost - **Reserve** budget — lock funds before the call - **Reconcile** after — record actual spend - **Config
### Agent Compatibility
OpenMontage works with any AI coding assistant that can read files and execute Python.
| Platform | Config File |
| **Claude Code** | `CLAUDE.md` |
| **Cursor** | `CURSOR.md` + `.cursor/rules/` |
| **GitHub Copilot** | `COPILOT.md` + `.github/copilot-instructions.md` |
| **Codex** | `CODEX.md` |
| **Windsurf** | `.windsurfrules` |
### Contributing
OpenMontage is built to be extended.
### Adding a New Tool
1.
### Adding a New Pipeline
1.
### Join the Community
We use GitHub Discussions to share work and ideas: - **Show and Tell** — Share videos you've made, prompts that worked well, or creative workflows you've discov
### Contact
For updates, releases, and behind-the-scenes build notes, follow @calesthioailabs.
### Testing
---
```
# Run contract tests (no API keys needed)
make test-contracts

# Run all tests
...
```
### Star History
---
### License
GNU AGPLv3 --- **OpenMontage** — Production-grade video with real quality enforcement, orchestrated by your AI assistant.

## Sentences with numbers (verbatim)
- Use real footage only, no narration, elegiac tone." > "Create a 60-second Adam-Curtis-style archival collage about 1950s consumer optimism.
- --- ## Supported Providers > **Full setup guide with pricing and free tiers:** `docs/PROVIDERS.md` Video Generation — 20+ providers | Provider | Type | Notes | |----------|------|-
- "motion-led" video with 80% still images), slideshow risk score is critical, or renderer family is missing.
- ### Scored Provider Selection Every tool selection (video generation, image generation, TTS, music) runs through a 7-dimension scoring engine: task fit (30%), output quality (20%),

## Page blocks (id kind y: text)
b000 header 72: calesthio / OpenMontage Public Notifications Fork 8.1k Star 
b001 star 88: Star 63.5k
b053 list 9235: Paste a reference video The agent analyzes transcript, pacin
b058 list 9463: What it keeps from the reference: pacing, hook style, struct
b072 code 12251: python -m backlot open # the library — every project on disk
b082 list 12558: Python 3.10+ — python.org FFmpeg — brew install ffmpeg / sud
b086 code 12731: git clone https://github.com/calesthio/OpenMontage.git cd Op
b103 list 13567: Read the contract first Start with AGENT_GUIDE.md, then PROJ
b107 code 13896: # .env — every key is optional, add what you have # Image + 
b118 list 15368: Image-based video: Piper narrates your script, images provid
b172 list 18435: 10+ production pipelines — explainers, talking heads, screen
b220 list 22218: Human approval gates are enforced, not suggested — proposal,
b234 list 23181: Estimate before execution — see what it will cost Reserve bu
b250 list 24096: Create a Python file in the appropriate tools/ subdirectory 
b254 list 24269: Create a YAML manifest in pipeline_defs/ Create stage direct
b260 list 24518: Show and Tell — Share videos you've made, prompts that worke
b270 code 24956: # Run contract tests (no API keys needed) make test-contract
b284 media 2209: Monty the Clapper — the official mascot of OpenMontage
b285 media 3554: 
b286 media 4147: 
b287 media 4957: 
b288 media 5622: 
b289 media 6432: 
b290 media 7073: 
b291 media 7739: 
b292 media 8380: 
b293 media 9890: Backlot live board — assets generating
b294 media 10619: Backlot storyboard — filmstrip with takes and renders
b295 media 11488: Backlot script gate — awaiting approval
b296 media 11959: Backlot library
b297 media 25190: Star History Chart

## Media
m00 block b284 still NonexNone: Monty the Clapper — the official mascot of OpenMontage
m01 block b285 animated 300f@30 1920x1080: 
m02 block b286 animated 300f@30 540x960: 
m03 block b287 animated 300f@30 1280x720: 
m04 block b288 animated 300f@30 720x1280: 
m05 block b289 animated 300f@24.0 2276x1280: 
m06 block b290 animated 300f@30 2276x1280: 
m07 block b291 animated 300f@30 960x540: 
m08 block b292 animated 300f@30 1280x720: 
m09 block b293 still 1560x1150: Backlot live board — assets generating
m10 block b294 still 1560x1500: Backlot storyboard — filmstrip with takes and renders
m11 block b295 still 1560x760: Backlot script gate — awaiting approval
m12 block b296 still 1560x500: Backlot library
m13 block b297 still NonexNone: Star History Chart