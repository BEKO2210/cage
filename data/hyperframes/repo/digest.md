# heygen-com/hyperframes
Write HTML. Render video. Built for agents.
stars 59553 · forks 5310 · TypeScript · licence Apache-2.0 · release v0.8.143 (2026-10-08) · pushed 2026-10-09 · topics ai, animation, ffmpeg, framework, gsap, html, mcp, puppeteer
languages {'TypeScript': 87.6, 'JavaScript': 11.8, 'Shell': 0.2, 'Python': 0.2, 'CSS': 0.1}

## README by section
### (intro)
Write HTML.
### Quick Start
### With an AI coding agent
For Claude Code, install the versioned plugin: Enable auto-update for the **hyperframes** marketplace in `/plugin` → **Marketplaces**, then use `/hyperframes:hy
```
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```
```
npx skills add heygen-com/hyperframes
```
### Skills
HyperFrames ships 21 skills agents load on demand.
### Plugin packages
Plugins bundle the full skill catalog and use their agent's update manager.
### Upload to Codex
Build the upload-ready Codex plugin archive from the committed `HEAD` version of the manifest, brand assets, and skills: This writes `dist/hyperframes-plugin.zi
```
bun run package:codex-plugin
```
### Router
| Skill | Use when |
| `/hyperframes` | **Read first** for any request to make / create / edit / animate / render a video, animation, or motion graphic
### Creation workflows
| Skill | Use when |
| `/product-launch-video` | Any **website** — marketing / launching / promoting a product (from its URL, a brief, or a script), or
| `/faceless-explainer` | **Explaining a topic / concept** from arbitrary text — no product, no URL, no website capture; every vis
| `/pr-to-video` | A **GitHub pull request** (PR URL, `owner/repo#N` ref, or "this PR") → changelog / feature-reveal / fix / refac
| `/embedded-captions` | Adding **captions / subtitles** to an existing talking-head video (footage untouched) — verbatim rail, em
| `/talking-head-recut` | Packaging an existing talking-head / interview / podcast video with **designed graphic overlays** — lowe
|...
### Domain skills (loaded on demand)
Atomic capabilities the creation workflows compose against — pull one when you need that specific layer.
| Skill | Covers |
| `/hyperframes-core` | The composition contract — `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variables
| `/hyperframes-animation` | All animation knowledge — atomic motion rules, scene blueprints, transitions, runtime adapters (GSAP 
| `/hyperframes-keyframes` | Seek-safe keyframe authoring across runtimes — GSAP timelines, CSS keyframes, Anime.js, WAAPI, FLIP, 
| `/hyperframes-creative` | Non-animation creative direction — `frame.md` / `design.md`, palettes, typography, narration, beat pla
| `/media-use` | The media OS (a host app's own music and sound-effect tools come first for those) — resolve any media need (BGM, 
|...
### Manually with the CLI
**Requirements:** Node.js 22+, FFmpeg
```
npx hyperframes init my-video
cd my-video
npx hyperframes preview      # preview in browser with live reload
npx hyperframes render       # render to MP4
```
### What You Can Build
Need ideas?
### Frame.md
**frame.md — your design system, ready for video.** Every brand has a `design.md`.
### How It Works
Define a video as HTML.
```
<div id="stage" data-composition-id="launch" data-start="0" data-width="1920" data-height="1080">
  <video
    class="clip"
    data-start="0"
