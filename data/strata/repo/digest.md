# Niko1221/Strata
Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Strata inference engine, OpenAI/Anthropic API on localhost, optional image input.
stars 16905 · forks 1481 · C++ · licence MIT · release v0.1.40.3 (2026-10-07) · pushed 2026-10-07 · topics 
languages {'C++': 69.3, 'Python': 18.6, 'Cuda': 10.1, 'CMake': 0.8, 'JavaScript': 0.4}

## README by section
### (intro)
Strata **English** · 简体中文 · 日本語 · Deutsch · Français · Español · Português Run a 125-billion-parameter AI model on your own gaming PC NVIDIA or AMD graphics car
### How fast is it?
We measured it on two ordinary gaming PCs.
| Size | Writes answers | Reads your prompt |
| **Q2_0** | 94 tokens/s | 2,650 tokens/s |
| **IQ2_XS** | 79 tokens/s | 2,090 tokens/s |
| **IQ3_XXS** | 62 tokens/s | 1,750 tokens/s |
| **IQ3_S** | 53 tokens/s | 1,620 tokens/s |
| **Coder** | 55 tokens/s | 2,180 tokens/s |
|...
### What you need
The installer sets up everything else.
| **Graphics card** | **NVIDIA** GeForce RTX 20, 30, 40 or 50 series, or **AMD** Radeon RX 7900 XT / XTX, RX 7800 XT / 7700 XT, RX
| **RAM** | 32 GB or more. Your RAM decides which model fits. 64 GB runs every size. |
| **Disk** | About 80 GB free. Use an SSD if you can: the first start is much faster. |
| **System** | Windows 10 / 11 or Linux, and a current graphics driver from NVIDIA or AMD. |
### Install
### Let your AI set it up
Do you use an AI coding assistant (Claude Code, Cursor, Codex, GitHub Copilot, ...)?
```
Set up Strata on this PC for me: https://github.com/Niko1221/Strata - follow docs/AI_SETUP.md in tha
```
### Or do it yourself
Download Strata and unzip it (or `git clone` it).
### Which model should I pick?
The installer recommends one for your RAM.
| Your RAM | Take | Why |
| **32 GB** | **Coder** | it fits 32 GB, and it is made for code (with a 24 GB card, Q2_0 and IQ2_XS run too) |
| **48 GB** | **IQ2_XS** (or Q2_0, the fastest) | the larger sizes do not fit |
| **64 GB** | **IQ2_XS** (recommended), or IQ3_XXS / IQ3_S | every size fits; IQ3_S is the best and the slowest |
| **96 GB or more** | **IQ3_S**, or Unsloth's UD-IQ4_XS (~4-bit) | room for the largest sizes with everything else open |
### Using it
The Strata app's Monitor (left) while a coding agent writes the pagoda garden from the video (right) - **In the browser:** open `http://127.0.0.1:8080`.
### Something went wrong?
- **My PC froze the first time Strata started.** This is normal while it loads the model.
### How does it work?
Models like this one usually run on servers with hundreds of gigabytes of graphics memory.
### Credits and license
The model is Qwen3.8-Flash-Next by the Qwen team.
### Support Strata
Strata is free and open source.

## Sentences with numbers (verbatim)
- Strata **English** · 简体中文 · 日本語 · Deutsch · Français · Español · Português Run a 125-billion-parameter AI model on your own gaming PC NVIDIA or AMD graphics card (12 GB or more) · 
- 60 tokens per second is faster than you can read.
- NVIDIA: RTX 5070 (12 GB), Ryzen 5 7600, 64 GB RAMAMD: RX 9070 XT (16 GB), Ryzen 9 3900X, 47 GB RAM | Size | Writes answers | Reads your prompt | | --- | ---: | ---: | | **Q2_0** | 
- A card with more VRAM is faster: an RTX 3090 (24 GB) should write about 100-140 tokens per second.
- ## What you need | | | | --- | --- | | **Graphics card** | **NVIDIA** GeForce RTX 20, 30, 40 or 50 series, or **AMD** Radeon RX 7900 XT / XTX, RX 7800 XT / 7700 XT, RX 9060 XT, RX 
- It needs **12 GB of VRAM or more**.
- | | **RAM** | 32 GB or more.
- 64 GB runs every size.
- | | **Disk** | About 80 GB free.
- Then it downloads the model (about 70 GB) and starts it.
- > **While the model starts, your PC can be slow or stop responding for 1-3 minutes** (longest the first time).
- > Strata loads 35-55 GB into your RAM and locks part of it for the graphics card.
- | Your RAM | Take | Why | | --- | --- | --- | | **32 GB** | **Coder** | it fits 32 GB, and it is made for code (with a 24 GB card, Q2_0 and IQ2_XS run too) | | **48 GB** | **IQ2_XS
- It reaches 91% of the full model's SWE-bench Verified score (measured by its authors) and fits 32 GB of RAM.
- A 94 GB download.
- With less than ~80 GB of RAM, Strata reads part of it from the SSD while it answers, so it is slower there (an NVMe SSD helps).
- But Strata reads most of it from the SSD while it answers, so it writes only 7-8.5 tokens/s on a 64 GB PC.
- On a 12 GB card this makes each answer slower.

