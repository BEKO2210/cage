# JuliusBrussee/caveman
🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.
stars 110358 · forks 6386 · Go · licence Apache-2.0 · release v3.1.0 (2026-10-04) · pushed 2026-10-07 · topics ai, anthropic, caveman, claude, claude-code, llm, meme, prompt-engineering
languages {'Go': 45.5, 'JavaScript': 27.0, 'TypeScript': 15.2, 'Python': 11.3, 'Shell': 0.3}

## README by section
### (intro)
### why many token when few do trick
**Caveman make your AI agent say less and read less.
| Skill | Same answer | Tokens |
| `/caveman` | New object ref each render, so React re-renders. Wrap the prop in `useMemo`. | 20 |
| `/ultracave` | Inline object prop, new ref, re-render. `useMemo`. | 14 |
| `/megacave` | 新參照致重繪。`useMemo`。 | **13** |
### How caveman talks
Caveman is a voice, not broken grammar.
| Rule | What it means |
| **Answer first** | `[thing] [action] [reason]. [next step].` No greeting, no "let me", no recap, no "hope this helps" |
| **One idea per sentence** | Built on ASD-STE100, the controlled English written for aircraft maintenance manuals: 20 words max, 
| **Meaning never dropped** | Articles can go. *not*, *never*, *no*, *only* never go. Numbers and units stay exact |
| **Payload verbatim** | Code, commands, paths, and error messages untouched, character for character |
| **Quiet tool runs** | No chatter between tool calls. One line per phase, one line with the result |
|...
### Install
Works in Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Cline, Copilot, and 30+ more.
```
npx skills add JuliusBrussee/caveman -g
```
```
# Claude Code plugin, auto-starts every session
claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman

# Gemini CLI
...
```
### The numbers
Outside labs first, then ours.
| Who | Setup | Result |
| **Adobe Research**, CAVEWOMAN paper (cites this repo) | Caveman-style output, eight models, five datasets | **Cost cut 1.4 to 2.
| **Elastic**, Elasticsearch Labs | Caveman mode remade for Elasticsearch, eight live MCP scenarios | **63.6% fewer response token
| **JetBrains** | 86 real coding tasks, paired A/B | **No measurable quality loss** (p = 0.82). 8.5% fewer output tokens |
### The proxy: 33.2% fewer input tokens
**18 of 18 answers right.** *The file* is each benchmark file run through today's compressor on its own.
| File type | The file, through caveman | File saved | Whole Claude Code session, 3 runs | Session saved |
| CSV | 28,041 → **314** | **98.9%** | 165,823 → 74,484 | **55.1%** |
| Logs | 22,810 → **348** | **98.5%** | 148,807 → 74,068 | **50.2%** |
| YAML | 20,447 → **178** | **99.1%** | 132,124 → 71,027 | **46.2%** |
| Test output | 18,806 → **203** | **98.9%** | 150,377 → 108,514 | **27.8%** |
| JSON | 18,837 → **281** | **98.5%** | 147,975 → 108,939 | **26.4%** |
|...
### The skill: ten dev questions on claude-opus-5-5
New models already know "be concise", so that line is the real baseline.
| Instruction | Output tokens |
| None | 6,983 |
| `Answer concisely.` | 4,334 |
| `/caveman` | 4,119 |
| `/ultracave` | **2,693** |
### Everything else
The rules add about 1,000 input tokens to every call.
| What | Result |
| A web page the agent reads (`caveman browse`, 200-row table) | **121 tokens instead of 15,704** for a Playwright snapshot, 129.8
| Memory files like `CLAUDE.md` (`/caveman-compress`) | **46% smaller** across five fixtures, with every heading, code block, and 
### Big rock: the proxy
**Logs, CSV, YAML, JSON, and test output come out 98.5% to 99.1% smaller.
```
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude        # or codex · gemini · aider · kilo · qwen · opencode · hermes · openclaw · pi
```
```
caveman learn                 # rank where your tokens go, from agent history already on disk
caveman learn implement       # apply the fixes one diff at a time, only on your yes
caveman trial -- claude       # A/B a real session on your own work
caveman shrink -- pnpm test   # compress noisy command output
...
```
### What you get
| Command | What it does |
| `/caveman` · `/ultracave` · `/megacave` | The voice, the grunt, the 文言文. `/caveman status` shows the mode, `/caveman off` stops 
| `/caveman-commit` | One-line Conventional Commit |
| `/caveman-review` | One finding per line: `L42: 🔴 null deref. Guard it.` |
| `/caveman-compress ` | Shrinks memory files and backs up the original |
| `/caveman-stats` | Real token usage for this Claude Code session |
|...
### In the wild
**ThePrimeagen**: *"No way this actually works."* Watch **Adobe Research**: CAVEWOMAN, arXiv, June 2026 **JetBrains**: *"It is fun, and it costs you nothing mea
### Privacy
The skill runs on your machine and sends nothing.
### License
Apache-2.0, whole repo.
### Cite
--- 🪨 **Caveman save you token.
```
@software{brussee2026caveman,
  author = {Brussee, Julius},
  title  = {Caveman: why many token when few do trick},
  year   = {2026},
...
```

