# cathrynlavery/diagram-design
Editorial diagram design for Claude Code, Codex, GitHub Copilot, Factory Droid, and Pi. 42 diagram types. Self-contained HTML + SVG. No shadows. No Mermaid slop.
stars 45744 · forks 2928 · HTML · licence MIT · release None () · pushed 2026-10-08 · topics agent-skills, claude-code, codex, data-visualization, diagrams, drawio, mermaid, svg
languages {'HTML': 66.4, 'Python': 33.5, 'Mermaid': 0.0}

## README by section
### (intro)
![Content site architecture](docs/screenshots/architecture.png) ![The self-improving loop](docs/screenshots/loop.png) *New in 2.0 — the Loop: flywheels with a s
### Why I built it
I write at littlemight.com (and run BestSelf.co on the side).
### What it makes
Every visual type ships in three static variants: minimal light, minimal dark, and full-editorial.
### Install
Official builds come only from this repository.
```
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```
```
codex plugin marketplace add cathrynlavery/diagram-design
codex plugin add diagram-design@diagram-design
```
### Editable install
Managed installs are convenient, but changes to `references/style-guide.md` may be replaced by package updates.
```
git clone git@github.com:cathrynlavery/diagram-design.git ~/code/diagram-design

# Pi: register the checkout as a local package
pi install ~/code/diagram-design
...
```
### Onboarding — make it look like *your* brand
The whole point: ship editorial-quality diagrams in **your** colors and typography, not a generic template.
### The flow
Every new diagram now uses your colors.
```
You:     "onboard diagram-design to https://yoursite.com"
Agent:   → fetches the homepage
         → extracts the dominant palette + font stack
         → maps detected values to semantic roles:
...
```
### What gets extracted
| Detected from your site | Becomes |
| `` background | `paper` token |
| Primary text color | `ink` token |
| Secondary / caption text | `muted` token |
| Cards or containers | `paper-2` token |
| Most-used brand color (CTA, link, heading) | `accent` token |
|...
### Contrast checks happen automatically
Before writing tokens, the skill verifies WCAG AA contrast on `ink` over `paper`.
### Accessible by default
Every diagram template gives the inline SVG an accessible name and description: `role="img"`, a resolving `aria-labelledby`, and first-child `` / `` slots.
### Manual override
Prefer to set tokens by hand?
### First-run gate
The skill won't silently ship default-skinned diagrams into a branded project.
### Working with multiple clients
Onboard a brand once, save the result as a named profile, then add a `.diagram-design` marker containing `profile: ` to each client project.
### Quickstart
Operator recipes for editable installs, first diagrams, brand setup, import, export, validation, Windows junctions, and reusable prompts live in `docs/cookbook.
```
# From a cloned checkout, open the gallery to see every diagram
open skills/diagram-design/assets/index.html       # macOS
xdg-open skills/diagram-design/assets/index.html  # Linux

