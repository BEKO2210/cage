# coreyhaines31/marketingskills
Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.
stars 53319 · forks 7937 · JavaScript · licence MIT · release v2.11.17 (2026-10-03) · pushed 2026-10-03 · topics claude, codex, marketing
languages {'JavaScript': 93.9, 'HTML': 4.0, 'Shell': 2.0}

## README by section
### Marketing Skills for AI Agents
A collection of AI agent skills focused on marketing tasks.
### Partners
The library is free and MIT-licensed.
### What are Skills?
Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks.
### How Skills Work Together
Skills reference each other and build on shared context.
```
                            ┌──────────────────────────────────────┐
                            │          product-marketing           │
                            │    (read by all other skills first)  │
                            └──────────────────┬───────────────────┘
...
```
### Available Skills
| Skill | Description |
| ab-testing | When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation prog
| ad-creative | When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad
| ads | When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X,...
| ai-seo | When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers....
| analytics | When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions
|...
### Installation
### Option 1: CLI Install (Recommended)
Use npx skills to install skills directly: The CLI detects which agents you have installed and asks where to install.
```
# Install all skills
npx skills add coreyhaines31/marketingskills

# Install specific skills
...
```
### Option 2: Claude Code Plugin
Install via Claude Code's built-in plugin system: > **Note:** `/plugin` is only available in an interactive Claude Code CLI session.
```
# Add the marketplace
/plugin marketplace add coreyhaines31/marketingskills

# Install all marketing skills
...
```
### Option 3: OpenAI Codex Plugin
Install via Codex's plugin system: Select **marketing-skills** to install all skills.
```
# Add the marketplace
codex plugin marketplace add coreyhaines31/marketingskills

# Then browse and install from inside a Codex session
...
```
### Option 4: Clone and Copy
Clone the entire repo and copy the skills folder:
```
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```
### Option 5: Git Submodule
Add as a submodule for easy updates: Then reference skills from `.agents/marketingskills/skills/`.
```
git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills
```
### Option 6: Fork and Customize
1.
### Option 7: SkillKit (Multi-Agent)
Use SkillKit to install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.):
```
# Install all skills
npx skillkit install coreyhaines31/marketingskills

# Install specific skills
...
```
### Upgrading from v1.x to v2.0
v2.0 renames 17 skills and consolidates `page-cro` + `form-cro` into a single `cro` skill.
```
# From the directory where you installed the skills (e.g., .agents/skills/ or .claude/skills/)
rm -rf page-cro form-cro \
       ab-test-setup analytics-tracking aso-audit competitor-alternatives \
       email-sequence free-tool-strategy launch-strategy onboarding-cro \
...
```
### Migrate the product marketing context file
In v2.0 the context file moved from `.claude/` to `.agents/` and was renamed from `product-marketing-context.md` to `product-marketing.md`.
```
mkdir -p .agents
# v2.0 file (or pre-v2.0 file with new name)
mv .claude/product-marketing.md .agents/product-marketing.md 2>/dev/null
# pre-v2.0 file with legacy name
...
```
### Full rename map
| Old | New |
| `ab-test-setup` | `ab-testing` |
| `analytics-tracking` | `analytics` |
| `aso-audit` | `aso` |
| `competitor-alternatives` | `competitors` |
| `email-sequence` | `emails` |
|...
### Usage
Once installed, just ask your agent to help with marketing tasks: You can also invoke skills directly:
```
"Help me optimize this landing page for conversions"
→ Uses cro skill

"Write homepage copy for my SaaS"
...
```
```
/cro
/emails
/seo-audit
```
### Skill Categories
### Conversion Optimization
- `cro` - Pages and forms - `signup` - Registration flows - `onboarding` - Post-signup activation - `popups` - Modals and overlays - `paywalls` - In-app upgrade
### Content & Copy
- `copywriting` - Marketing page copy - `copy-editing` - Edit and polish existing copy - `cold-email` - B2B cold outreach emails and sequences - `emails` - Auto
### SEO & Discovery
- `seo-audit` - Technical and on-page SEO - `ai-seo` - AI search optimization (AEO, GEO, LLMO) - `programmatic-seo` - Scaled page generation - `site-architectur
### Paid & Distribution
- `ads` - Google, Meta, LinkedIn ad campaigns - `events` - Webinars, conferences, sponsorships, speaking - `ad-creative` - Bulk ad creative generation and itera
### Measurement & Testing
- `analytics` - Event tracking setup - `ab-testing` - Experiment design
### Retention
- `churn-prevention` - Cancel flows, save offers, dunning, payment recovery
### Growth Engineering
- `co-marketing` - Partner identification and joint campaigns - `free-tools` - Marketing tools and calculators - `referrals` - Referral and affiliate programs
### Strategy & Monetization
- `marketing-ideas` - 140 SaaS marketing ideas - `marketing-psychology` - Mental models and psychology - `launch` - Product launches and announcements - `pricin
### Sales & RevOps
- `revops` - Lead lifecycle, scoring, routing, pipeline management - `sales-enablement` - Sales decks, one-pagers, objection docs, demo scripts
### Contributing
Found a way to improve a skill?
### License
MIT - Use these however you want.

