# blixvip/NullMotion
Watch a finished motion-graphics ad play over the HyperFrames drafts it grew from, frame-synced, and export the breakdown as an MP4. Local, zero dependencies. Join the Discord: discord.gg/zEB4VjmfSb
stars 705 · forks 62 · HTML · licence None · release v1.0.0 (2026-10-04) · pushed 2026-10-04 · topics animation, ffmpeg, frame-accurate, gsap, html5-video, hyperframes, javascript, launch-video
languages {'HTML': 54.3, 'JavaScript': 34.3, 'CSS': 10.8, 'Python': 0.5}

## README by section
### (intro)
Null Motion Watch a finished motion-graphics ad play over the rough drafts it grew from, frame-synced.Then export the whole breakdown as one MP4.
### Quick start
3.
```
git clone https://github.com/blixvip/NullMotion.git && cd NullMotion   # 1. get it
npm start                                                              # 2. run it (Node 22+, nothin
```
### What it does
Motion-graphics ads look effortless, but every one starts as a rough plan: which idea goes in which section, and when each move lands.
### Showcase
The repo ships three references with their drafts, ready to play: These clips come from other creators and are used as examples.
| | Reference | Length | Drafts |
| | **Infinite · Global payments** | 0:30 | 7 |
| | **SaaS · Launch sequence** | 1:02 | 8 |
| | **Motion study 08** | 0:03 | 3 |
### 🎬 Show what you made
Exported a breakdown or built drafts for your own ad?
### How it works
1.
### Requirements
| | Needed for |
| **Node.js 22+** | Running the local server (`npm start`). No dependencies to install. |
| **Chrome or Edge** | MP4 export (WebCodecs + `requestVideoFrameCallback`). Playback works in any modern browser. |
| **FFmpeg / ffprobe** (optional) | Importing your own references, planning sections, rebuilding the showcase, and extracting audi
| **Python 3** (optional) | `scripts/import-motionclone.py`. |
### Bring your own references
With Python, FFmpeg and ffprobe installed: Imported media stays local in `.local-media/` and `public/references/` (both ignored by Git) and takes precedence ove
```
python scripts/import-motionclone.py --source /path/to/MotionClone
node scripts/plan-sections.mjs      # sections + scene cuts + contact sheets
```
### FAQ and troubleshooting
**The Download button says "Needs Chrome or Edge".** Export uses WebCodecs and `requestVideoFrameCallback`.
### Project layout
```
public/demo.html · demo.mjs · demo.css   the preview page and exporter
public/drafts.mjs                        HyperFrames draft engine (beat kinds)
public/scraps.mjs                        hand-built drafts for the Interface reference
public/editor.*                          the earlier launch editor, at /editor
...
```
```
npm run dev     # restart on change
npm run check   # UI file checks
npm test        # node --test
```
### Notes
- The browser only calls this project's own origin.
### Contributing
Bug reports, draft ideas, and pull requests are welcome.
### Community
💬 Questions, help, feedback, release news, and your renders all go in **Insider AI on Discord**.

## Sentences with numbers (verbatim)
- **Drafts.** `public/drafts.mjs` is a small HyperFrames engine: each draft is a 640×360 HTML scene on a paused GSAP timeline.

## Page blocks (id kind y: text)
b000 header 72: blixvip / NullMotion Public Notifications Fork 62 Star 705 C
b001 star 88: Star 705
b016 code 2130: git clone https://github.com/blixvip/NullMotion.git && cd Nu
b019 list 2217: Open http://127.0.0.1:4343, pick a reference, and press Down
b027 list 2672: The final film on top. The full ad, full width, playing on a
b043 list 4692: Sections. scripts/plan-sections.mjs splits each reference in
b052 code 5457: python scripts/import-motionclone.py --source /path/to/Motio
b075 code 6747: npm run dev # restart on change npm run check # UI file chec
b081 list 6916: The browser only calls this project's own origin. The earlie
b091 media 1413: The Infinite ad playing on top, its black-and-white drafts u
b092 media 2892: The Null Motion page: film, drafts, and the video library
b093 media 3693: 
b094 media 3798: 
b095 media 3902: 
b096 media 4016: Motion study 08 above its drafts

## Media
m00 block b091 animated 120f@12.0 800x554: The Infinite ad playing on top, its black-and-white drafts underneath, in sync
m01 block b092 still 1600x1233: The Null Motion page: film, drafts, and the video library
m02 block b093 still 480x270: 
m03 block b094 still 480x270: 
m04 block b095 still 480x270: 
m05 block b096 animated 33f@12.0 720x508: Motion study 08 above its drafts