## Sentences with numbers (verbatim)
- Brain still big.** 33.2% fewerinput tokens through the proxy54 Claude Code runs, 18 of 18 answers right 129.8× smallerweb pages for the agentcaveman browse vs a Playwright snapshot
- 63 token become 20.
- | 14 | | `/megacave` | 新參照致重繪。`useMemo`。 | **13** | Token counts: tiktoken o200k.
- | Who | Setup | Result | |---|---|---| | **Adobe Research**, CAVEWOMAN paper (cites this repo) | Caveman-style output, eight models, five datasets | **Cost cut 1.4 to 2.4× per mode
- 8.5% fewer output tokens | Two findings shaped caveman.
- ### The proxy: 33.2% fewer input tokens | File type | The file, through caveman | File saved | Whole Claude Code session, 3 runs | Session saved | |---|---:|---:|---:|---:| | CSV |
- The session run is from August 2026, on an engine that only got the JSON file down to 8,106 tokens.
- Headroom on the same suite got 15 of 18 right and used 6.7% fewer tokens on those 15.
- On top of it, `/caveman` cuts 3% more at the median and `/ultracave` cuts 35% more.
- Harness ### Everything else | What | Result | |---|---| | A web page the agent reads (`caveman browse`, 200-row table) | **121 tokens instead of 15,704** for a Playwright snapshot,
- Tiny forms lose 2.3×.
- Bench | | Memory files like `CLAUDE.md` (`/caveman-compress`) | **46% smaller** across five fixtures, with every heading, code block, and path intact.
- ## Big rock: the proxy **Logs, CSV, YAML, JSON, and test output come out 98.5% to 99.1% smaller.
- Whole sessions use 33.2% fewer input tokens, same answers.** (benchmark) The skill shrinks what the agent **says**.

