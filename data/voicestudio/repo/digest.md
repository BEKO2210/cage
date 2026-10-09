# debpalash/VoiceStudio
VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.
stars 55868 · forks 6265 · Python · licence AGPL-3.0 · release v0.5.6 (2026-09-23) · pushed 2026-10-09 · topics ai, audiobook, cuda, dubbing, elevenlabs-alternative, huggingface, local-first, mlx
languages {'Python': 56.0, 'JavaScript': 22.0, 'TypeScript': 19.6, 'Shell': 0.7, 'CSS': 0.6}

## README by section
### (intro)
VoiceStudio Open-source voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.
### Your voice. Your workflow.
Start with **VoiceStudio** (default, powered by k2-fsa/OmniVoice), or choose another engine.
| Create | Produce | Connect |
| Clone a voice or design your own | Dub videos with timed speech | Local API & MCP for agents |
| Dictate with a floating widget | Stories, audiobooks & batch jobs | Optional remote workers |
### Get started
### One-command install (macOS / Linux)
On Windows, run `irm https://voicestudio.sh/install | iex` in PowerShell.
| Hardware | Support |
| NVIDIA GPU (Windows / Linux) | CUDA acceleration |
| Apple Silicon | Metal (MPS) acceleration |
| No dedicated GPU (Intel/AMD integrated graphics, older PCs) | Fully usable on the CPU, slower; setup installs the small CPU buil
| Windows on ARM (Snapdragon X etc.) | **Experimental**, validation pending: native ARM64 app, x64 Python backend under emulation,
| Intel Mac | App UI only; connect to a remote backend (why) |
```
# Latest Electron release
curl -fsSL https://voicestudio.sh/install | sh

# A specific published Electron release (replace X.Y.Z)
...
```
### Install with prompt
Paste into your coding agent (Claude Code, Codex, Cursor, …): The agent guide covers hardware detection, reusing existing data, asking before model downloads, a
```
Install the VoiceStudio Electron app on this device and verify it works, following
https://github.com/debpalash/VoiceStudio/blob/main/docs/install/agent.md
```
```
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun install
bun run setup:api  # prepare Python dependencies before starting Electron
...
```
### Documentation
Agent skills: `npx skills add debpalash/VoiceStudio` — choose **voicestudio** for audio workflows or **voicestudio-maintainer** for repository maintenance.
| Need | Start here |
| Setup help | Troubleshooting · Model downloads |
| Models & audio quality | Engine guides · Benchmarks |
| Integrations | Local API · MCP · Examples |
| Development | Contributing · Electron · Changelog |
### Sponsors
**Become a featured partner.** Apply for a paid placement · Email us Support development: Ko-fi · PayPal · Sponsorship details
### License & responsible use
AGPL-3.0.

## Sentences with numbers (verbatim)
- VoiceStudio Open-source voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.
- Or download from Releases (macOS `.dmg`, Windows `.exe`, Linux `.AppImage` or `.deb`) and follow your platform guide: **macOS · Windows · Linux · Docker** | Hardware | Support | |-
- > **Electron is the only desktop app and web UI.** Version 0.5.3 was the final Tauri release.

## Page blocks (id kind y: text)
b000 header 172: VoiceStudio Public Sponsor Notifications Fork6.3k (6.3k) Sta
b001 star 192: Star55.9k (55.9k)
b002 about 250: About VoiceStudio is the open-source, fully-local ElevenLabs
b003 files 368: Name Last commit message Last commit date .agents/skills cho
b005 text 2187: VoiceStudio Open-source voice cloning, voice design, video d
b009 text 2444: Open-source voice cloning, voice design, video dubbing, dict
b010 text 2508: Website · Download · Get started · Docs · Discord · 简体中文 · 日
b014 heading 3180: Your voice. Your workflow.
b016 table 3234: rows 0-2 (0 = header) Create Produce Connect Clone a voice or design your own Dub 
b017 text 3362: Start with VoiceStudio (default, powered by k2-fsa/OmniVoice
b018 text 3426: Local workflows run on your hardware. Remote services are op
b019 text 3466: Explore the workspaces · Clone, dub, design & models
b021 heading 3514: Get started
b024 heading 3577: One-command install (macOS / Linux)
b026 code 3618: # Latest Electron release curl -fsSL https://voicestudio.sh/
b029 text 3882: On Windows, run irm https://voicestudio.sh/install | iex in 
b030 text 3994: Or download from Releases (macOS .dmg, Windows .exe, Linux .
b031 text 4058: macOS · Windows · Linux · Docker
b032 table 4098: rows 0-5 (0 = header) Hardware Support NVIDIA GPU (Windows / Linux) CUDA accelerat
b033 text 4385: Open Voice cloning, choose a voice or add a clean reference 
b035 heading 4457: Install with prompt
b037 text 4498: Paste into your coding agent (Claude Code, Codex, Cursor, …)
b039 code 4538: Install the VoiceStudio Electron app on this device and veri
b041 text 4626: The agent guide covers hardware detection, reusing existing 
b042 text 4690: Run the Electron preview from source
b043 quote 4730: Electron is the only desktop app and web UI. Version 0.5.3 w
b045 heading 4826: Documentation
b047 table 4880: rows 0-4 (0 = header) Need Start here Setup help Troubleshooting · Model downloads
b048 text 5082: Agent skills: npx skills add debpalash/VoiceStudio — choose 
b050 heading 5154: Sponsors
b053 text 5335: Become a featured partner. Apply for a paid placement · Emai
b054 text 5375: Support development: Ko-fi · PayPal · Sponsorship details
b056 heading 5423: License & responsible use
b058 text 5477: AGPL-3.0. Models have their own licenses; review them before
b059 media 2591: A tour of the Electron app: voice cloning, voice design, dub
b060 media 3499: Electron voice cloning workspace with the bundled demo voice
b061 media 3497: Electron video dubbing workspace
b062 media 3819: Describe a voice in the Electron voice design workspace
b063 media 3817: Install and manage local speech models
b064 media 4147: VoiceStudio desktop workspace
b065 media 5208: Your brand — apply for a featured VoiceStudio sponsor slot

## Media
m00 block b059 animated 154f@10.0 1080x720: A tour of the Electron app: voice cloning, voice design, dubbing, and model mana
m01 block b060 still 1440x960: Electron voice cloning workspace with the bundled demo voice
m02 block b061 still 1440x960: Electron video dubbing workspace
m03 block b062 still 1440x960: Describe a voice in the Electron voice design workspace
m04 block b063 still 1440x960: Install and manage local speech models
m05 block b064 still 2628x1950: VoiceStudio desktop workspace
m06 block b065 still NonexNone: Your brand — apply for a featured VoiceStudio sponsor slot