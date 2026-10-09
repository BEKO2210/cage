# antirez/ds4
DeepSeek 4 Flash and PRO local inference engine for Metal, CUDA and ROCm
stars 23731 · forks 2290 · C · licence MIT · release None () · pushed 2026-10-08 · topics 
languages {'C': 46.9, 'Cuda': 25.4, 'Objective-C': 12.2, 'Metal': 7.1, 'Python': 5.1}

## README by section
### (intro)
**DwarfStar** aims to be the best way to run a few excellent large language models on consumer hardware (that is, hardware that people can actually own).
### Supported hardware
* **Metal**, the primary target, on Macs with 96 GB or more.
### So, what can I do with this software?
* You can run a very capable models in your consumer hardware, a MacBook, a DGX Spark, or a Strix Halo for example.
### Motivations
* Capable open-weight models now fit on high-end personal machines.
### AI full disclosure
* This software is developed with **strong assistance from AI coding agents** and with humans leading the ideas, testing, and debugging.
### Acknowledgements to llama.cpp and GGML
`ds4.c` does not link against GGML, but it **exists thanks to the path opened by the llama.cpp project and the kernels, quantization formats, GGUF ecosystem, an
### Status
The software is currently very fast changing.
### How to use this project?
I (Salvatore) believe that the way projects should be shipped and used changed because of AI.
### Start Here
Choose your build.
| Platform guide | Build |
| Metal on Apple Silicon | `make` |
| DGX Spark | `make cuda-spark` |
| Strix Halo / Framework Desktop | `make strix-halo` |
| One or more CUDA cards, including Ada/L40S | `make cuda-generic` |
```
git clone https://github.com/antirez/ds4.git
cd ds4
```
```
./download_model.sh ds4f-q2
```
### Everyday Use
Once built and with a model downloaded: The default model is `ds4flash.gguf`, a link updated by main-model downloads.
```
./ds4
./ds4 -p "Explain Redis streams in one paragraph."
./ds4-agent
./ds4-server --ctx 32768
```
### Native coding agent
`ds4-agent` runs inference directly, without a separate HTTP server.
| Command | Action |
| `/save` | Save the current session |
| `/list` | List saved sessions |
| `/switch ` | Resume a session |
| `/del ` | Delete a saved session |
| `/strip ` | Keep text and title, removing the large KV payload |
### Models, images, and speculation
Models and vision lists the supported downloads and memory requirements.
```
./download_model.sh qwen38-q2
./ds4 --ctx 8192 --prefill-chunk 1024
```
### Output and power
Thinking is enabled by default.
### Capability Evaluation
`ds4-eval` runs embedded capability regression tests against a real GGUF.
```
./ds4-eval -m ds4flash.gguf --trace /tmp/ds4-eval.txt
./ds4-eval -m ds4flash.gguf --suite hard-smoke
./ds4-eval -m ds4flash.gguf --suite hard --retry-incomplete
```
### Speed
This recorded DeepSeek V4 Flash Q2 sweep uses an M5 Max with 128 GB RAM, 2048-token continued-prefill intervals, and 128 greedy generation tokens per frontier.
### Detailed Guides
- Models and vision: Flash, PRO, GLM, Qwen, and matching encoders.
### Logo
The DwarfStar logo was designed by hand by Salvatore Sanfilippo, made more graphical with AI, and manually reworked by Ben Gnomino, whose human touch made it ro