...
```
### HyperFrames Stack
HyperFrames is the open-source rendering engine, plus a growing set of tools around HTML-native video creation.
| Piece | Status | What it does |
| CLI | Available | Scaffold, preview, lint, inspect, and render local video projects |
| Core / Engine / Producer | Available | Parse compositions, drive headless Chrome, encode video, and mix audio |
| Catalog | Available | Reusable blocks and components for transitions, overlays, captions, charts, maps, and effects |
| Agent skills | Available | Teach coding agents the video-production patterns that generic web docs miss |
| Studio | Available, evolving | Browser surface for previewing and editing compositions |
|...
### Catalog
Install ready-to-use blocks and components: Browse the catalog at hyperframes.heygen.com/catalog.
```
npx hyperframes add flash-through-white   # shader transition
npx hyperframes add instagram-follow      # social overlay
npx hyperframes add data-chart            # animated chart
```
### Why HyperFrames?
- **HTML-native:** compositions are HTML files with data attributes.
### HyperFrames vs Remotion
HyperFrames is inspired by Remotion.
| | **HyperFrames** | **Remotion** |
| Authoring | HTML + CSS + seekable animation | React components |
| Build step | None; `index.html` plays as-is | Bundler required |
| Agent handoff | Plain HTML files | JSX / React project |
| Library-clock animations | Seekable, frame-accurate via adapters | Wall-clock animation patterns need care |
| Distributed rendering | Local and AWS Lambda render paths | Remotion Lambda, mature cloud renderer |
|...
### Documentation
Full documentation: hyperframes.heygen.com/introduction - Quickstart - Showcase - Guides - API Reference - Catalog - Examples - AWS Lambda rendering
### Packages
| Package | Description |
| `hyperframes` | CLI for creating, previewing, linting, and rendering compositions |
| `@hyperframes/core` | Types, parsers, generators, linter, runtime, and frame adapters |
| `@hyperframes/engine` | Seekable page-to-video capture engine using Puppeteer and FFmpeg |
| `@hyperframes/producer` | Full rendering pipeline for capture, encode, and audio mix |
| `@hyperframes/studio` | Browser-based composition editor UI |
|...
### Community
HyperFrames is used in production at HeyGen, with community examples from teams like tldraw, TanStack, and others in ADOPTERS.md.
### Development Note
The repo uses Git LFS for golden regression-test baselines under `packages/producer/tests/**/output.mp4` (about 240 MB of `.mp4` files).
```
# macOS
brew install git-lfs

# Ubuntu / Debian
...
```
```
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/heygen-com/hyperframes.git
```
### License
Apache 2.0

## Sentences with numbers (verbatim)
- Studio | Quickstart | Showcase | Playground | Catalog | Docs | Discord HyperFrames is an open-source framework for turning HTML, CSS, media, and seekable animations into determinis
- Agents and non-interactive runs should use `npx hyperframes skills update` instead — it installs exactly the core set, whereas `skills add --all` installs all 21 published skills.
- ## Skills HyperFrames ships 21 skills agents load on demand.
- ### Upload to Codex Build the upload-ready Codex plugin archive from the committed `HEAD` version of the manifest, brand assets, and skills: This writes `dist/hyperframes-plugin.zi
- Up to ~3 min (sweet spot 30-90s).
- | | `/motion-graphics` | A short, **unnarrated, design-led motion graphic** (~under 10s) — kinetic type, stat / chart hit, logo sting, lower-third, animated tweet / headline.
- - Questions and ideas: Discord - Bugs and feature requests: GitHub Issues - User research: Book a casual 30-minute conversation with the HyperFrames team — no preparation or sales 

