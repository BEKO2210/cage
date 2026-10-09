# bilawalsidhu/gods-eye-view
A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe.
stars 49460 · forks 10012 · JavaScript · licence NOASSERTION · release v0.2.1 (2026-10-03) · pushed 2026-10-08 · topics 3d-globe, cesium, flight-tracking, geospatial, geospatial-intelligence, gis, osint, photogrammetry
languages {'JavaScript': 97.1, 'CSS': 2.3, 'HTML': 0.5, 'Shell': 0.2, 'Python': 0.0}

## README by section
### (intro)
### 🌐 God's Eye View
![CI](https://github.com/bilawalsidhu/gods-eye-view/actions/workflows/ci.yml) ![Reached #1 on GitHub Trending](https://x.com/bilawalsidhu/status/209379888781534
### A spy-satellite simulator in your browser — then you realize the sources are public and the data is real.
Photorealistic 3D globe.
### 🌍 Why This Exists
God's Eye View brings public signals into one explorable globe.
### 🎛️ What This Thing Does
- **🛩️ Cockpit view:** Ride inside a tracked flight — the camera holds the terrain under you all the way down.
### ⚡ Quick Start
**Start without an account or API keys.** Both paths open the same app with Esri satellite imagery and keyless terrain.
### Path 1 — One click, no terminal
1.
### Path 2 — Terminal / coding agent
Use **Node.js 24.x (24.14.0 or later) or 26.x**.
```
git clone https://github.com/bilawalsidhu/gods-eye-view.git
cd gods-eye-view
npm ci
npm run doctor
...
```
### Then power it up — in the app, not in a file
Keys are upgrades, not prerequisites.
### 🕐 The First Five Minutes
Choose a first-run mission, or try these in order.
### 🛩️ The Cockpit
> Every plane should let you do this.
### 🎙️ Talk to It
> Voice can use an **OpenAI API key** or, on the same machine, an opt-in signed-in **ChatGPT/Codex OAuth** session.
### 🛰️ What's on the Globe
Twenty layers and map sources.
| Layer | What you get | Source | Auth |
| 🗺️ **Map Stack** | Esri satellite imagery, Google Photorealistic 3D, OSM, plus additional ion-hosted stacks | Esri / Google / Io
| ✈️ **Live Flights** | 11,000+ live aircraft + route history | OpenSky + adsb.lol | 🟢 (🟡 optional for more polling credits) |
| 🎖️ **Military Flights** | ADS-B military traffic in amber | adsb.lol | 🟢 |
| 🚢 **Live Vessels** | Thousands of ships worldwide | AISStream | 🟡 |
| 🛰️ **Satellites** | 838-object catalog, color-coded by class with a live legend — the **DENSE** chip drops in the whole Starlink
|...
### 📷 Street Level
> Street-level photos from any provider in one panel.
### 🎖️ Field Missions
Once the basics click, run these: _🎙️ = voice missions — they need an OpenAI key._ _Ask the planet: a military contact's last ~24 hours of real trace history, r
| Mission | How |
| **🚁 Ask the planet** | _"Why are all these military helicopters flying in circles?"_ Select a military track — it silently backf
| **✈️ Final approach** | Click-track an airliner lining up for a runway, hop into the **cockpit**, and ride it down. |
| **🌃 Night watch** | Fly to your own city, switch to **NVG**, and let the detection mesh and HUD read the scene. |
| **🚢 Port call** | Vessels on over the Port of Long Beach. Click a tanker for its tactical card and wake trail — then hit **NEARE
| **📻 Tokyo FM** | Orbit Shibuya with the **Radio** layer on — then drag the analog tuner needle: every position snaps to a real s
|...
### 🔧 Under the Hood
How the globe handles live data: - **World-stable icons.** Aircraft and ships point along their _true real-world heading_ at every camera angle — tracked or not
```
src/
├── main.js                 # Bootstrap: Google 3D tiles, layer registration
├── ui.js                   # Runtime UI — panels, HUD, styles, control facade
├── hud.js                  # Intelligence HUD + AI scene summary
...
```
### 🔑 API Keys
🟢 **No key** · 🟡 **Free key** · 🔴 **Metered** Use **POWER UP → Provider Settings** to add keys.
### Choose the capabilities you want
Seven keys.
| | Key | Why | Get it |
| 🟡 | **Cesium ion** | 🗺️ Google Photorealistic 3D, world terrain, and additional ion-hosted imagery stacks. The free Community pl
| 🔴 | **Google Maps** | Direct Google Photorealistic 3D + Google place search (Map Tiles API) | Google Cloud Console — URL-restric
| 🔴 | **OpenAI** | 🎙️ Voice + AI HUD summary through an API key. Provider Settings also offers **USE CHATGPT OAUTH** for cloud voi
| 🟡 | **AISStream** | 🚢 Live global ships | aisstream.io — free signup |
| 🟡 | **NASA FIRMS** | 🔥 Live active fires | firms.modaps.eosdis.nasa.gov — free |
|...
### Cherry on top
Add these if you need higher polling allowances.
| | Key | Why | Get it |
| 🟡 | **OpenSky** | ✈️ More flight-polling credits (🟢 anonymous works without) | opensky-network.org |
| 🟡 | **Launch Library 2** | 🚀 Higher space-missions request allowance (🟢 works without) | thespacedevs.com |
```
# Put keys in .env (see .env.example), or pass them as env vars:
OPENAI_API_KEY="…" AISSTREAM_API_KEY="…" npm run dev -- --host localhost --port 4173

# On macOS, store any of them in the Keychain and dev-fresh.sh pulls them in:
...
```
### 💸 What it actually costs
Honest numbers, roughly, as of mid-2026 — always check the provider pricing pages: Google's direct 3D route is surprisingly generous: the first 1,000 Photoreali
| | Cost reality |
| **🟢 Most layers** | **$0, no signup.** OpenSky anon, USGS, CelesTrak, adsb.lol, city CCTV, Radio Browser, GBFS, Launch Library 2
| **🟡 The free-key tier** | **$0 with a signup.** AISStream, FIRMS, TomTom, OpenSky, plus Cesium ion for eligible personal/non-com
| **🗺️ Google 3D tiles** | **Free through an eligible Cesium ion Community account within its quota; metered through a direct Goog
| **🔴 OpenAI voice** | API-key sessions keep the live spend readout, STD/MINI model toggle, $2 warning, and **$5 hard cap**. ChatG
### 🧗 The floor is low on purpose
Everything above is the deliberately cheap baseline — enough to get a real taste of geospatial intelligence, GEOINT, and OSINT without ever talking to a sales t
### 🔒 Sharing an instance
By default nobody else can reach your server — it binds to localhost.
### 📋 Responsible & Open
God's Eye View runs on **public data, clear sources, and local-first execution.** No secrets, no private datasets, no mystery scraping — anything involving a pr
### 🧭 What's Next
First — thank you.

## Sentences with numbers (verbatim)
- _No place left behind._ ▶️ **From the project behind the viral God's Eye View series** _(formerly WorldView)_ — 5M+ on YouTube · 25M+ across socials 🏆 **Reached #1 on GitHub Trendi
- Version 8.2 fixes the launcher installation issue; details from the Pinokio maintainer.
- ### Path 2 — Terminal / coding agent Use **Node.js 24.x (24.14.0 or later) or 26.x**.
- The setup doctor warns about Node 25, which is end-of-life.
- The Pinokio 8.2 announcement fixes installation; it does not establish that this separate Configure issue is resolved.
- With TomTom, live flow speeds drive the simulation and congestion colors below ~8 km; individual vehicle positions are not live observations | TomTom + OSM | 🟢 simulation · 🟡 live 
- Mapillary first; Panoramax, KartaView and Google Street View planned | Mapillary | 🟡 Mapillary client token | | 📻 **Radio** | Geolocated world radio with an **analog tuner** — drag
- OSM takes over automatically if Esri is unreachable; if terrain is unavailable the globe continues without it | | 🟡 A free Cesium ion token | **Google Photorealistic 3D cities** an
- Share links carry the provider switches and filters (`0.m.0` Mapillary off, `0.p.p` panoramas only, `0.s.365` the last year).
- | | **🚀 Launch replay** | Open **Space Missions**, pick a launch from the last 30 days, and ride the T-minus countdown through ascent to orbit — scrub it at 0.25×–4×.
- | _🎙️ = voice missions — they need an OpenAI key._ _Ask the planet: a military contact's last ~24 hours of real trace history, resolved as stacked 3D loops._ _"Draw the walking rou
- - **Smooth motion from choppy data.** Live feeds arrive every 15–30s; the globe renders one interval behind real time and interpolates between known fixes.
- Each retains at most 12 segments and 24 MiB in memory; individual downloads are capped at 4 MiB with a ten second deadline.
- Closing it releases only that lease; abandoned leases expire after 15 seconds without access.
- ### 💸 What it actually costs Honest numbers, roughly, as of mid-2026 — always check the provider pricing pages: | | Cost reality | | ------------------------ | --------------------

## Page blocks (id kind y: text)
b000 header 172: gods-eye-view Public Notifications Fork10k (10k) Star49.5k (
b001 star 192: Star49.5k (49.5k)
b002 about 250: About A spy satellite simulator in your browser, except the 
b003 files 368: Name Last commit message Last commit date .agents/skills/com
b005 text 1719: 🌐 God's Eye View A spy-satellite simulator in your browser —
b008 text 1837: A spy-satellite simulator in your browser — then you realize
b009 text 1903: Photorealistic 3D globe. Live aircraft, ships, satellites, e
b010 text 1967: No place left behind.
b013 text 2754: ▶️ From the project behind the viral God's Eye View series (
b014 text 2818: 🏆 Reached #1 on GitHub Trending, daily and weekly · August 2
b015 text 2858: #8 Product of the Day · Hunted by Chris Messina, creator of 
b016 text 2898: “pretty cool” — Brendan Eich, creator of JavaScript and co-f
b017 text 2962: ⚡ Start without API keys. Install with Pinokio or run locall
b018 text 3059: Quick Start · First Five Minutes · Talk to It · What's Live 
b021 heading 3156: 🌍 Why This Exists
b023 text 3210: God's Eye View brings public signals into one explorable glo
b024 text 3274: Flight transponders, ship beacons, orbital elements, seismog
b025 quote 3386: Half the magic is that it looks like a forbidden cockpit. Th
b026 text 3450: Most feeds are live or regularly refreshed. Traffic is simul
b027 text 3514: Start with the included data sources, then add your own. Eac
b029 heading 3587: 🎛️ What This Thing Does
b031 list 3641: 🛩️ Cockpit view: Ride inside a tracked flight — the camera h
b032 text 4606: ▶️ The full walkthrough of everything below, on YouTube
b034 text 5101: ▶️ The full walkthrough of everything below, on YouTube
b036 heading 5149: ⚡ Quick Start
b038 text 5203: Start without an account or API keys. Both paths open the sa
b039 text 5291: For photorealistic 3D, add a Cesium ion token for eligible p
b040 quote 5379: Already installed? Update to the latest version. Older versi
b042 heading 5475: Path 1 — One click, no terminal
b044 list 5516: Install or update Pinokio to 8.2 or later. Open God's Eye Vi
b045 text 5612: Available on Windows, macOS, and Linux. The Pinokio maintain
b046 text 5700: Tried before and installation failed? Update Pinokio and try
b048 heading 5772: Path 2 — Terminal / coding agent
b050 text 5813: Use Node.js 24.x (24.14.0 or later) or 26.x. The setup docto
b051 code 5877: git clone https://github.com/bilawalsidhu/gods-eye-view.git 
b054 text 6023: Open http://localhost:4173. Choose Live Contacts, Space Miss
b056 text 6127: macOS shortcut: ./scripts/dev-fresh.sh clears the Vite cache
b058 heading 6199: Then power it up — in the app, not in a file
b060 text 6240: Keys are upgrades, not prerequisites. When you want one, cli
b061 list 6352: Where keys land: Pinokio → the app's ignored pinokio/ENVIRON
b062 text 6592: Older Pinokio versions and credential storage
b063 text 6632: The server binds to localhost on both paths, and Provider Se
b065 heading 6753: 🕐 The First Five Minutes
b067 text 6807: Choose a first-run mission, or try these in order. The GIFs 
b068 list 6871: Light up the sky. Take the Live Contacts mission (or turn on
b070 list 7484: Drop into a busy airport. Search one and descend to the taxi
b072 list 8021: Look through a public camera. Turn on Cameras over Austin, L
b074 list 8606: Track something in orbit. Turn on Satellites and click the I
b076 list 9143: Switch the optics. Tap 1–7 — CRT, NVG, FLIR — and the whole 
b078 list 9680: Talk to it (needs an OpenAI key): "Take me to LAX and select
b079 text 9748: Keyboard: 1–7 visual styles · H HUD · D detection · C cockpi
b081 heading 9845: 🛩️ The Cockpit
b083 quote 9900: Every plane should let you do this.
b084 text 9940: Real-time cockpit mode, built from live flight data: the cam
b086 text 10501: The cockpit even carries its own briefing strip: nearby live
b088 text 11099: Why cockpit mode exists: you're riding a real aircraft over 
b090 heading 11196: 🎙️ Talk to It
b092 quote 11250: Voice can use an OpenAI API key or, on the same machine, an 
b093 text 11386: The OAuth option is experimental. OpenAI documents ChatGPT p
b094 text 11474: GEV reads Codex's file credentials but does not write or ref
b095 text 11658: For a live voice check, run node scripts/qa-voice-auth.mjs h
b096 text 11794: Click GEV MIC, grant the microphone, and just talk. This is 
b097 list 11834: 🧠 It knows what it's looking at. The agent pulls live scene 
b098 text 12178: Thirty tools, four jobs — the commands below come straight f
b099 text 12242: 🎥 Direct it — drone-operator camera verbs:
b100 quote 12282: 🗣️ "Take me to Tokyo." · "Orbit around this area slowly." · 
b101 text 12346: 🖊️ Annotate it — a whiteboard over the real world:
b102 quote 12386: 🗣️ "Outline the state of Texas." · "Annotate the Texas State
b103 text 12498: ✍️ Or draw it yourself — DISPLAY ▸ Draw: pick Area, Line or 
b106 text 13508: 🔎 Interrogate it — analyst queries against the live layers:
b107 quote 13548: 🗣️ "How many flights are over Texas right now?" · "Which shi
b108 text 13636: 🎛️ Operate it — the whole console, hands-free:
b109 quote 13676: 🗣️ "Switch to night vision and turn on the flights layer." ·
b110 text 13740: And the rapid-fire tier — one sentence each:
b111 quote 13780: 🗣️ "Show me global infrastructure." (stages the layers and p
b113 text 14365: Ask for radio near anywhere and the globe starts broadcastin
b114 text 14462: 💬 Or ask from Claude and Codex. God's Eye View is also an MC
b116 heading 14558: 🛰️ What's on the Globe
b118 text 14612: Twenty layers and map sources. Seventeen have a keyless path
b119 table 14676: rows 0-20 (0 = header) Layer What you get Source Auth 🗺️ Map Stack Esri satellite i
b120 text 16982: Weather, keyless. Wind animates 10 m forecast flow from NOAA
b121 text 17118: In the app, Data Layers groups them as Movement, Cameras, In
b122 text 17182: The basemap ladder — what each tier buys you:
b123 table 17222: rows 0-3 (0 = header) You have The globe you get 🟢 Nothing Esri World Imagery sate
b125 text 17980: The Space Missions layer replaying a Falcon 9 ascent — label
b126 text 18044: Also on the globe: neighborhood overlays · an optional cockp
b128 text 18581: Missing a layer you want? Open an issue — or add it and send
b130 heading 18654: 📷 Street Level
b132 quote 18709: Street-level photos from any provider in one panel. This bui
b133 text 18773: Setup. At mapillary.com/dashboard/developers, register an ap
b134 text 18861: Use. Turn on Street Level under DATA LAYERS → Cameras, or wi
b135 text 19021: Drag the panel header to float the panel, and resize it from
b137 heading 19141: 🎖️ Field Missions
b139 text 19195: Once the basics click, run these:
b140 table 19235: rows 0-11 (0 = header) Mission How 🚁 Ask the planet "Why are all these military hel
b141 text 20080: 🎙️ = voice missions — they need an OpenAI key.
b143 text 20593: Ask the planet: a military contact's last ~24 hours of real 
b145 text 21106: "Draw the walking route… now fly it" — banked turns, eased e
b147 text 21643: Walk the boneyard: rows of retired airframes, fully resolved
b149 heading 21716: 🔧 Under the Hood
b151 text 21770: How the globe handles live data:
b152 list 21810: World-stable icons. Aircraft and ships point along their tru
b154 code 22282: src/ ├── main.js # Bootstrap: Google 3D tiles, layer registr
b156 text 22566: See docs/CURRENT-STATE.md for the authoritative runtime refe
b158 heading 22639: 🔑 API Keys
b160 text 22694: 🟢 No key · 🟡 Free key · 🔴 Metered
b161 text 22734: Use POWER UP → Provider Settings to add keys. The tables bel
b162 text 22798: No key needed for Wind, Rain radar, Satellite clouds, Lightn
b164 heading 22894: Choose the capabilities you want
b166 text 22935: Seven keys. Five have a free tier, and the two 🔴 ones are me
b167 table 22975: rows 0-7 (0 = header) Key Why Get it 🟡 Cesium ion 🗺️ Google Photorealistic 3D, wor
b169 text 24169: What the TomTom key buys you: rush-hour density painted on t
b171 heading 24241: Cherry on top
b173 table 24282: rows 0-2 (0 = header) Key Why Get it 🟡 OpenSky ✈️ More flight-polling credits (🟢 a
b174 text 24458: Add these if you need higher polling allowances.
b175 text 24498: npm run doctor reports Node/npm readiness, the primary provi
b176 text 24682: Advanced setup: environment variables and macOS Keychain
b177 text 24722: Live video cameras (HLS)
b179 heading 24770: 💸 What it actually costs
b181 text 24811: Honest numbers, roughly, as of mid-2026 — always check the p
b182 table 24851: rows 0-4 (0 = header) Cost reality 🟢 Most layers $0, no signup. OpenSky anon, USGS
b183 text 25293: Google's direct 3D route is surprisingly generous: the first
b185 heading 25437: 🧗 The floor is low on purpose
b187 text 25478: Everything above is the deliberately cheap baseline — enough
b189 heading 25646: 🔒 Sharing an instance
b191 text 25687: By default nobody else can reach your server — it binds to l
b192 text 25919: Provider Settings is disabled when the server is shared, so 
b193 text 25983: Pinokio LAN and Cloudflare sharing remain disabled for this 
b195 heading 26104: 📋 Responsible & Open
b197 text 26158: God's Eye View runs on public data, clear sources, and local
b198 text 26246: The line. This project models events, assets, infrastructure
b199 text 26358: Come build it. This is the canonical live 3D client from the
b200 text 26470: Status: An evolving open-source client for exploration and l
b201 text 26582: Maintainers: Bilawal Sidhu and Sameh Khamis at Halfpixel.
b202 text 26622: Media note: the capture GIFs on this page show Google Photor
b203 text 26686: Important God's Eye View is an exploratory visualization of 
b205 text 26726: God's Eye View is an exploratory visualization of public and
b207 heading 26879: 🧭 What's Next
b209 text 26933: First — thank you. To everyone who watched the God-view demo
b211 text 27321: So here it is. Step inside the spy-thriller cockpit — except
b212 text 27409: One heads-up from the inside: build in this space for a week
b213 text 27521: Update — a hosted version is coming. We originally planned t
b214 text 27690: ▶️ Watch the God's Eye View series · 📬 Map the World — the n
b215 text 27690: ▶️ Watch the God's Eye View series · 📬 Map the World — the n
b216 text 27730: 🌐 God's Eye View. No place left behind.
b217 media 2007: Orbital HUD, a tracked live globe, FLIR terrain — then OPEN 
b218 media 2480: The God's Eye View video series on YouTube
b219 media 4606: YouTube video about the God's Eye View open source release
b220 media 7011: Riding with a live aircraft in cockpit view while switching 
b221 media 7548: Moving from a full airport overhead down to close taxiway in
b222 media 8133: Diving into an Austin intersection with a live public camera
b223 media 8670: Tracking the ISS along its orbital path as it crosses over U
b224 media 9207: Cycling a dense live globe through CRT, FLIR, and NVG in one
b225 media 10028: Jumping between live aircraft and falling straight into a co
b226 media 10589: A live military contact ridden through Normal, NVG, and Iron
b227 media 12562: Zilker Park and Lady Bird Lake drawing onto the 3D city as p
b228 media 13035: A spoken distance measurement spanning an airport, inspected
b229 media 13892: The globe populating with the world's radio stations as anot
b230 media 17507: A reconstructed Falcon 9 ascent climbing and curving into it
b231 media 18108: Diving into the Bahamas and revealing labeled submarine cabl
b232 media 20120: Resolving a selected aircraft's recent flight path into stac
b233 media 20633: Asking for a walking route and flying the generated path thr
b234 media 21170: Descending from regional context into dense rows of retired 
b235 media 23696: Diving from city-scale live congestion straight into an inte
b236 media 27021: Community survey on open-sourcing God's Eye View

## Media
m00 block b217 animated 98f@12.01 800x450: Orbital HUD, a tracked live globe, FLIR terrain — then OPEN SOURCED
m01 block b218 still 2032x648: The God's Eye View video series on YouTube
m02 block b219 still 1280x720: YouTube video about the God's Eye View open source release
m03 block b220 animated 64f@7.99 800x450: Riding with a live aircraft in cockpit view while switching sensor modes
m04 block b221 animated 64f@12.01 800x450: Moving from a full airport overhead down to close taxiway inspection with 3D fli
m05 block b222 animated 56f@7.99 800x450: Diving into an Austin intersection with a live public camera projected into the 
m06 block b223 animated 61f@7.99 800x450: Tracking the ISS along its orbital path as it crosses over Ukraine
m07 block b224 animated 38f@7.98 800x450: Cycling a dense live globe through CRT, FLIR, and NVG in one continuous view
m08 block b225 animated 40f@7.98 800x450: Jumping between live aircraft and falling straight into a cockpit view
m09 block b226 animated 76f@12.5 918x534: A live military contact ridden through Normal, NVG, and Ironbow FLIR with dense 
m10 block b227 animated 52f@7.99 800x450: Zilker Park and Lady Bird Lake drawing onto the 3D city as persistent vector ann
m11 block b228 animated 52f@7.99 800x450: A spoken distance measurement spanning an airport, inspected from orbit
m12 block b229 animated 40f@7.98 800x450: The globe populating with the world's radio stations as another live layer
m13 block b230 animated 48f@7.99 800x450: A reconstructed Falcon 9 ascent climbing and curving into its projected orbit
m14 block b231 animated 41f@7.99 800x450: Diving into the Bahamas and revealing labeled submarine cable routes beneath the
m15 block b232 animated 36f@7.98 800x450: Resolving a selected aircraft's recent flight path into stacked 3D loops above t
m16 block b233 animated 40f@7.98 800x450: Asking for a walking route and flying the generated path through the 3D city
m17 block b234 animated 55f@7.99 800x450: Descending from regional context into dense rows of retired aircraft at the bone
m18 block b235 animated 48f@7.99 800x450: Diving from city-scale live congestion straight into an intersection's public ca
m19 block b236 still 1128x680: Community survey on open-sourcing God's Eye View