## Page blocks (id kind y: text)
b000 header 172: caveman Public Sponsor Notifications Fork6.4k (6.4k) Star110
b001 star 192: Star110k (110k)
b002 about 250: About 🪨 why use many token when few token do trick. Viral sk
b003 files 368: Name Last commit message Last commit date .claude-plugin cho
b005 text 2720: why many token when few do trick Caveman make your AI agent 
b007 text 2967: why many token when few do trick
b008 text 3034: Caveman make your AI agent say less and read less. Code stay
b010 table 3117: rows 0-0 (0 = header) 33.2% fewer input tokens through the proxy 54 Claude Code ru
b011 text 3308: Cited by Adobe Research · A/B tested by JetBrains · Remade f
b012 text 3396: How it talks · Install · The numbers · The proxy · What you 
b013 table 3469: rows 0-1 (0 = header) Normal agent · 63 tokens Caveman agent · 20 tokens The reaso
b014 text 3729: Same fix. 63 token become 20. Brain still big.
b016 table 3809: rows 0-3 (0 = header) Skill Same answer Tokens /caveman New object ref each render
b017 text 3998: Token counts: tiktoken o200k.
b019 heading 4046: How caveman talks
b021 text 4100: Caveman is a voice, not broken grammar. Every reply follows 
b022 table 4140: rows 0-8 (0 = header) Rule What it means Answer first [thing] [action] [reason]. [
b023 text 4658: Every reply runs a check before it sends: opener that announ
b025 heading 4730: Install
b027 code 4784: npx skills add JuliusBrussee/caveman -g
b030 text 4852: Works in Claude Code, Codex, Gemini CLI, Cursor, Windsurf, C
b031 text 4916: Other ways in: Claude Code plugin, Gemini, every agent at on
b033 heading 4964: The numbers
b035 text 5018: Outside labs first, then ours. Nothing rounded up. Red rows 
b036 table 5058: rows 0-3 (0 = header) Who Setup Result Adobe Research, CAVEWOMAN paper (cites this
b037 text 5367: Two findings shaped caveman. Adobe found that cavemanning yo
b039 heading 5487: The proxy: 33.2% fewer input tokens
b041 table 5528: rows 0-7 (0 = header) File type The file, through caveman File saved Whole Claude 
b042 text 5889: 18 of 18 answers right. The file is each benchmark file run 
b044 heading 6057: The skill: ten dev questions on claude-opus-5-5
b046 table 6098: rows 0-4 (0 = header) Instruction Output tokens None 6,983 Answer concisely. 4,334
b047 text 6300: New models already know "be concise", so that line is the re
b049 heading 6372: Everything else
b051 table 6413: rows 0-2 (0 = header) What Result A web page the agent reads (caveman browse, 200-
b052 text 6589: The rules add about 1,000 input tokens to every call. If you
b054 heading 6685: Big rock: the proxy
b056 text 6739: Logs, CSV, YAML, JSON, and test output come out 98.5% to 99.
b057 text 6803: The skill shrinks what the agent says. The proxy shrinks wha
b058 code 6891: npm install -g @caveman-ai/cli && caveman setup --install ca
b062 code 7019: caveman learn # rank where your tokens go, from agent histor
b066 text 7766: Building your own agent? Same shrinking, as one wrapper arou
b067 code 7830: npm install @caveman-ai/middleware @caveman-ai/sdk # TypeScr
b070 text 7918: TypeScript guide · Python guide · Every framework · One cont
b072 heading 7966: What you get
b074 table 8020: rows 0-9 (0 = header) Command What it does /caveman · /ultracave · /megacave The v
b076 heading 8655: In the wild
b078 text 8709: ThePrimeagen: "No way this actually works." Watch
b079 text 8749: Adobe Research: CAVEWOMAN, arXiv, June 2026
b080 text 8789: JetBrains: "It is fun, and it costs you nothing measurable i
b081 text 8853: Elastic: elastic-caveman on Elasticsearch Labs, April 2026
b082 text 8893: Hacker News: #1, 904 points
b083 text 8933: GitHub Trending #1 overall, July 2026 · Trendshift #1 repo o
b084 text 8997: Started as a joke in April 2026. Now past 100,000 stars. Jok
b088 heading 9748: Privacy
b090 text 9802: The skill runs on your machine and sends nothing. The cavema
b092 heading 9922: License
b094 text 9976: Apache-2.0, whole repo. Read it, fork it, ship it, host it. 
b096 heading 10048: Cite
b098 code 10102: @software{brussee2026caveman, author = {Brussee, Julius}, ti
b101 text 10301: 🪨 Caveman save you token. Star cost zero. Fair trade. Docs ·
b102 text 10301: 🪨 Caveman save you token. Star cost zero. Fair trade.
b104 media 2720: Caveman
b105 media 7205: Caveman Learn report: a summary and savings cards on the lef
b106 media 8709: ThePrimeagen reacts to Caveman: No way this actually works
b107 media 9061: Star History Chart

## Media
m00 block b104 still 1200x360: Caveman
m01 block b105 still 1254x806: Caveman Learn report: a summary and savings cards on the left; the biggest place
m02 block b106 still 480x360: ThePrimeagen reacts to Caveman: No way this actually works
m03 block b107 still 3152x2466: Star History Chart