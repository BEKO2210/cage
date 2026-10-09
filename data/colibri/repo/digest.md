# JustVugg/colibri
Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦
stars 40719 · forks 4472 · C · licence Apache-2.0 · release v2.0.0 (2026-10-06) · pushed 2026-10-08 · topics 
languages {'C': 54.6, 'Python': 33.5, 'Shell': 3.7, 'Cuda': 3.7, 'TypeScript': 1.4}

## README by section
### (intro)
Website · Discord · English · 简体中文 · 繁體中文 · Italiano · 日本語 · Bahasa Indonesia **Tiny engine, immense model.** colibri runs very large open models on the machine
```
$ ./coli chat
  colibri v2.0.0 · GLM-5.2 · 744B MoE · int4 · streaming CPU
  ✓ ready in 32s · resident 9.9 GB
  › ciao!
...
```
### Get started in one step
You need a computer with **8 GB of RAM** at the very least (16 GB or more is better), **22 GB free on the disk** for the smallest model, and an internet connect
| Option | What it does |
| `--list` | every model against this machine, and why one does not fit |
| `--model ID` | install that model (the ids are in the tables below) |
| `--yes` | no questions: take the recommendation |
| `--dir DIR` | put the models on another disk (default `~/colibri-models`) |
| `--backend vulkan`, `cuda` or `cpu` | choose the engine build yourself; `--no-gpu` is `--backend cpu` |
|...
```
sudo apt install git python3 build-essential
git clone https://github.com/JustVugg/colibri
cd colibri
./start-here.sh
```
```
xcode-select --install
brew install libomp git python
git clone https://github.com/JustVugg/colibri
cd colibri
...
```
### If something goes wrong
| What you see | What to do |
| it stopped during the download | run the same command again: it resumes from the bytes already on disk |
| `to use the GPU through ..., first run: ` | run that command, then the setup again: it rebuilds for the GPU and does not downloa
| `the ... build failed`, for example `Unsupported gpu architecture` when the installed CUDA toolkit no longer supports the card |
| `needs N GB free for the download` | `--dir` with a folder on a bigger disk |
| on WSL, the model folder is under `/mnt/c` | keep it on the Linux disk (the default, `~/colibri-models`): `/mnt/c` is many times
|...
### Let your AI assistant set it up
If you use an AI coding assistant, it can do all of this for you.
### Or by hand
To choose each step yourself (a prebuilt release or a source build, any model from the tables below, then `coli chat`, `coli web` or `coli serve`), see Install 
### What colibri is, and why
A mixture-of-experts model is huge on disk and small per token.
### Which model for my machine
The setup recommends the most capable model that runs from RAM on your machine, and lists the larger ones that stream from the disk right below it.
| Model | `--model` | Download | RAM | GPU | Measured |
| **Qwen3.6-35B-A3B**: chat with thinking and tools | `qwen36-35b` | 23 GB | 10 / 20 GB | CUDA, Vulkan (integrated too) | 6.0 tok/
| Qwen3-Coder-30B-A3B: code and tool calls, no thinking | `qwen3-coder-30b` | 19 GB | 8 / 18 GB | CUDA, Vulkan (integrated too) | 
| **Qwen-Image-2.1**: text to picture, non-commercial licence | `qwen-image-2.1` | 33 GB | 12 / 18 GB | Vulkan | one 768x512 pictu
| Model | `--model` | Download | RAM | GPU | Measured |
| DeepSeek V4 Flash REAP 150B: 132 of the 256 experts | `deepseek-v4-flash-reap` | 85 GB | 16 / 32 GB | CUDA, Vulkan | |
|...
### GPUs
### No GPU needed
Every engine runs on the CPU with nothing else installed.
### Vulkan: any GPU
Every MoE engine can use any GPU with a Vulkan 1.2 driver (AMD, Intel, NVIDIA, integrated or discrete) in two ways: - **the expert tier**: a cache of routed exp
| | CPU | Vulkan, expert tier | Vulkan, tier and dense chain |
| Qwen3.6-35B-A3B, decode | 6.0 tok/s | 8.0 tok/s | **9.9 tok/s** |
| Qwen3.6-35B-A3B, a 512-token prompt | 35.7 s | 12.2 s | **9.5 s** |
| Qwen3.8-Flash-Next (int4 experts), decode | 3.5 tok/s | **3.8 tok/s** | 3.2 tok/s |
| Qwen3.8-Flash-Next, a 512-token prompt | 43.6 s | 38.7 s | **30.1 s** |
| OLMoE, decode (warm) | **23.1 tok/s** | 12.8 tok/s | 17.3 tok/s |
### CUDA: NVIDIA cards
The setup builds CUDA on Linux when the CUDA toolkit is installed, for the engines that have a CUDA path: GLM-5.2/5.3, GLM-5.3-Flash, Inkling, Kimi K3, DeepSeek
### Apple Silicon
A Metal backend does the expert math on the unified-memory GPU for several engines (docs/metal.md).
### System One: a decision with a probability
Most of what people ask a model for is a choice, not a paragraph: which queue, which verdict, yes or no.
```
curl -s http://127.0.0.1:8000/v1/systemone -H 'Content-Type: application/json' -d '{
  "state": "340 lines, 8 files, no tests. CI is green but nothing covers that path.",
  "questions": {
    "review": {"type": "choice", "instructions": "What should the reviewer do?",
...
```
### The dashboard
`coli web` opens it, and so does the one-step setup: the chat, the System One page, the Brain and the Profiling page, in a light or a dark theme.
### Use it from other apps
`coli serve` (which the setup starts for you) is one server with several APIs: - **OpenAI-compatible**: `/v1/chat/completions`, `/v1/completions` and `/v1/model
### How it works
Every layer of every token walks the same five steps: route, union, place, overlap, learn.
### Benchmarks
The same engine and the same int4 container: the hardware only changes where the experts live.
### Install by hand
**1.
```
git clone https://github.com/JustVugg/colibri && cd colibri/c
./setup.sh                                # checks gcc/OpenMP, builds, self-tests
make qwen36 VK=1                          # one engine, here with Vulkan (CUDA=1 for CUDA)
```
```
./coli chat  --model /nvme/qwen36          # chat in the terminal
./coli web   --model /nvme/qwen36          # API + dashboard, opens a browser
./coli serve --model /nvme/qwen36          # API + dashboard, no browser
./coli plan  --model /nvme/qwen36          # where the model will live: VRAM, RAM, disk
...
```
### Research, and how to help
colibri wants frontier models to depend less on scarce hardware and to cost less to run.
| hypothesis | evidence so far | experiment still needed |
| Routing history can place experts better than plain LRU | learned pins improve repeated workloads, but can overfit a prompt | he
| Multiple SSDs can turn independent bandwidth into decode speed | two independent NVMe drives measured +37.5% decode; a slower th
| A hardware-aware planner can approach each machine's best configuration automatically | RAM/VRAM budgets and several backends ar
| Lossless or quality-bounded representations can reduce weight movement enough to matter | format and quantization ablations exis
| Routing-aware speculation can pay before near-full residency | MTP and grammar drafts work, but MTP has also measured a 32% loss
|...
### Documentation
| topic | doc |
| The one-step setup and the manual install, every platform | quickstart.md |
| Setting up through an AI assistant, and the MCP server | AI_SETUP.md, MCP_SERVER.md |
| The API: OpenAI, Anthropic, tools, KV slots, dashboard | api.md |
| System One and the decision models | systemone.md, laya.md, gliner_decide.md, clef.md |
| Vulkan: the expert tier, the dense chain, cards without Resizable BAR | vulkan.md |
|...
### Repo layout
**One `.c` per model family, over shared single headers.** An engine owns its architecture and nothing else; anything two engines both need lives in a header th
```
start-here.sh, START-HERE.bat   the one-step setup (Linux and macOS, Windows)
Makefile                        root build/check entry point
c/
├── colibri.c             GLM-5.2/5.3 engine  (make glm)
...
```
### Supporting the project
colibri started as a one-person project on a 12-core laptop with 25 GB of RAM; today its numbers come from a community of real machines.
### Why "colibrì"
The hummingbird weighs a few grams, hovers in place, and visits a thousand flowers a day.
### Acknowledgements
colibri is an engine; the minds it runs are a gift.
### License
Apache 2.0, Copyright 2026 Vincenzo Fornaro.

## Sentences with numbers (verbatim)
- Ten are for language models: **GLM-5.2/5.3**, **GLM-5.3-Flash**, **Inkling**, **Kimi K3**, **DeepSeek V4 Flash**, **DeepSeek V4.1 Flash**, **MiMo-V2.6 Flash** (and Pro), **Qwen3.8-
- Which one for my machine ## Get started in one step You need a computer with **8 GB of RAM** at the very least (16 GB or more is better), **22 GB free on the disk** for the smalles
- GLM-5.2 has 744B parameters, uses about 40B for each token, and only about 11 GB of those change from one token to the next: the routed experts.
- **Small models, which run from RAM** | Model | `--model` | Download | RAM | GPU | Measured | |---|---|---|---|---|---| | **Qwen3.6-35B-A3B**: chat with thinking and tools | `qwen36
- Each family has its page: qwen36.md (Qwen3.6, Qwen3-Coder, Qwen3.8-27B), qwen38.md, deepseek-v4.md, deepseek-v41.md, mimo.md, glm53-flash.md, inkling.md, kimi_k3.md, qwen-image.md,
- Measured on the integrated Radeon 780M of machine A, the model files dropped from the page cache before each run, 100 tokens decoded (vulkan.md): | | CPU | Vulkan, expert tier | Vu
- That is why the setup turns Vulkan on for an integrated GPU only for Qwen3.6, Qwen3-Coder and Qwen3.8-Flash-Next, and why each engine decides for itself whether to run the dense ch
- On an integrated GPU, try both: on a laptop with an Intel Iris Xe (Core i7-1355U), Qwen3.6 decoded 2.1 tok/s on the CPU, 1.7 to 1.9 with Vulkan, and 2.1 with the dense chain off.
- **We have not measured a discrete GPU ourselves yet.** The first number comes from a user: Qwen3.6 at 17 to 19 tok/s on a Tesla V100 16 GB, with the expert tier and the dense chain
- (Before them, GLM-5.2's earlier Vulkan path decoded 1.7-1.8 tok/s on a discrete RX 9070.) Numbers from your card are welcome.
- Such a card (every Turing card, Ampere cards on their launch firmware, older AMD cards with the option off) lets the CPU write only about 256 MB of its memory directly; colibri now
- The path is tested by forcing it and by emulating the small window on three devices, and it costs nothing measurable on the 780M; it has not been measured on a card without Resizab
- On Windows the CUDA engine is a separate DLL (windows.md), and every release ships it built: `colibri--windows-x86_64-cuda.zip` has `coli_cuda.dll` (cards of compute capability 8.0
- Qwen3.6 on two 8 GB cards (RTX 3070 and Quadro RTX 4000) decoded 11.3 tok/s with a warm history (qwen36-cuda-tier.md); GLM-5.2 on six RTX 5090 with every expert resident, 9.0-9.2 t
- On an RTX 3070 with the dense layers in VRAM: 25.4 to 30.0 tok/s (qwen36-cuda-tier.md).
- - **Older cards.** If the CUDA toolkit no longer compiles for your card (CUDA 13 and a V100, in #1852), the setup sees it before building and uses the card through Vulkan, saying w
- `POST /v1/systemone` takes a state (text or JSON) and typed questions, and answers each one with the probability of every allowed option and a confidence.
- Many questions about one document read the document once: on Qwen3.6, four questions about one document came back 5.7x faster than generating the same answers on the same CPU box.

## Page blocks (id kind y: text)
b000 header 172: colibri Public Notifications Fork4.5k (4.5k) Star40.7k (40.7
b001 star 192: Star40.7k (40.7k)
b002 about 250: About Run frontier MoE models on hardware you already own — 
b003 files 368: Name Last commit message Last commit date .github Merge remo
b007 text 1993: Website · Discord · English · 简体中文 · 繁體中文 · Italiano · 日本語 ·
b008 text 2033: Tiny engine, immense model. colibri runs very large open mod
b009 text 2145: Thirteen engines run today. Ten are for language models: GLM
b011 code 2281: $ ./coli chat colibri v2.0.0 · GLM-5.2 · 744B MoE · int4 · s
b014 heading 2435: Get started in one step
b016 text 2489: You need a computer with 8 GB of RAM at the very least (16 G
b018 list 2593: On this page click Code, then Download ZIP, and unzip it. Do
b019 text 2661: Linux (Ubuntu and Debian; other distributions have the same 
b020 code 2701: sudo apt install git python3 build-essential git clone https
b023 text 2828: macOS (with Homebrew)
b024 code 2868: xcode-select --install brew install libomp git python git cl
b027 text 3015: You answer one question, which model, and Enter takes the re
b028 list 3055: looks at your machine: RAM, free disk, CPU and GPUs; recomme
b030 code 3423: Starting colibri Browser: http://127.0.0.1:8000/ OpenAI base
b032 text 3569: Next time, run START-HERE.bat or ./start-here.sh again: coli
b033 text 3657: Options go after ./start-here.sh or START-HERE.bat:
b034 table 3697: rows 0-7 (0 = header) Option What it does --list every model against this machine,
b035 text 4010: What each step does, in detail: docs/quickstart.md.
b037 heading 4058: If something goes wrong
b039 table 4099: rows 0-7 (0 = header) What you see What to do it stopped during the download run t
b041 heading 4660: Let your AI assistant set it up
b043 text 4701: If you use an AI coding assistant, it can do all of this for
b044 quote 4741: Set up colibri on this machine following docs/AI_SETUP.md fr
b045 text 4781: docs/AI_SETUP.md gives the assistant every step as a command
b047 heading 4901: Or by hand
b049 text 4942: To choose each step yourself (a prebuilt release or a source
b051 heading 5038: What colibri is, and why
b053 text 5092: A mixture-of-experts model is huge on disk and small per tok
b055 text 5387: So the model does not have to fit in fast memory; it has to 
b056 text 5523: Why: to run models of this size on hardware people already o
b058 heading 5691: Which model for my machine
b060 text 5745: The setup recommends the most capable model that runs from R
b061 list 5857: RAM is two numbers: below the first the model does not start
b062 text 6025: Small models, which run from RAM
b063 table 6065: rows 0-3 (0 = header) Model --model Download RAM GPU Measured Qwen3.6-35B-A3B: cha
b064 text 6446: Large models, whose experts stream from the disk (the disk s
b065 table 6510: rows 0-9 (0 = header) Model --model Download RAM GPU Measured DeepSeek V4 Flash RE
b066 text 7737: By hand: a conversion or preparation step after the download
b067 table 7777: rows 0-4 (0 = header) Model Download, then on disk RAM GPU Measured OLMoE (7B): sm
b068 text 8267: Decision models (they answer System One questions, they do n
b069 table 8307: rows 0-3 (0 = header) Model Download, then on disk RAM GPU Measured Laya (Convai I
b070 text 8640: The machines: A a Ryzen 7 PRO 8700GE desktop (8 cores, 61-64
b071 text 8752: Each family has its page: qwen36.md (Qwen3.6, Qwen3-Coder, Q
b073 heading 8872: GPUs
b076 heading 8934: No GPU needed
b078 text 8975: Every engine runs on the CPU with nothing else installed. A 
b080 heading 9047: Vulkan: any GPU
b082 text 9088: Every MoE engine can use any GPU with a Vulkan 1.2 driver (A
b083 list 9152: the expert tier: a cache of routed experts in GPU memory, fi
b084 text 9292: Measured on the integrated Radeon 780M of machine A, the mod
b085 table 9356: rows 0-5 (0 = header) CPU Vulkan, expert tier Vulkan, tier and dense chain Qwen3.6
b086 text 9715: An integrated GPU shares the CPU's RAM. What it saves is the
b087 text 9851: Turning the GPU on or off. coli setup --backend vulkan uses 
b088 text 10035: On a discrete GPU the setup builds Vulkan for every engine (
b089 text 10195: Cards without Resizable BAR now work. Such a card (every Tur
b090 text 10331: CI checks every engine's Vulkan path against the CPU's token
b092 heading 10427: CUDA: NVIDIA cards
b094 text 10468: The setup builds CUDA on Linux when the CUDA toolkit is inst
b095 list 10628: The VRAM expert tier keeps the hottest experts on the card, 
b096 text 10964: All of it: docs/cuda.md.
b098 heading 11012: Apple Silicon
b100 text 11053: A Metal backend does the expert math on the unified-memory G
b102 heading 11173: System One: a decision with a probability
b104 text 11227: Most of what people ask a model for is a choice, not a parag
b105 code 11339: curl -s http://127.0.0.1:8000/v1/systemone -H 'Content-Type:
b108 text 11506: A choice comes back with the chosen label, a probability for
b110 list 11610: Any chat model colibri runs, by scoring: it reads the probab
b111 text 11798: Switching from Jev. The request and the reply are those of T
b112 text 11910: The same mode is in the terminal (/decide merge | request ch
b114 heading 12006: The dashboard
b116 text 12060: coli web opens it, and so does the one-step setup: the chat,
b118 text 12644: Qwen3.6 answering on a CPU box, experts streamed from disk.
b120 text 13205: System One: give the model a document and the only answers i
b122 text 13789: The Brain: the measured expert atlas of GLM-5.2, 13,260 char
b123 text 13901: The Profiling page shows where each turn spends its time, ph
b125 heading 13973: Use it from other apps
b127 text 14028: coli serve (which the setup starts for you) is one server wi
b128 list 14068: OpenAI-compatible: /v1/chat/completions, /v1/completions and
b129 text 14396: Coding CLIs and editors connect as to any OpenAI-compatible 
b131 heading 14468: How it works
b134 text 14800: Every layer of every token walks the same five steps: route,
b136 list 15237: A JIT for weights. A compiler JIT never compiles the whole p
b137 text 15873: The engine is one C file per model family (c/colibri.c for G
b139 heading 15969: Benchmarks
b142 text 16374: The same engine and the same int4 container: the hardware on
b143 list 16438: 6x RTX 5090, every expert resident: 5.8-6.8 tok/s, 9.0-9.2 w
b144 text 16586: Quality is measured, not assumed: the int4 container's cost 
b146 heading 16682: Install by hand
b148 text 16736: 1. The program. Take the archive for your platform from Rele
b149 code 16872: git clone https://github.com/JustVugg/colibri && cd colibri/
b152 text 16979: 2. A model. Any download in the tables above: the setup's id
b153 text 17187: 3. Run it. From c/ in a source checkout, or from the unpacke
b154 code 17275: ./coli chat --model /nvme/qwen36 # chat in the terminal ./co
b157 text 17442: On Windows a release archive ships coli.cmd (coli.cmd chat -
b159 heading 17538: Research, and how to help
b161 text 17592: colibri wants frontier models to depend less on scarce hardw
b162 table 17728: rows 0-6 (0 = header) hypothesis evidence so far experiment still needed Routing h
b163 text 18532: Want to help? Pick a row and publish the negative results to
b165 heading 18676: Documentation
b167 table 18730: rows 0-12 (0 = header) topic doc The one-step setup and the manual install, every p
b169 heading 19380: Repo layout
b172 code 19434: start-here.sh, START-HERE.bat the one-step setup (Linux and 
b174 text 20251: One .c per model family, over shared single headers. An engi
b176 heading 20371: Supporting the project
b178 text 20425: colibri started as a one-person project on a 12-core laptop 
b179 list 20489: star the repository and share it; open issues with benchmark
b181 heading 20645: Why "colibrì"
b183 text 20699: The hummingbird weighs a few grams, hovers in place, and vis
b185 heading 20795: Acknowledgements
b187 text 20849: colibri is an engine; the minds it runs are a gift. Thank yo
b188 text 21009: The project's expert placement, compression, and routing exp
b189 list 21073: REAP and EASY-EP for output-aware and domain-specific expert
b190 text 21301: The engine also stands on concrete engineering work, not onl
b191 list 21365: safetensors: the container every engine reads (c/st.h), incl
b193 heading 21677: License
b195 text 21731: Apache 2.0, Copyright 2026 Vincenzo Fornaro. See LICENSE and
b196 media 1818: colibrì: tiny engine, immense model
b197 media 5180: only about 5.4% of parameters are active per token
b198 media 12124: the colibri web dashboard: chat, live metrics, hardware pane
b199 media 12684: the System One page: a document read once, a probability for
b200 media 13269: the Brain page: the measured expert atlas of GLM-5.2 drawn a
b201 media 14522: route, union, place, overlap, learn
b202 media 14888: VRAM, RAM and NVMe as three tiers of expert residency
b203 media 16023: measured GLM-5.2 decode speed by hardware class

## Media
m00 block b196 still NonexNone: colibrì: tiny engine, immense model
m01 block b197 still 1884x412: only about 5.4% of parameters are active per token
m02 block b198 still 3200x1900: the colibri web dashboard: chat, live metrics, hardware panel, expert tiers
m03 block b199 still 3200x1900: the System One page: a document read once, a probability for every allowed answe
m04 block b200 still 3200x1900: the Brain page: the measured expert atlas of GLM-5.2 drawn as a cortex, ten regi
m05 block b201 still 1884x574: route, union, place, overlap, learn
m06 block b202 still 1884x732: VRAM, RAM and NVMe as three tiers of expert residency
m07 block b203 still 1884x738: measured GLM-5.2 decode speed by hardware class