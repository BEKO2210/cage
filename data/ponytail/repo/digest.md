# DietrichGebert/ponytail
Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
stars 155947 · forks 8373 · JavaScript · licence MIT · release v4.13.0 (2026-10-05) · pushed 2026-10-05 · topics agent-skills, ai-agents, claude, claude-code, claude-code-plugin, cursor-rules, developer-tools, llm
languages {'JavaScript': 70.2, 'Python': 29.4, 'PowerShell': 0.2, 'Shell': 0.2}

## README by section
### (intro)
Ponytail He says nothing.
### Already built with Ponytail
--- You know him.
### The prompt
Ponytail is one prompt: `skills/ponytail/SKILL.md`.
### Install
**Claude Code**, as two separate prompts: **Codex:** Then open `/hooks` in Codex, trust its two lifecycle hooks, and start a new thread.
```
/plugin marketplace add DietrichGebert/ponytail
```
```
/plugin install ponytail@ponytail
```
### Before / after
You ask for a date picker.
```

<input type="date">
```
### How it works
Before writing code, the agent stops at the first rung that holds: The ladder runs *after* it understands the problem, not instead of it: it reads the code the 
```
1. Does this need to exist?   → no: skip it (YAGNI)
2. Already in this codebase?  → reuse it, don't rewrite
3. Stdlib does it?            → use it
4. Native platform feature?   → use it
...
```
### Commands
Commands need a skill-capable host (Claude Code, Codex, Devin CLI, OpenCode, Gemini, pi, Hermes Agent, Qoder, Grok Build).
| Command | What it does |
| `/ponytail [lite \| full \| ultra \| off]` | Set the intensity, or turn it off. No argument switches ponytail on at the default 
| `/ponytail-review` | Review the current diff for over-engineering, hands back a delete-list. Name a target in plain words to nar
| `/ponytail-audit` | Audit the whole repo for over-engineering, not just the diff. |
| `/ponytail-debt` | Harvest the `ponytail:` shortcuts you've deferred into a ledger, so "later" doesn't become "never". |
| `/ponytail-gain` | Show the measured impact scoreboard (less code, less cost, more speed) from the benchmark. |
|...
### Numbers
The honest measurement is a real agent doing real work: a headless Claude Code session editing tiangolo's full-stack-fastapi-template (a real FastAPI + React re
| vs no-skill baseline | LOC | tokens | cost | time | safe |
| **ponytail** | **-54%** | **-22%** | **-20%** | **-27%** | **100%** |
| caveman (terse-prose control) | -20% | +7% | +3% | +2% | 100% |
| "YAGNI + one-liners" prompt | -33% | -14% | -21% | -30% | 95% |
### FAQ
**Can I use it with caveman?** Yes, and you should.
### Sponsors
### License
MIT.
### Star History

## Sentences with numbers (verbatim)
- ~54% less code (up to 94%) &middot; ~20% cheaper &middot; ~27% faster &middot; 100% safe Real Claude Code sessions editing a real FastAPI + React repo, the same agent with and with
- | vs no-skill baseline | LOC | tokens | cost | time | safe | |---|--:|--:|--:|--:|--:| | **ponytail** | **-54%** | **-22%** | **-20%** | **-27%** | **100%** | | caveman (terse-pros
- One prompt, one completion, counting lines of the answer: This showed **80-94% less code**.
- Zero bugs, zero CVEs, 100% uptime since forever.

## Page blocks (id kind y: text)
b000 header 72: DietrichGebert / ponytail Public Sponsor Notifications Fork 
b001 star 88: Star 156k
b002 files 307: Name Last commit message Last commit date .agents fix: narro
b006 heading 2246: Ponytail
b008 text 2312: He says nothing. He writes one line. It works.
b012 text 2551: ~54% less code (up to 94%) · ~20% cheaper · ~27% faster · 10
b013 text 2639: Español · 한국어 · 简体中文 · 日本語
b016 heading 2981: Already built with Ponytail
b019 text 3219: You know him. Long ponytail. Oval glasses. Has been at the c
b020 text 3283: Ponytail puts him inside your AI agent.
b022 heading 3331: The prompt
b024 text 3385: Ponytail is one prompt: skills/ponytail/SKILL.md. The compac
b026 heading 3457: Install
b028 text 3511: Claude Code, as two separate prompts:
b030 code 3551: /plugin marketplace add DietrichGebert/ponytail
b033 code 3619: /plugin install ponytail@ponytail
b036 code 3727: codex plugin marketplace add DietrichGebert/ponytail codex p
b039 text 3814: Then open /hooks in Codex, trust its two lifecycle hooks, an
b040 text 3854: Any other agent: copy AGENTS.md into your project, or ask yo
b041 text 3942: That was it. He'd be proud. He won't say it.
b042 text 3982: Active every session, with a handful of commands (see Comman
b043 text 4046: Only install ponytail from DietrichGebert/ponytail on GitHub
b045 heading 4118: Before / after
b047 text 4172: You ask for a date picker. Your agent installs flatpickr, wr
b049 code 4276: <!-- ponytail: browser has one --> <input type="date">
b052 text 4364: More survivors in examples/.
b054 heading 4412: How it works
b056 text 4466: Before writing code, the agent stops at the first rung that 
b058 code 4506: 1. Does this need to exist? → no: skip it (YAGNI) 2. Already
b060 text 4692: The ladder runs after it understands the problem, not instea
b061 text 4756: Lazy, not negligent: trust-boundary validation, data-loss ha
b063 heading 4828: Commands
b065 table 4882: rows 0-6 (0 = header) Command What it does /ponytail [lite | full | ultra | off] S
b066 text 5278: Commands need a skill-capable host (Claude Code, Codex, Devi
b068 heading 5422: Numbers
b070 text 5476: The honest measurement is a real agent doing real work: a he
b072 table 6063: rows 0-3 (0 = header) vs no-skill baseline LOC tokens cost time safe ponytail -54%
b073 text 6228: ponytail is the only arm that cuts every metric, and the onl
b074 text 6340: Older single-shot numbers (isolated generation)
b075 text 6380: The rule was never "fewest tokens." It is: write only what t
b077 heading 6500: FAQ
b079 text 6554: Can I use it with caveman? Yes, and you should. Caveman shri
b080 text 6642: Does it need a config file? No. An optional ~/.config/ponyta
b081 text 6706: What if I really need the 120-line cache class? You don't. I
b082 text 6770: Does it scale? The code you never wrote scales infinitely. Z
b083 text 6834: Why "ponytail"? You know exactly why.
b085 heading 6882: Sponsors
b089 heading 7024: License
b091 text 7078: MIT. The shortest license that works.
b093 heading 7126: Star History
b096 media 1963: Ponytail, the lazy senior dev
b097 media 2712: Something's coming, join the waitlist
b098 media 3035: Retriever
b099 media 5564: Each arm as a percent of the no-skill baseline across LOC, t
b100 media 6428: Median lines of code per arm across Haiku, Sonnet and Opus
b101 media 7180: Star History Chart

## Media
m00 block b096 still 1085x1241: Ponytail, the lazy senior dev
m01 block b097 still 1280x400: Something's coming, join the waitlist
m02 block b098 still NonexNone: Retriever
m03 block b099 still NonexNone: Each arm as a percent of the no-skill baseline across LOC, tokens, cost and time
m04 block b100 still NonexNone: Median lines of code per arm across Haiku, Sonnet and Opus
m05 block b101 still NonexNone: Star History Chart