...
```
```
cp skills/diagram-design/assets/template.html my-diagram.html        # minimal light
cp skills/diagram-design/assets/template-full.html my-diagram.html   # editorial with summary cards
cp skills/diagram-design/assets/template-motion.html my-diagram.html # optional accessible motion
```
### Semantic patterns and optional motion
When behavior matters, the skill chooses a semantic pattern first and a visual type second.
### Import from draw.io, Mermaid, or Excalidraw
Already have diagrams in draw.io / diagrams.net, Mermaid, or Excalidraw?
```
/diagram-design:import-drawio platform.drawio
/diagram-design:import-drawio platform.drawio --size=slide-16x9 --detail=simplified --audience=execu
/diagram-design:import-drawio platform.drawio --detail=faithful --format=png --page=all
/diagram-design:import-mermaid README.md --diagram=all
...
```
### The four dials
The point isn't conversion, it's **fitting the output to where it's going**.
| Dial | Options | What it changes |
| **Format** | `html` · `svg` · `png` · `html+png` | The deliverable. SVG for Figma, PNG for slides, HTML for the web. |
| **Size** | `doc-inline` · `doc-wide` · `slide-16x9` · `slide-4x3` · `social-og` · `social-square` · `print-a4-landscape` · `prin
| **Detail** | `faithful` (≤24 nodes, zoned) · `balanced` (≤12) · `simplified` (≤7) | How much of the source survives, via a fixed
| **Audience** | `engineer` · `mixed` · `executive` | The *wording*, not the count. `Auth Service / JWT · RS256 · :8443` → `Auth S
```
Detail: balanced · 12 source nodes → 8 drawn
Collapsed: "Token valid?" decision → edge label on Gateway → Auth
Dropped:   1 sticky note ("legacy path, to be retired") — unconnected in source
Kept in full: the request path (Web/Mobile → Gateway → Orders → Postgres)
```
### Export to PNG / SVG
Diagrams ship as self-contained HTML, but you can export the diagram itself for Figma, slides, or social cards.
```
/export-diagram path/to/diagram.html
/export-diagram path/to/diagram.html --svg-only
/export-diagram path/to/diagram.html --png-only --scale=3
/export-diagram path/to/diagram.html --registry
```
```
/diagram-design:export-diagram path/to/diagram.html
/diagram-design:export-diagram path/to/diagram.html --svg-only
/diagram-design:export-diagram path/to/diagram.html --png-only --scale=3
/diagram-design:export-diagram path/to/diagram.html --registry
```
### Architecture
Progressive disclosure.
```
diagram-design/
├── .agents/plugins/marketplace.json — Codex marketplace catalog
├── .claude-plugin/                  — Claude marketplace + plugin manifest
├── .codex-plugin/                   — Codex plugin manifest
...
```
### Contributing / skin lint
Before submitting a new example, run `python3 scripts/lint-skin.py `.
```
pip install playwright && playwright install chromium   # same dep as PNG export
python3 scripts/lint-render.py --self-test              # checks the checks
python3 scripts/lint-render.py --all                   # examples and templates
python3 scripts/lint-render.py <your-new-example.html>
...
```
### What loads when
At startup, the agent sees only the skill name and description.
| You ask for… | Agent loads |
| "Make me a flowchart" | `SKILL.md` + `references/type-flowchart.md` |
| "Build an architecture diagram" | `SKILL.md` + `references/type-architecture.md` |
| "Show what was added, removed, changed, moved, or rewired in this migration" | `SKILL.md` + `references/type-architecture-delta.
| "Show what's inside this device, exploded" | `SKILL.md` + `references/type-exploded.md` |
| "Draw our office floor plan" | `SKILL.md` + `references/type-axonometric-plan.md` |
|...
### It's working if…
- A routine request ("make me a flowchart") loads `SKILL.md`, exactly one type reference, and at most the two core references (`primitives-core.md`, `layout-bud
### The design system (in one paragraph)
One accent color, 1–2 focal elements per diagram.
### Primitives
- **Annotation callout** — italic Instrument Serif + dashed Bézier leader, for editorial asides that sit in the margins.
### When *not* to use this skill
- **Quick unicode diagrams** for tweets or terminal output → wiretext-style skill.
### Contributing
Contributions are welcome — new diagram types, import grammar support, examples, docs, and tooling.
### About
Made by **Cathryn Lavery** — founder of BestSelf.co.

## Sentences with numbers (verbatim)
- I'd either fight with Figma for 30 minutes or just skip the diagram.
- Editorial-quality visual types, matched to your brand in 60 seconds by reading your website.
- The accent color is reserved for the 1–2 things the reader should look at first.
- But 60 seconds of onboarding is better — the skill will pull your brand from your website and apply it across every diagram.
- | | **Detail** | `faithful` (≤24 nodes, zoned) · `balanced` (≤12) · `simplified` (≤7) | How much of the source survives, via a fixed degrade ladder — decorations, then duplicates, 
- - **PNG** — rasterizes the diagram via Playwright at 2× by default.
- ### Contributing / skin lint Before submitting a new example, run `python3 scripts/lint-skin.py `.
- The repository-wide check `python3 scripts/lint-skin.py --all --baseline` covers examples and templates and must stay green.
- Semantic routing must pass `python3 scripts/verify-semantic-motion.py --markdown-only`; the animated example has a separate `--example-only` gate.
- Every shipped motion template/example must also pass `python3 scripts/verify-motion.py --shipped`.
- If you touch the draw.io import path, `python3 scripts/verify-drawio-import.py` must also pass — it drives the real extractor against `scripts/fixtures/sample-architecture.drawio` 
- If you touch the Mermaid import path, `python3 scripts/verify-mermaid-import.py` must also pass — it covers all supported grammars, multi-block Markdown, adversarial labels, trust-
- If you touch the Excalidraw import path, `python3 scripts/verify-excalidraw-import.py` must also pass — it covers scene parsing, bound labels, groups and frames, adversarial labels
- Label placement is gated geometrically: `python3 scripts/verify-geometry.py --all` fails CI when a label mask overlaps a node declared later in the document, because the node fill 
- `python3 scripts/test-verify-geometry.py` keeps that checker honest in both directions.
- Diagrams using the traceable block decomposition pattern get a structural gate on top of that: `python3 scripts/verify-block-registry.py --all` fails CI on a duplicate `data-block-
- `python3 scripts/test-verify-block-registry.py` keeps that checker honest in both directions.
- Treemaps get a second geometric gate, because their whole claim is that area *is* the encoding: `python3 scripts/verify-treemap.py --all` fails CI when a cell's share of the drawn 

## Page blocks (id kind y: text)
b000 header 172: diagram-design Public Sponsor Notifications Fork2.9k (2.9k) 
b001 star 192: Star45.7k (45.7k)
b002 about 250: About Editorial diagram design for Claude Code, Codex, GitHu
b003 files 368: Name Last commit message Last commit date .agents/plugins do
b011 text 2856: New in 2.0 — the Loop: flywheels with a shared-memory hub. T
b012 text 2896: New in 2.3: semantic system patterns and optional accessible
b013 text 2960: New in 2.5.10: ten more layout grammars — Sankey, fishbone, 
b014 text 3024: Editorial diagram types for Claude Code, Codex, Factory Droi
b015 text 3184: No Figma. No generic rounded boxes. No 30-minute color-picki
b016 text 3224: Project site: diagramdesign.dev
b018 heading 3297: Why I built it
b020 text 3351: I write at littlemight.com (and run BestSelf.co on the side)
b021 text 3463: So I built a Claude Code skill for it. Editorial-quality vis
b022 quote 3527: The highest-quality move is usually deletion. Every node ear
b024 heading 3624: What it makes
b026 text 3678: Every visual type ships in three static variants: minimal li
b027 table 3742: rows 0-14 (0 = header) Architecture Components + connections IT current-state Legac
b028 text 6875: Architecture delta compares synchronized topologies through 
b029 text 6963: Exploded axonometric draws one object in 2:1 dimetric projec
b030 text 7075: Axonometric plan uses the same projection for one floor or o
b031 text 7163: The v2.5.10 release added ten layout grammars. Compare their
b032 text 7227: Browse the live gallery: cathrynlavery.github.io/diagram-des
b034 heading 7324: Install
b036 text 7378: Official builds come only from this repository. LittleMight,
b039 code 7506: /plugin marketplace add cathrynlavery/diagram-design /plugin
b041 text 7593: Then enable updates once: run /plugin, open Marketplaces, se
b043 code 7745: codex plugin marketplace add cathrynlavery/diagram-design co
b046 text 7833: Codex refreshes configured Git marketplaces at startup. To f
b048 code 7937: copilot plugin marketplace add cathrynlavery/diagram-design 
b051 text 8024: Copilot installs the shared Diagram Design skill plus its do
b053 code 8200: droid plugin marketplace add https://github.com/cathrynlaver
b056 text 8287: Droid tracks Git plugins by commit rather than the manifest'
b057 text 8375: Claude Cowork (organization marketplace): Organization GitHu
b059 code 8575: pi install https://github.com/cathrynlavery/diagram-design
b062 text 8643: Run /reload in an open Pi session. Pi makes the skill availa
b063 text 8755: Kiro: Import the Agent Skill from the repository subdirector
b065 code 8795: https://github.com/cathrynlavery/diagram-design/tree/main/sk
b067 text 8863: Kiro copies imported skills into .kiro/skills/ for a workspa
b068 text 8951: OpenCode: Copy or symlink skills/diagram-design/ to .opencod
b069 text 9039: Any other Agent Skills host (Cursor, Cline, Amp, Gemini CLI,
b070 code 9127: npx skills add cathrynlavery/diagram-design
b073 text 9195: When the selected roots resolve to more than one skills dire
b074 text 9331: This is a standalone install, separate from every marketplac
b075 quote 9467: One-time migration: an existing standalone npx skills add co
b077 heading 9611: Editable install
b079 text 9652: Managed installs are convenient, but changes to references/s
b080 code 9764: git clone git@github.com:cathrynlavery/diagram-design.git ~/
b083 text 10127: The shared skill lives at skills/diagram-design/. Pi discove
b085 heading 10248: Onboarding — make it look like your brand
b087 text 10303: The whole point: ship editorial-quality diagrams in your col
b088 text 10343: Out of the box, diagrams render in a clean jet-black + atomi
b090 heading 10463: The flow
b093 code 10504: You: "onboard diagram-design to https://yoursite.com" Agent:
b095 text 10709: Every new diagram now uses your colors. Your website's paper
b096 text 10773: Brand matching also emits a fidelity receipt: sampled URLs, 
b098 heading 10869: What gets extracted
b100 table 10910: rows 0-8 (0 = header) Detected from your site Becomes <body> background paper toke
b102 heading 11268: Contrast checks happen automatically
b104 text 11309: Before writing tokens, the skill verifies WCAG AA contrast o
b106 heading 11381: Accessible by default
b108 text 11422: Every diagram template gives the inline SVG an accessible na
b110 heading 11542: Manual override
b112 text 11583: Prefer to set tokens by hand? Open skills/diagram-design/ref
b114 heading 11679: First-run gate
b116 text 11720: The skill won't silently ship default-skinned diagrams into 
b117 quote 11784: "This is your first diagram in this project. The style guide
b118 text 11848: See skills/diagram-design/references/onboarding.md for the f
b120 heading 11896: Working with multiple clients
b122 text 11937: Onboard a brand once, save the result as a named profile, th
b123 text 12049: The profile library is shared across Claude Code, Codex, Fac
b125 heading 12170: Quickstart
b127 code 12224: # From a cloned checkout, open the gallery to see every diag
b130 text 12469: Operator recipes for editable installs, first diagrams, bran
b131 text 12533: Your agent will pick the right type, build the HTML, and sav
b132 code 12597: cp skills/diagram-design/assets/template.html my-diagram.htm
b136 heading 12713: Semantic patterns and optional motion
b138 text 12754: When behavior matters, the skill chooses a semantic pattern 
b139 text 12890: Motion is optional and does not create another visual type. 
b141 heading 13107: Import from draw.io, Mermaid, or Excalidraw
b143 text 13161: Already have diagrams in draw.io / diagrams.net, Mermaid, or
b145 text 13772: A 12-node draw.io file redrawn at balanced detail for a blog
b147 code 13836: /diagram-design:import-drawio platform.drawio /diagram-desig
b149 text 14002: Or just ask: "redraw this drawio file for my deck", "make th
b150 text 14066: Reads the common containers draw.io writes — .drawio, .drawi
b152 heading 14234: The four dials
b154 text 14275: The point isn't conversion, it's fitting the output to where
b155 table 14339: rows 0-4 (0 = header) Dial Options What it changes Format html · svg · png · html+
b156 text 14757: Every import ends with a fidelity ledger — what got merged, 
b158 code 14821: Detail: balanced · 12 source nodes → 8 drawn Collapsed: "Tok
b160 text 14948: What never carries over: source or renderer coordinates, sou
b162 heading 15093: Export to PNG / SVG
b164 text 15147: Diagrams ship as self-contained HTML, but you can export the
b167 code 15251: /export-diagram path/to/diagram.html /export-diagram path/to
b171 code 15418: /diagram-design:export-diagram path/to/diagram.html /diagram
b173 text 15545: Or just ask in natural language:
b175 code 15585: "Export this diagram as SVG and PNG." "Save my-diagram.html 
b177 list 15672: SVG — extracts the <svg> node and injects Google Fonts so it
b178 text 15788: Both formats are diagram-only — editorial cards and headers 
b179 list 15876: --registry — for diagrams using the traceable block decompos
b180 text 15988: For motion-enabled HTML, export the explicit final state: op
b182 heading 16109: Architecture
b184 text 16164: Progressive disclosure. SKILL.md routes behavior first when 
b186 code 16228: diagram-design/ ├── .agents/plugins/marketplace.json — Codex
b188 text 18403: This keeps the agent's working context tight: routine diagra
b190 heading 18475: Contributing / skin lint
b192 text 18516: Before submitting a new example, run python3 scripts/lint-sk
b193 text 18988: Label placement is gated geometrically: python3 scripts/veri
b194 text 19772: All pull requests and pushes are automatically validated acr
b195 text 19836: lint-skin.py reads the source. lint-render.py renders it — h
b196 code 19924: pip install playwright && playwright install chromium # same
b199 text 20071: Clipping is measured by paint, not geometry: getBoundingClie
b200 text 20279: No golden images, so there is nothing to re-record and no PN
b201 text 20415: Font metrics differ between the default run and --fonts. Wit
b203 heading 20535: What loads when
b205 text 20576: At startup, the agent sees only the skill name and descripti
b206 table 20640: rows 0-16 (0 = header) You ask for… Agent loads "Make me a flowchart" SKILL.md + re
b207 text 21622: No matter how many types exist, the agent only reads the one
b209 heading 21719: It's working if…
b211 list 21773: A routine request ("make me a flowchart") loads SKILL.md, ex
b212 text 22049: If any of these fail, that's a bug worth filing.
b214 heading 22097: The design system (in one paragraph)
b216 text 22151: One accent color, 1–2 focal elements per diagram. Three font
b218 heading 22344: Primitives
b220 list 22399: Annotation callout — italic Instrument Serif + dashed Bézier
b222 heading 22696: When not to use this skill
b224 list 22750: Quick unicode diagrams for tweets or terminal output → wiret
b225 text 22874: Before drawing, ask: would a reader learn more from this tha
b227 heading 22971: Contributing
b229 text 23025: Contributions are welcome — new diagram types, import gramma
b231 heading 23146: About
b233 text 23200: Made by Cathryn Lavery — founder of BestSelf.co. I write abo
b234 text 23264: If this is useful, star the repo and come say hi on X.
b235 media 1326: Diagram Design. Editorial diagrams your designer won't hate.
b236 media 1859: Content site architecture
b237 media 2284: The self-improving loop
b238 media 3764: Architecture
b239 media 3759: IT current-state
b240 media 3749: Flowchart
b241 media 3968: Sequence
b242 media 3984: State machine
b243 media 3981: ER
b244 media 4193: Timeline
b245 media 4186: Swimlane
b246 media 4183: Quadrant
b247 media 4397: Radar chart
b248 media 4377: Loop
b250 media 4625: Tree
b251 media 4610: Org chart
b252 media 4622: Layer stack
b253 media 4831: Venn
b254 media 4829: Pyramid
b256 media 5023: Treemap
b259 media 5222: Scatter plot
b260 media 5217: High-Level
b261 media 5233: Process
b262 media 5424: Medallion
b263 media 5429: Data flow
b264 media 5421: DP integration
b265 media 5652: DP security matrix
b266 media 5628: Sankey
b267 media 5647: Fishbone
b268 media 5837: Wardley map
b269 media 5846: Kanban
b270 media 5840: User journey
b271 media 6056: Deployment
b272 media 6031: Dependency graph
b273 media 6021: UML class
b274 media 6260: Story map
b275 media 6260: Database schema
b276 media 6263: Polar chart
b277 media 6468: Waterfall
b278 media 6460: Architecture delta
b279 media 6461: Exploded axonometric
b280 media 6677: Axonometric plan
b281 media 6671: Heatmap
b282 media 13225: Redrawn from a .drawio file

## Media
m00 block b235 still 1680x840: Diagram Design. Editorial diagrams your designer won't hate.
m01 block b236 still 1400x673: Content site architecture
m02 block b237 still 1400x916: The self-improving loop
m03 block b238 still 1400x673: Architecture
m04 block b239 still 600x313: IT current-state
m05 block b240 still 600x360: Flowchart
m06 block b241 still 600x350: Sequence
m07 block b242 still 600x276: State machine
m08 block b243 still 600x288: ER
m09 block b244 still 600x252: Timeline
m10 block b245 still 600x288: Swimlane
m11 block b246 still 600x300: Quadrant
m12 block b247 still 600x300: Radar chart
m13 block b248 still 1400x916: Loop
m14 block b249 still 600x300: Nested
m15 block b250 still 600x288: Tree
m16 block b251 still 600x358: Org chart
m17 block b252 still 600x300: Layer stack
m18 block b253 still 600x288: Venn
m19 block b254 still 600x300: Pyramid
m20 block b255 still 600x300: Bar chart
m21 block b256 still 600x300: Treemap
m22 block b257 still 600x300: Line chart
m23 block b258 still 600x300: Gantt