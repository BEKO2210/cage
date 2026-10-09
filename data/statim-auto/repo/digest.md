# BEKO2210/statim
Native C++20 engine for System-1 decision models — Laya/Jev-compatible, no Python, bit-exact parity
stars 1 · forks 0 · Python · licence Apache-2.0 · release v0.9.5 (2026-10-03) · pushed 2026-10-04 · topics 
languages {'Python': 66.3, 'C++': 20.8, 'HTML': 7.9, 'Shell': 1.1, 'CSS': 1.0}

## README by section
### (intro)
Watch the 60-second film Statim answers typed questions about text or JSON: pick one of several labels (`choice`), rate on a scale (`score`), or give a yes/no p
### At a glance
- CPU latency: **535 ms/state, multilingual**; **1,683 ms/state, English**.
| Measure | **Statim Decide Multilingual 0.7.0**, trained | **Qwen3-8B**, zero-shot |
| 14-category macro accuracy | **0.748** | 0.706 |
| Banking77 | **0.913** | 0.650 |
| Decisions/s, one RTX 3070 | **68** | ≈6 |
### Against ONNX Runtime on CPU
The comparison uses the same model and the same token ids on a Ryzen 7 5800X: Statim 0.9.2 against onnxruntime 1.30 (CPU execution provider).
| Measure | **Statim** | **ORT** |
| Short inputs, f32, 8 threads, ms per state | **257** | 266 |
| 1,024 tokens, f32, 8 threads, ms | **4,399** | 11,421 |
| Short inputs, f32, 16 threads (SMT), ms per state | 457 | **366** |
| First answer after process start, f32 | **0.45 s** | 2.06 s |
| Resident memory at start-up, 8-bit | **276 MiB** | 579–581 MiB |
|...
### On a public suite: S1Bench
On S1Bench (13 public subsets, 3,880 items, the harness Lev's authors used), the multilingual model 0.7.0 scores **0.638** macro, above its untuned Laya base (0
### Quick start
Linux x86-64 with AVX2 (Haswell or newer), CPU.
```
# 1. Download the engine (3 MB) and the multilingual model (357 MB), and verify both
curl -fLO https://github.com/BEKO2210/statim/releases/download/v0.9.5/statim-0.9.5-linux-x86_64-cpu.
curl -fLO https://github.com/BEKO2210/statim/releases/download/v0.9.5/SHA256SUMS
sha256sum -c --ignore-missing SHA256SUMS && tar -xzf statim-0.9.5-linux-x86_64-cpu.tar.gz
...
```
```
{"answers": {
  "department": {"type": "choice", "choice": "billing", "probabilities": {"billing": 0.9948, "techni
  "urgency": {"type": "score", "score": 1.585, "legend": {"0": "not urgent", "1": "soon", "2": "crit
  "refund": {"type": "noul", "noul": 0.9224}}}
```
### How it works
The state and all questions become one token sequence with a mask per option.
### Why Statim
- Runtime: Laya needs Python 3.10+, PyTorch, and transformers.
| Measure | Laya | Statim |
| Runtime | Python stack | 5.5 MB + `.gguf` |
| Answers | Reference | 240/240; within 1e-4 |
| Cold start to first answer | 11.35 s | **0.76 s** |
| Server memory | 3,915 MB | **650 MB** |
| HTTP throughput | 0.43 req/s | **1.07 req/s** |
### Models
Statim runs any Laya checkpoint.
| Model | Languages |
| statim-decide-en-large 0.5.0ModernBERT-large, 395M | English |
| statim-decide-multilingual-base 0.7.0mmBERT-base | 12 evaluated |
| Suite | English | Multilingual |
| typed-decisions | **0.768** | 0.763 |
| Banking77 | **0.928** | 0.914 |
|...
```
hf download Beko2210/statim-decide-en-large statim-decide-en-large-q8_0.gguf --local-dir models   # 
./statim serve -m english=models/statim-decide-en-large-q8_0.gguf
```
### API
The single-state response returns `model`, `answers`, `usage`, and `routing`.
| Endpoint | Purpose |
| `POST /v1/systemone` | Decide for one state |
| `POST /v1/systemone/batch` | Decide for many states |
| `GET /v1/models` | List loaded models and adapters |
| `GET /health`, `GET /ready` | Liveness and readiness. |
| `GET /metrics` | Prometheus metrics |
|...
### LoRA adapters
One base model can serve small per-category LoRA adapters selected by name or question family.
```
python tools/convert_lora.py runs/emotion-lora -o models/emotion.lora.gguf \
    --base models/laya-multilingual-q8_0.gguf --category emotion      # PEFT adapter -> GGUF
statim serve -m multilingual=models/laya-multilingual-q8_0.gguf \
    --adapter multilingual:emotion=models/emotion.lora.gguf
...
```
### Authentication, limits, and operations
Set `STATIM_API_KEY=key1,key2` or pass `--api-key-file FILE`.
### Client SDKs
The dependency-free Python and TypeScript clients retry `503` responses with backoff.
| Package | Path |
| Python `statim` | `clients/python` |
| TypeScript `@statim/client` | `clients/js` |
```
from statim import Client

client = Client("http://127.0.0.1:8080", timeout=120)
decision = client.decide(
...
```
### Performance
### CPU performance
Measured on an Intel Xeon E3-1505M v5 laptop CPU (4 cores, 8 threads, AVX2, turbo off, 31 GB RAM), using the f32 multilingual checkpoint and Laya 0.3.20 on PyTo
| Measure | Laya | Statim |
| In-process mean | 1,186 ms | **1,139 ms** |
| In-process p50 | 815 ms | **823 ms** |
| HTTP rate, 1 client | 0.43 req/s | **1.07 req/s** |
| HTTP p50, 1 client | 1,718 ms | **889 ms** |
| HTTP p95, 1 client | 4,994 ms | **1,280 ms** |
|...
### GPU performance
GPU build and launch instructions are in docs/BUILD.md.
| Path | CPU | RTX 3070 | Gain |
| Multilingual state | 535 ms | **54 ms** | ~10× |
| English state | 1,683 ms | **137 ms** | ~12× |
| Multilingual rate1 client | 2.68 req/s | **20.5 req/s** | 7.7× |
| Multilingual p501 client | 353 ms | **45 ms** | — |
| English rate1 client | 0.91 req/s | **8.1 req/s** | 8.9× |
|...
```
./build-vk/statim serve --device vulkan -m english=models/laya-english-f32.gguf \
  --batch-window-ms 2 --max-batch 16
```
### Results
### Trained Statim versus zero-shot general models
Every system receives the same 11,550 held-out items, questions, and options: 37 language cells with 150 items each across 14 categories, plus the first 2,000 t
| Measure | Statim | Qwen3-8B | NLI |
| Parameters | 307M | 8.2B | 279M |
| 14-category macro accuracy | **0.748** | 0.706 | 0.488 |
| Categories won | **9** | 5 | 0 |
| Banking77 | **0.913** | 0.650 | 0.224 |
| AG News | **0.929** | 0.847 | 0.581 |
|...
### Published model gates
Published models must pass validation, held-out-suite, and pooled-family promotion gates before replacing their base.
| Suite | English 0.5.0 | Multilingual 0.7.0 |
| typed-decisions | 0.768 | 0.763 |
| Banking77 | 0.928 | 0.914 |
| MASSIVE | 0.867 English | 0.800 / 12 languages |
| HWU64 (English only) | 0.833 | — |
| AG News (never trained) | 0.939 | 0.9295 |
|...
### Security and robustness
Statim applies bearer authentication, bounded parsing and inference budgets, admission control, deadlines, fixed error responses, and load-time model validation
```
python3 tests/security/test_http.py --binary build/statim --model models/laya-multilingual-f32.gguf
```
### Platform support
Only what CI builds and tests, or what was run on real hardware, is listed as supported.
| Platform | Release binary | CI | Tested on hardware |
| Linux x86-64, CPU (AVX2, FMA, F16C, BMI2) | yes; glibc 2.28 or newer (0.9.5 and earlier: 2.38) | build, full `ctest`, ASan + UBS
| Linux x86-64, Vulkan | yes | builds in the release job only; no GPU runner | RTX 3070, driver 580.159.03: the four `*_vulkan` pa
| Linux x86-64, CUDA | no; build from source | no | RTX 3070, CUDA 12.8: the four `*_cuda` parity tests pass (2026-10-01) |
| x86-64 without AVX2 | no; the release binaries stop with a message naming the missing features | `cpu_check` test | Core i5-2520
| Android arm64 (NEON, dotprod) | no; build from source with the NDK (BUILD.md) | cross-build | Galaxy A15 (Dimensity 6100+) and G
|...
### Status and roadmap
The current release is v0.9.5: Linux x86-64 binaries for CPU and Vulkan, CUDA from source (see platform support), two published models, client SDKs, and a publi
### Licence
- Source code—engine, server, and tools—is Apache-2.0, free for any use.

## Sentences with numbers (verbatim)
- Statim runs Laya checkpoints and implements the Jev/Laya `POST /v1/systemone` protocol, so existing clients can switch by changing the base URL.
- - **Live demo**: in the browser, no install, no key - **Models on Hugging Face**: English, multilingual, and three category adapters - **Ticket triage example**: a complete applica
- RTX 3070: 54 ms and 137 ms.
- Full results - Speed: Statim Vulkan f32 reached 68 decisions/s (11.6 ms/decision) in batches of 16 on one RTX 3070.
- Qwen3-8B reached ≈6 decisions/s through Ollama Q4_K_M with 2 parallel requests; mDeBERTa-v3 XNLI used CUDA f32 and reached 4 decisions/s.
- Measurements - CPU latency: Ryzen 7 5800X, 16 threads, f32, 30 states × 8 questions, and up to 770 tokens.
- ORT is called from Python, which adds at most 0.02 % to a run.
- | Measure | **Statim** | **ORT** | |---|---:|---:| | Short inputs, f32, 8 threads, ms per state | **257** | 266 | | 1,024 tokens, f32, 8 threads, ms | **4,399** | 11,421 | | Short 
- Full protocol and every row ### On a public suite: S1Bench On S1Bench (13 public subsets, 3,880 items, the harness Lev's authors used), the multilingual model 0.7.0 scores **0.638*
- ## Why Statim | Measure | Laya | Statim | |---|---|---| | Runtime | Python stack | 5.5 MB + `.gguf` | | Answers | Reference | 240/240; within 1e-4 | | Cold start to first answer | 
- Statim uses one 5.5 MB binary and one `.gguf` file.
- - Answers: the comparison covers 240/240 token sequences; answers are within 1e-4 of the reference, which is one step of the 4-decimal rounding both use.
- Statim's native C++ tokenizer is identical on 3,906 cases plus 140k fuzz strings and about 10× faster.
- | Model | Languages | |---|---:| | statim-decide-en-large 0.5.0ModernBERT-large, 395M | English | | statim-decide-multilingual-base 0.7.0mmBERT-base | 12 evaluated | Files: f32 1.5
- ## API | Endpoint | Purpose | |---|---| | `POST /v1/systemone` | Decide for one state | | `POST /v1/systemone/batch` | Decide for many states | | `GET /v1/models` | List loaded mod
- Requests retain base latency; each adapter owns a copy of the adapted weights, 438 MB for the multilingual f32 model.
- A rank-4 adapter uses 3.3 MB and adds 17–28 % CPU latency.
- Merging the test adapter into q4_0 loses 91 % of its effect.

## Page blocks (id kind y: text)
b000 header 72: BEKO2210 / statim Public Notifications Fork 0 Star 1 Code Is
b001 star 88: Star 1
b011 list 2636: Live demo: in the browser, no install, no key Models on Hugg
b016 text 3953: Measure Statim Decide Multilingual 0.7.0, trained Qwen3-8B, 
b017 list 4166: CPU latency: 535 ms/state, multilingual; 1,683 ms/state, Eng
b019 list 4298: Accuracy: the same 11,550 held-out items, questions, and opt
b025 text 4743: Measure Statim ORT Short inputs, f32, 8 threads, ms per stat
b036 code 5530: # 1. Download the engine (3 MB) and the multilingual model (
b040 code 6052: {"answers": { "department": {"type": "choice", "choice": "bi
b053 text 7134: Measure Laya Statim Runtime Python stack 5.5 MB + .gguf Answ
b054 list 7373: Runtime: Laya needs Python 3.10+, PyTorch, and transformers.
b064 code 8404: hf download Beko2210/statim-decide-en-large statim-decide-en
b078 code 9182: python tools/convert_lora.py runs/emotion-lora -o models/emo
b082 list 9441: f32, f16, and bf16 default to merging W + B·A at load. Reque
b095 code 10295: from statim import Client client = Client("http://127.0.0.1:
b105 text 10719: Measured on an Intel Xeon E3-1505M v5 laptop CPU (4 cores, 8
b106 text 10831: Measure Laya Statim In-process mean 1,186 ms 1,139 ms In-pro
b108 list 11369: One client: Laya's 0.43 req/s used 4 threads. Statim reached
b121 code 13149: ./build-vk/statim serve --device vulkan -m english=models/la
b132 text 13572: Measure Statim Qwen3-8B NLI Parameters 307M 8.2B 279M 14-cat
b147 code 14779: python3 tests/security/test_http.py --binary build/statim --
b164 list 16262: Source code—engine, server, and tools—is Apache-2.0, free fo
b166 media 1799: Statim
b167 media 1942: Statim in ten seconds: a support ticket in JSON becomes thre
b168 media 2850: Statim against ONNX Runtime and the Laya PyTorch reference o
b169 media 6369: State and questions become one token sequence with a [MASK] 
b170 media 12392: RTX 3070 vs. Ryzen 7 5800X: 7.7x (multilingual) and 8.9x (En

## Media
m00 block b166 still NonexNone: Statim
m01 block b167 animated 250f@25.0 540x960: Statim in ten seconds: a support ticket in JSON becomes three typed decisions, d
m02 block b168 still NonexNone: Statim against ONNX Runtime and the Laya PyTorch reference on one CPU (speed, st
m03 block b169 still NonexNone: State and questions become one token sequence with a [MASK] per option; one forw
m04 block b170 still NonexNone: RTX 3070 vs. Ryzen 7 5800X: 7.7x (multilingual) and 8.9x (English) HTTP throughp