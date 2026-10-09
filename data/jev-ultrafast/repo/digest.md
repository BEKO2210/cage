# browser-use/jev-ultrafast
Fastest and cheapest web agent
stars 22261 · forks 1615 · Python · licence MIT · release None () · pushed 2026-09-30 · topics 
languages {'Python': 57.8, 'HTML': 18.5, 'JavaScript': 13.3, 'CSS': 10.4}

## README by section
### (intro)
### Jev Ultrafast ⚡
> [!IMPORTANT] > **The Browser Use Cloud waitlist is open.** Get early access to ultrafast browser agents in the cloud.
### The action space
Every observation produces a new element table: The operations are `CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_UP`, `SCROLL_DOWN`, `WAIT`, `DONE`, and `BLOCKED`.
```
[1] button    Change ticket type · Round trip
[2] combobox  Where from?        · San Francisco
[3] combobox  Where to?          · empty
[4] textbox   Departure          · empty
...
```
```
                      one TypeSafe request
                     ┌───────────────────────────┐
page → element table → operation                 │
                     │ click_target              │
...
```
### Try it
Open **http://127.0.0.1:8766** and click **Start demo → Run automatically**.
```
git clone https://github.com/browser-use/jev-ultrafast.git
cd jev-ultrafast
uv sync
cp .env.example .env
...
```
### Use the library
Run with `uv run --env-file .env python your_script.py`.
```
from jev_ultrafast import Agent

with Agent(
    "https://www.google.com/travel/flights?hl=en",
...
```
```
uv run --env-file .env python examples/run.py \
  --url https://en.wikipedia.org/wiki/Main_Page \
  --goal 'Find and open the Wikipedia article about Gödel’s incompleteness theorems.'
```
### Why it moves
- **One request per decision cycle.** Operation and target heads share the same observed state.
### Small enough to read
| File | Job |
| agent.py | The complete loop and text-helper handoff |
| snapshot.js | Atomic DOM snapshot, indexed controls, freshness guards |
| browser.py | Browser connection, current geometry, execution |
| model.py | Dynamic operation/target heads and text generation |
| questions.py | Model instructions |
|...
### Evidence and limits
The current video is a **7,073 ms** Google Flights run.
### Development
Tests are offline.
```
uv run ruff check .
uv run pytest
node --check jev_ultrafast/static/app.js
node --check jev_ultrafast/snapshot.js
...
```

## Sentences with numbers (verbatim)
- **Zürich → London on Google Flights in 7.1 seconds.** One natural-language goal, actual text generation, and loading waits included.
- - **Wait for useful state.** After typing into a combobox, wait for visible suggestions, capped at 200 ms.
- Other interactions get at most two animation frames or 50 ms.
- ## Small enough to read | File | Job | | --- | --- | | agent.py | The complete loop and text-helper handoff | | snapshot.js | Atomic DOM snapshot, indexed controls, freshness guard
- The video plays at 1×, with no opening hold and a 0.5-second final hold.
- Median task time went from **9.450 s → 7.092 s**, a **25% reduction**; median browser protocol calls went from **1,092 → 101**.
- The same policy opened the requested Wikipedia article in **2.798 s** and passed a local hotel search/filter task in **1.896 s**.
- `scripts/record_flights.py ` captures original browser timestamps; `scripts/render_demo.py ` renders that verified run at 1× and crops out the Google account strip.

## Page blocks (id kind y: text)
b000 header 172: jev-ultrafast Public Notifications Fork1.6k (1.6k) Star22.3k
b001 star 192: Star22.3k (22.3k)
b002 about 250: About Fastest and cheapest web agent browser-use.com Resourc
b003 files 368: Name Last commit message Last commit date docs Reduce browse
b007 heading 1275: Jev Ultrafast ⚡
b009 text 1342: Important The Browser Use Cloud waitlist is open. Get early 
b011 text 1382: The Browser Use Cloud waitlist is open. Get early access to 
b012 text 1454: A browser agent with a dynamic, indexed action space.
b013 text 1494: Give it one goal. TypeSafe's Jev picks an operation and an e
b014 text 1558: Zürich → London on Google Flights in 7.1 seconds. One natura
b016 text 2190: Watch the MP4 · Measurements · Read the loop
b018 heading 2238: The action space
b020 text 2293: Every observation produces a new element table:
b022 code 2333: [1] button Change ticket type · Round trip [2] combobox Wher
b024 text 2479: The operations are CLICK, TYPE_TEXT, SELECT, SCROLL_UP, SCRO
b026 code 2543: one TypeSafe request ┌───────────────────────────┐ page → el
b028 text 2847: Target questions are speculative. If the operation is CLICK,
b029 text 2935: There are no site-specific action scripts or prepared field 
b031 heading 3031: Try it
b033 code 3086: git clone https://github.com/browser-use/jev-ultrafast.git c
b036 text 3252: Open http://127.0.0.1:8766 and click Start demo → Run automa
b037 text 3340: Chrome connects through Browser Harness, installed by uv syn
b038 text 3404: TEXT_MODEL_API_KEY is an OpenRouter key in the example confi
b040 heading 3500: Use the library
b042 code 3554: from jev_ultrafast import Agent with Agent( "https://www.goo
b045 text 3779: Run with uv run --env-file .env python your_script.py. The s
b046 code 3819: uv run --env-file .env python examples/run.py \ --url https:
b049 text 3926: uv run --env-file .env python examples/flights.py --keep-ope
b051 heading 3998: Why it moves
b053 list 4053: One request per decision cycle. Operation and target heads s
b054 text 4481: Every executed target is resolved from an observed node. The
b056 heading 4577: Small enough to read
b058 table 4631: rows 0-6 (0 = header) File Job agent.py The complete loop and text-helper handoff 
b060 heading 4915: Evidence and limits
b062 text 4969: The current video is a 7,073 ms Google Flights run. Timing s
b063 text 5081: In six alternating runs with identical models and settings, 
b064 text 5169: The same policy opened the requested Wikipedia article in 2.
b065 text 5257: A DONE choice still requires independent outcome verificatio
b067 heading 5377: Development
b069 code 5431: uv run ruff check . uv run pytest node --check jev_ultrafast
b072 text 5578: Tests are offline. uv run python scripts/check_guards.py che
b073 text 5723: Browser Use · Browser Harness · TypeSafe speculative fan-out
b074 media 957: Jev Ultrafast · Browser Use × TypeSafe
b075 media 1622: A real Google Flights search at 1× speed, with generated cit

## Media
m00 block b074 still NonexNone: Jev Ultrafast · Browser Use × TypeSafe
m01 block b075 animated 91f@12.01 1152x750: A real Google Flights search at 1× speed, with generated city names and dynamic 