## Page blocks (id kind y: text)
b000 header 172: Strata Public Notifications Fork1.5k (1.5k) Star16.9k (16.9k
b001 star 192: Star16.9k (16.9k)
b002 about 250: About Qwen3.8-Flash-Next on any consumer hardware: one-click
b003 files 368: Name Last commit message Last commit date .github chore(gith
b006 heading 1982: Strata
b008 text 2049: English · 简体中文 · 日本語 · Deutsch · Français · Español · Portug
b009 text 2089: Run a 125-billion-parameter AI model on your own gaming PC N
b010 text 2153: A voxel pagoda garden, 1 shot prompt running on an RTX 5070 
b011 text 2614: Strata runs Qwen3.8-Flash-Next on a normal PC. This is a lar
b013 heading 2710: How fast is it?
b015 text 2764: We measured it on two ordinary gaming PCs. A token is about 
b016 list 2804: Writes answers: how fast the reply appears in a short chat. 
b017 table 2920: rows 0-11 (0 = header) NVIDIA: RTX 5070 (12 GB), Ryzen 5 7600, 64 GB RAM AMD: RX 90
b018 text 3234: NVIDIA: Q2_0 with engine 0.1.36, the other rows with 0.1.26 
b019 text 3322: Strata is free. If it runs well on your PC, a coffee keeps t
b021 heading 3427: What you need
b023 table 3481: rows 0-4 (0 = header) Graphics card NVIDIA GeForce RTX 20, 30, 40 or 50 series, or
b024 text 3707: The installer sets up everything else. Two or three cards ca
b025 text 3747: Experimental, written and tested by community members on the
b026 list 3787: Older graphics cards (Tesla P40 / V100, GTX 10, Radeon VII /
b027 text 3935: The full list: docs/INSTALL.md.
b029 heading 3983: Install
b032 heading 4045: Let your AI set it up
b034 text 4086: Do you use an AI coding assistant (Claude Code, Cursor, Code
b036 code 4126: Set up Strata on this PC for me: https://github.com/Niko1221
b038 text 4194: It checks your graphics card, RAM and disk and picks the mod
b040 heading 4290: Or do it yourself
b042 text 4331: Download Strata and unzip it (or git clone it). Windows: dou
b043 text 4395: The steps are the same for NVIDIA and AMD. The installer fin
b044 list 4459: which model and which size, how much context (how much text 
b045 text 4555: Press Enter each time for the recommended answer. Then it do
b046 quote 4643: While the model starts, your PC can be slow or stop respondi
b047 text 4731: Next time, run START-HERE.bat (or ./setup.sh) again. It star
b049 heading 4827: Which model should I pick?
b051 text 4881: The installer recommends one for your RAM. The same model co
b052 table 4945: rows 0-4 (0 = header) Your RAM Take Why 32 GB Coder it fits 32 GB, and it is made 
b053 list 5219: Coder: a coding version with half of the experts removed. It
b054 text 5539: Sizes, downloads and what fits where: docs/MODELS.md. To add
b056 heading 5611: Using it
b058 text 5665: The Strata app's Monitor (left) while a coding agent writes 
b059 list 6184: In the browser: open http://127.0.0.1:8080. It has Chat, a l
b060 text 6660: More: where your chats are stored, the API.
b062 heading 6708: Something went wrong?
b064 list 6762: My PC froze the first time Strata started. This is normal wh
b065 text 7006: More problems and their fixes: docs/TROUBLESHOOTING.md. Stil
b067 heading 7078: How does it work?
b069 text 7132: Models like this one usually run on servers with hundreds of
b071 list 7653: The model is a team of 24,576 small specialists ("experts").
b073 list 8104: Guess, then check: a small helper guesses the next few words
b074 text 8220: The longer explanation: docs/HOW_IT_WORKS.md. Every part and
b076 heading 8292: Credits and license
b078 text 8347: The model is Qwen3.8-Flash-Next by the Qwen team. It was com
b080 heading 8443: Support Strata
b082 text 8497: Strata is free and open source. If it is useful to you, you 
b084 media 2153: A voxel pagoda garden that Strata's model wrote, running in 
b085 media 5665: The Strata app's Monitor tab next to a coding agent
b086 media 7220: The model's 24,576 experts: the busiest on the graphics card
b087 media 7793: A small helper guesses the next words; the big model checks 

## Media
m00 block b084 animated 300f@12.02 720x414: A voxel pagoda garden that Strata's model wrote, running in the browser
m01 block b085 still 2560x1440: The Strata app's Monitor tab next to a coding agent
m02 block b086 still NonexNone: The model's 24,576 experts: the busiest on the graphics card, all of them in RAM
m03 block b087 still NonexNone: A small helper guesses the next words; the big model checks them all at once and