## Page blocks (id kind y: text)
b000 header 172: hyperframes Public Notifications Fork5.3k (5.3k) Star59.6k (
b001 star 192: Star59.6k (59.6k)
b002 about 250: About Write HTML. Render video. Built for agents. hyperframe
b003 files 368: Name Last commit message Last commit date .agents/skills doc
b007 text 2548: Write HTML. Render video. Built for agents.
b008 text 2588: Studio | Quickstart | Showcase | Playground | Catalog | Docs
b010 text 3101: HyperFrames is an open-source framework for turning HTML, CS
b012 heading 3197: Quick Start
b015 heading 3259: With an AI coding agent
b017 text 3300: For Claude Code, install the versioned plugin:
b018 code 3340: claude plugin marketplace add heygen-com/hyperframes claude 
b021 text 3428: Enable auto-update for the hyperframes marketplace in /plugi
b022 text 3516: For standalone skills (including OpenCode), use:
b023 code 3556: npx skills add heygen-com/hyperframes
b026 quote 3624: The picker opens with nothing pre-selected — the Core Skills
b028 quote 3888: Using /hyperframes, create a 10-second product intro with a 
b029 text 3952: The skills teach agents the HyperFrames production loop: pla
b031 heading 4048: Skills
b033 text 4102: HyperFrames ships 21 skills agents load on demand. Read /hyp
b034 text 4190: For standalone installation, default to the core set — the r
b035 text 4374: Standalone installs stay lean after that: npx hyperframes in
b037 heading 4518: Plugin packages
b039 text 4559: Plugins bundle the full skill catalog and use their agent's 
b041 heading 4655: Upload to Codex
b043 text 4696: Build the upload-ready Codex plugin archive from the committ
b044 code 4760: bun run package:codex-plugin
b047 text 4828: This writes dist/hyperframes-plugin.zip with a hyperframes/ 
b049 heading 4900: Router
b051 table 4941: rows 0-1 (0 = header) Skill Use when /hyperframes Read first for any request to ma
b053 heading 5112: Creation workflows
b055 table 5153: rows 0-10 (0 = header) Skill Use when /product-launch-video Any website — marketing
b057 heading 6017: Domain skills (loaded on demand)
b059 text 6058: Atomic capabilities the creation workflows compose against —
b060 table 6122: rows 0-9 (0 = header) Skill Covers /hyperframes-core The composition contract — da
b061 text 7037: For visual design handoff workflows, see the Claude Design g
b063 heading 7085: Manually with the CLI
b065 code 7126: npx hyperframes init my-video cd my-video npx hyperframes pr
b068 text 7253: Requirements: Node.js 22+, FFmpeg
b070 heading 7301: What You Can Build
b072 text 7355: Need ideas? Browse the Showcase for finished videos you can 
b073 list 7395: Product launch videos and feature announcements PR walkthrou
b075 heading 7583: Frame.md
b077 text 7637: frame.md — your design system, ready for video.
b078 text 7677: Every brand has a design.md. None of them were written for a
b079 text 7789: The output is a DESIGN.md superset your whole toolchain can 
b080 table 7853: rows 0-4 (0 = header) Biennale Yellow BlockFrame Blue Professional Bold Poster Bro
b081 text 9191: Browse and remix them all at hyperframes.dev/design.
b083 heading 9239: How It Works
b085 text 9293: Define a video as HTML. Add data attributes for timing and t
b086 code 9357: <div id="stage" data-composition-id="launch" data-start="0" 
b089 text 9977: Preview instantly in the browser. Render locally or in Docke
b091 heading 10049: HyperFrames Stack
b093 text 10103: HyperFrames is the open-source rendering engine, plus a grow
b094 table 10167: rows 0-8 (0 = header) Piece Status What it does CLI Available Scaffold, preview, l
b096 heading 10717: Catalog
b098 text 10771: Install ready-to-use blocks and components:
b099 code 10811: npx hyperframes add flash-through-white # shader transition 
b102 text 10918: Browse the catalog at hyperframes.heygen.com/catalog.
b104 heading 10966: Why HyperFrames?
b106 list 11020: HTML-native: compositions are HTML files with data attribute
b108 heading 11304: HyperFrames vs Remotion
b110 text 11359: HyperFrames is inspired by Remotion. Both tools render video
b111 table 11447: rows 0-6 (0 = header) HyperFrames Remotion Authoring HTML + CSS + seekable animati
b112 text 11771: Read the full comparison in the HyperFrames vs Remotion guid
b114 heading 11819: Documentation
b116 text 11873: Full documentation: hyperframes.heygen.com/introduction
b117 list 11913: Quickstart Showcase Guides API Reference Catalog Examples AW
b119 heading 12129: Packages
b121 table 12183: rows 0-8 (0 = header) Package Description hyperframes CLI for creating, previewing
b123 heading 12613: Community
b125 text 12667: HyperFrames is used in production at HeyGen, with community 
b126 list 12731: Questions and ideas: Discord Bugs and feature requests: GitH
b128 heading 12915: Development Note
b130 text 12969: The repo uses Git LFS for golden regression-test baselines u
b131 code 13033: # macOS brew install git-lfs # Ubuntu / Debian sudo apt inst
b134 text 13298: If you only need source files, you can skip LFS content:
b135 code 13338: GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/heygen-co
b139 heading 13414: License
b142 media 2392: HyperFrames
b143 media 2628: HyperFrames app opening from the Dock: native Mac and Linux 
b144 media 7860: Biennale Yellow
b146 media 8124: Blue Professional
b148 media 8389: Broadside
b150 media 8653: Cartesian
b152 media 8917: Coral

## Media
m00 block b142 still NonexNone: HyperFrames
m01 block b143 animated 130f@25.0 1200x675: HyperFrames app opening from the Dock: native Mac and Linux app now available
m02 block b144 still 1600x900: Biennale Yellow
m03 block b145 still 1600x900: BlockFrame
m04 block b146 still 1600x900: Blue Professional
m05 block b147 still 1600x900: Bold Poster
m06 block b148 still 1600x900: Broadside
m07 block b149 still 1600x900: Capsule
m08 block b150 still 1600x900: Cartesian
m09 block b151 still 1600x900: Cobalt Grid
m10 block b152 still 1600x900: Coral
m11 block b153 still 1600x900: Creative Mode