## Sentences with numbers (verbatim)
- ## Supported hardware * **Metal**, the primary target, on Macs with 96 GB or more.
- SSD streaming is also needed in order to run very large models such as full GLM 5.x (not Flash) on 128GB systems.
- The project follows the best open weights for useful local machine sizes, especially 128 GB laptops and 256/512 GB workstations.
- Our eight-L40S Flash setup has reached about 126 t/s aggregate generation with 16 sessions.
- * Using two 128 GB Macs connected with RDMA, you can run 4-bit DeepSeek Flash or GLM 5.3 Flash with tensor parallelism.
- Larger GLM 5.2 quants need larger machines, such as Mac Studios.
- The platform guides cover prerequisites, memory sizing, and hardware-specific setups: | Platform guide | Build | | --- | --- | | Metal on Apple Silicon | `make` | | DGX Spark | `ma
- Q2 runs with SSD streaming on one 128 GB Mac or Spark, or resident across two Macs or two Sparks using RDMA.
- Q4 needs SSD streaming or a 512 GB Mac.
- Qwen3.8's smaller Q2 release has **41.73 GiB** of main/MTP weights, with imatrix IQ2_XXS gate/up experts and padded Q2_K down projections.
- It is the starting option for 64 GB Macs.
- The GGUF also contains 95.37 GiB of original BF16 n-grams, read directly from disk rather than loaded into RAM.
- The larger `qwen38-q4k` target is also available.
- For V4.1, `ds4` and `ds4-agent` also accept `--think-level 25` or `/think 25`: 1 to 100 sets the reasoning effort, and 0 disables thinking.
- ## Speed This recorded DeepSeek V4 Flash Q2 sweep uses an M5 Max with 128 GB RAM, 2048-token continued-prefill intervals, and 128 greedy generation tokens per frontier.

## Page blocks (id kind y: text)
b000 header 172: ds4 Public Notifications Fork2.3k (2.3k) Star23.7k (23.7k)
b001 star 192: Star23.7k (23.7k)
b002 about 250: About DeepSeek 4 Flash and PRO local inference engine for Me
b003 files 368: Name Last commit message Last commit date cuda/mmq Document 
b006 text 4109: DwarfStar aims to be the best way to run a few excellent lar
b007 text 4293: We test things in integration: model loading, prompt renderi
b009 heading 4389: Supported hardware
b011 list 4443: Metal, the primary target, on Macs with 96 GB or more. Small
b012 text 4635: This project would not exist without llama.cpp and GGML, mak
b013 text 4699: Model support is intentionally opportunistic. The project fo
b015 heading 4795: So, what can I do with this software?
b017 list 4862: You can run a very capable models in your consumer hardware,
b019 heading 5162: Motivations
b021 list 5216: Capable open-weight models now fit on high-end personal mach
b023 heading 5348: AI full disclosure
b025 list 5415: This software is developed with strong assistance from AI co
b027 heading 5559: Acknowledgements to llama.cpp and GGML
b029 text 5613: ds4.c does not link against GGML, but it exists thanks to th
b031 heading 5805: Status
b033 text 5859: The software is currently very fast changing. Consider it be
b035 heading 5931: How to use this project?
b037 text 5998: I (Salvatore) believe that the way projects should be shippe
b038 list 6062: With AI, users can modify the software in significant ways w
b039 text 6298: So, while this project attempts to be usable for the feature
b041 heading 6442: Start Here
b043 code 6496: git clone https://github.com/antirez/ds4.git cd ds4
b046 text 6583: Choose your build. The platform guides cover prerequisites, 
b047 table 6647: rows 0-4 (0 = header) Platform guide Build Metal on Apple Silicon make DGX Spark m
b048 text 6849: For a first run on a 96 or 128 GB machine, download DeepSeek
b049 code 6889: ./download_model.sh ds4f-q2
b052 text 6957: Downloads go in gguf/. Repeat the command to resume an inter
b054 heading 7053: Everyday Use
b056 text 7107: Once built and with a model downloaded:
b057 code 7147: ./ds4 ./ds4 -p "Explain Redis streams in one paragraph." ./d
b060 text 7274: The default model is ds4flash.gguf, a link updated by main-m
b061 text 7362: The server listens at http://127.0.0.1:8000 by default; see 
b062 text 7426: The interactive CLI keeps a multi-turn conversation. Use /he
b064 heading 7498: Native coding agent
b066 text 7539: ds4-agent runs inference directly, without a separate HTTP s
b067 text 7627: Use /hints on for occasional, brief explanations of the prog
b068 text 7715: Sessions are stored in ~/.ds4/kvcache:
b069 table 7755: rows 0-5 (0 = header) Command Action /save Save the current session /list List sav
b070 text 7994: Compatible local KV snapshots avoid rebuilding the prompt. S
b071 text 8082: For Pi, OpenCode, Codex CLI, or Claude Code, use ds4-server 
b073 heading 8130: Models, images, and speculation
b075 text 8171: Models and vision lists the supported downloads and memory r
b076 text 8259: DeepSeek V4.1 Flash text and vision run on Metal; text also 
b077 text 8371: With the matching encoder passed as --vision FILE, use /read
b078 text 8435: Qwen3.8's smaller Q2 release has 41.73 GiB of main/MTP weigh
b079 code 8547: ./download_model.sh qwen38-q2 ./ds4 --ctx 8192 --prefill-chu
b082 text 8635: The download fetches one 137.10 GiB file and updates ds4flas
b083 text 8723: Speculative decoding is opt-in. GLM and Qwen use --mtp; V4 F
b085 heading 8819: Output and power
b087 text 8860: Thinking is enabled by default. Use --nothink or /nothink fo
b088 text 8996: For DeepSeek V4, --power N trades throughput for lower susta
b089 text 9060: DeepSeek V4 Flash and GLM 5.3 Flash also support directional
b090 text 9148: --prefix-file FILE preloads complete USER: / ASSISTANT: pair
b092 heading 9220: Capability Evaluation
b094 text 9274: ds4-eval runs embedded capability regression tests against a
b095 code 9338: ./ds4-eval -m ds4flash.gguf --trace /tmp/ds4-eval.txt ./ds4-
b098 text 9445: The default suite is core; --suite all runs core and hard ca
b100 heading 9565: Speed
b102 text 9619: This recorded DeepSeek V4 Flash Q2 sweep uses an M5 Max with
b104 text 10202: See performance and benchmarking for the full numbers, DGX S
b106 heading 10274: Detailed Guides
b108 list 10328: Models and vision: Flash, PRO, GLM, Qwen, and matching encod
b109 text 10592: Read CONTRIBUTING.md before sending a pull request.
b111 heading 10640: Logo
b113 text 10694: The DwarfStar logo was designed by hand by Salvatore Sanfili
b114 media 3909: DwarfStar logo
b115 media 9707: M5 Max Flash Q2 throughput

## Media
m00 block b114 still NonexNone: DwarfStar logo
m01 block b115 still NonexNone: M5 Max Flash Q2 throughput