## Sentences with numbers (verbatim)
- | | cold-email | Write B2B cold emails and follow-up sequences that get replies.
- | | prospecting | When the user wants to find, qualify, and build a list of prospects to reach out to — across B2B SaaS, general B2B, or...
- Clone your fork into your projects ### Option 7: SkillKit (Multi-Agent) Use SkillKit to install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.): ## Upgrading 
- If you installed the v1.x skills, you'll have **stale old-name folders** in your install directory after upgrading — the new skills install alongside the old ones, so you'll see bo
- ### Full rename map | Old | New | |-----|-----| | `ab-test-setup` | `ab-testing` | | `analytics-tracking` | `analytics` | | `aso-audit` | `aso` | | `competitor-alternatives` | `com

## Page blocks (id kind y: text)
b000 header 72: coreyhaines31 / marketingskills Public Sponsor Notifications
b001 star 88: Star 53.3k
b002 files 307: Name Last commit message Last commit date .agents/plugins fe
b005 heading 1143: Marketing Skills for AI Agents
b007 text 1210: A collection of AI agent skills focused on marketing tasks. 
b008 text 1322: Built by Corey Haines. Need hands-on help? Check out Convers
b009 text 1434: New to the terminal and coding agents? Check out the compani
b010 text 1474: Contributions welcome! Found a way to improve a skill or hav
b011 text 1514: Run into a problem or have a question? Open an issue — we're
b013 heading 1562: Partners
b015 text 1616: The library is free and MIT-licensed. Verified Partners fund
b016 quote 1704: ◆ Converly — Conversion tracking / attribution. Server-side 
b017 quote 1816: ◆ Ploy — AI website & growth platform. AI marketing platform
b019 heading 1912: What are Skills?
b021 text 1966: Skills are markdown files that give AI agents specialized kn
b023 heading 2062: How Skills Work Together
b025 text 2116: Skills reference each other and build on shared context. The
b027 code 2204: ┌──────────────────────────────────────┐ │ product-marketing
b029 text 2804: See each skill's Related Skills section for the full depende
b031 heading 2852: Available Skills
b033 table 2906: rows 0-50 (0 = header) Skill Description ab-testing When the user wants to plan, de
b035 heading 6018: Installation
b038 heading 6080: Option 1: CLI Install (Recommended)
b040 text 6121: Use npx skills to install skills directly:
b041 code 6161: # Install all skills npx skills add coreyhaines31/marketings
b044 text 6367: The CLI detects which agents you have installed and asks whe
b045 text 6431: Tip If you run the command from inside an agent session (e.g
b047 text 6471: If you run the command from inside an agent session (e.g., a
b048 code 6559: npx skills add coreyhaines31/marketingskills -a claude-code
b050 heading 6659: Option 2: Claude Code Plugin
b052 text 6700: Install via Claude Code's built-in plugin system:
b053 code 6740: # Add the marketplace /plugin marketplace add coreyhaines31/
b056 quote 6886: Note: /plugin is only available in an interactive Claude Cod
b058 heading 7094: Option 3: OpenAI Codex Plugin
b060 text 7135: Install via Codex's plugin system:
b061 code 7175: # Add the marketplace codex plugin marketplace add coreyhain
b064 text 7321: Select marketing-skills to install all skills. To pick up ne
b066 heading 7393: Option 4: Clone and Copy
b068 text 7434: Clone the entire repo and copy the skills folder:
b069 code 7474: git clone https://github.com/coreyhaines31/marketingskills.g
b073 heading 7570: Option 5: Git Submodule
b075 text 7611: Add as a submodule for easy updates:
b076 code 7651: git submodule add https://github.com/coreyhaines31/marketing
b079 text 7719: Then reference skills from .agents/marketingskills/skills/.
b081 heading 7767: Option 6: Fork and Customize
b083 list 7808: Fork this repository Customize skills for your specific need
b085 heading 7912: Option 7: SkillKit (Multi-Agent)
b087 text 7953: Use SkillKit to install skills across multiple AI agents (Cl
b088 code 7993: # Install all skills npx skillkit install coreyhaines31/mark
b092 heading 8206: Upgrading from v1.x to v2.0
b094 text 8261: v2.0 renames 17 skills and consolidates page-cro + form-cro 
b095 code 8373: # From the directory where you installed the skills (e.g., .
b098 text 8558: Then reinstall the v2.0 skills via your usual method (e.g., 
b100 heading 8630: Migrate the product marketing context file
b102 text 8671: In v2.0 the context file moved from .claude/ to .agents/ and
b103 code 8735: mkdir -p .agents # v2.0 file (or pre-v2.0 file with new name
b106 text 8882: Skills will still check .claude/ and the legacy product-mark
b108 heading 8954: Full rename map
b110 table 8995: rows 0-19 (0 = header) Old New ab-test-setup ab-testing analytics-tracking analytic
b112 heading 9760: Usage
b114 text 9814: Once installed, just ask your agent to help with marketing t
b116 code 9854: "Help me optimize this landing page for conversions" → Uses 
b118 text 10119: You can also invoke skills directly:
b120 code 10159: /cro /emails /seo-audit
b123 heading 10274: Skill Categories
b126 heading 10336: Conversion Optimization
b128 list 10377: cro - Pages and forms signup - Registration flows onboarding
b130 heading 10537: Content & Copy
b132 list 10578: copywriting - Marketing page copy copy-editing - Edit and po
b134 heading 10766: SEO & Discovery
b136 list 10807: seo-audit - Technical and on-page SEO ai-seo - AI search opt
b138 heading 10995: Paid & Distribution
b140 list 11036: ads - Google, Meta, LinkedIn ad campaigns events - Webinars,
b142 heading 11168: Measurement & Testing
b144 list 11209: analytics - Event tracking setup ab-testing - Experiment des
b146 heading 11285: Retention
b148 list 11326: churn-prevention - Cancel flows, save offers, dunning, payme
b150 heading 11374: Growth Engineering
b152 list 11415: co-marketing - Partner identification and joint campaigns fr
b154 heading 11519: Strategy & Monetization
b156 list 11560: marketing-ideas - 140 SaaS marketing ideas marketing-psychol
b158 heading 11692: Sales & RevOps
b160 list 11733: revops - Lead lifecycle, scoring, routing, pipeline manageme
b162 heading 11809: Contributing
b164 text 11863: Found a way to improve a skill? Have a new skill to suggest?
b165 text 11903: See CONTRIBUTING.md for guidelines on adding or improving sk
b167 heading 11951: License
b169 text 12006: MIT - Use these however you want.

## Media