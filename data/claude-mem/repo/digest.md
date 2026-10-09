# thedotmack/claude-mem
Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More
stars 96979 · forks 8546 · TypeScript · licence Apache-2.0 · release v13.33.0 (2026-10-06) · pushed 2026-10-06 · topics ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk
languages {'TypeScript': 57.5, 'JavaScript': 31.7, 'Python': 9.2, 'HTML': 0.9, 'Shell': 0.7}

## README by section
### (intro)
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; 🇨🇳 中文 • 🇹🇼 繁體中文 • 🇯🇵 日本語 • 🇵🇹 Português • 🇧🇷 Português • 🇰🇷 한국어 • 🇪🇸 Español • 🇩🇪 Deutsch • 🇫🇷 Français • 🇮🇱 עברית • 🇸🇦 ال
### Quick Start
Install claude-mem for Grok Bot: Grok Bot has no host hooks, so we watch the chat log files.
```
npx claude-mem install --ide grok-bot
```
```
npx claude-mem install
```
### 🦞 OpenClaw Gateway
Install claude-mem as a persistent memory plugin on OpenClaw gateways with a single command: The installer handles dependencies, plugin setup, AI provider confi
```
curl -fsSL https://install.cmem.ai/openclaw.sh | bash
```
### Documentation
📚 **View Full Documentation** - Browse on official website
### Getting Started
- **Installation Guide** - Quick start & advanced installation - **Usage Guide** - How Claude-Mem works automatically - **Search Tools** - Query your project hi
### Best Practices
- **Context Engineering** - AI agent context optimization principles - **Progressive Disclosure** - Philosophy behind Claude-Mem's context priming strategy
### Architecture
- **Overview** - System components & data flow - **Architecture Evolution** - The journey from v3 to v5 - **Hooks Architecture** - How Claude-Mem uses lifecycle
### Configuration & Development
- **Configuration** - Environment variables & settings - **Development** - Building, testing, contributing - **Release Branches** - Stable, core-dev, and commun
### How It Works
**Core Components:** 1.
### MCP Search Tools
Claude-Mem provides intelligent memory search through **4 MCP tools** following a token-efficient **3-layer workflow pattern**: **The 3-Layer Workflow:** 1.
```
// Step 1: Search for index
search(query="authentication bug", type="bugfix", limit=10)

// Step 2: Review index, identify relevant IDs (e.g., #123, #456)
...
```
### Release Branches
Stable releases ship from `main` and are published to npm.
### System Requirements
- **Node.js**: 20.0.0 or higher - **Claude Code**: Latest version with plugin support - **Bun**: JavaScript runtime and process manager (auto-installed if missi
### Windows Setup Notes
If you see an error like: Make sure Node.js and npm are installed and added to your PATH.
```
npm : The term 'npm' is not recognized as the name of a cmdlet
```
### Configuration
Settings are managed in `~/.claude-mem/settings.json` (auto-created with defaults on first run).
### Mode & Language Configuration
Claude-Mem supports multiple workflow modes and languages via the `CLAUDE_MEM_MODE` setting.
| Mode | Description |
| `code` | Default English mode |
| `code--zh` | Simplified Chinese mode |
| `code--ja` | Japanese mode |
```
{
  "CLAUDE_MEM_MODE": "code--zh"
}
```
```
ls ~/.claude/plugins/marketplaces/thedotmack/plugin/modes/
```
### Development
See the **Development Guide** for build instructions, testing, and contribution workflow.
### Troubleshooting
If experiencing issues, describe the problem to Claude and the troubleshoot skill will automatically diagnose and provide fixes.
### Bug Reports
Create comprehensive bug reports with the automated generator:
```
cd ~/.claude/plugins/marketplaces/thedotmack
npm run bug-report
```
### Contributing
Contributions are welcome!
### License
Claude-Mem is licensed under the Apache License 2.0.
### Support
- **Documentation**: docs/ - **Issues**: GitHub Issues - **Repository**: github.com/thedotmack/claude-mem - **Official X Account**: @Claude_Memory - **Official 
### What About CMEM?
CMEM is a token created by a 3rd party but officially embraced by the creator of Claude-Mem (Alex Newman, @thedotmack).

## Sentences with numbers (verbatim)
- Signing in provisions a memory key for your account and unlocks the **claude-mem observer**: memory that runs off-plan, free for up to 14 days, so you get up to 100% more usage fro
- **`search`** - Get compact index with IDs (~50-100 tokens/result) 2.
- **`get_observations`** - Fetch full details ONLY for filtered IDs (~500-1,000 tokens/result) **How It Works:** - Claude uses MCP tools to search your memory - Start with `search` t

## Page blocks (id kind y: text)
b000 header 72: thedotmack / claude-mem Public Sponsor Notifications Fork 8.
b001 star 88: Star 97k
b002 files 308: Name Last commit message Last commit date .agent-jobs fix(wo
b008 text 2814: 🇨🇳 中文 • 🇹🇼 繁體中文 • 🇯🇵 日本語 • 🇵🇹 Português • 🇧🇷 Português • 🇰🇷 
b010 heading 2934: Persistent memory compression system built for Claude Code.
b016 text 3413: Quick Start • How It Works • Search Tools • Documentation • 
b017 text 3453: Claude-Mem seamlessly preserves context across sessions by a
b019 heading 3598: Quick Start
b021 text 3652: Install claude-mem for Grok Bot:
b022 code 3692: npx claude-mem install --ide grok-bot
b025 text 3760: Grok Bot has no host hooks, so we watch the chat log files. 
b026 text 3824: Awareness push pilot (LFG + Orifice): needle observations (d
b027 text 3936: Install with a single command:
b028 code 3976: npx claude-mem install
b031 text 4044: The installer sets everything up first, then asks you to sig
b032 text 4204: Prefer to skip the sign-in? Pass an explicit --provider flag
b033 text 4268: Or install for OpenCode:
b034 code 4308: npx claude-mem install --ide opencode
b037 text 4376: Or install for T3 Code (Codex and Claude Code providers):
b038 code 4416: npx claude-mem install --ide t3code
b041 text 4484: The installer discovers T3 Code's enabled providers, registe
b042 text 4596: Or install for Antigravity CLI (setup guide):
b043 code 4636: npx claude-mem install --ide antigravity
b046 text 4704: Or install for OMP (Oh My Pi):
b047 code 4744: npx claude-mem install --ide omp
b050 text 4812: Or install from the plugin marketplace inside Claude Code:
b051 code 4852: /plugin marketplace add thedotmack/claude-mem /plugin instal
b054 text 4959: Restart Claude Code. Context from previous sessions will aut
b055 quote 4999: Note: Claude-Mem is also published on npm, but npm install -
b057 heading 5095: 🦞 OpenClaw Gateway
b059 text 5136: Install claude-mem as a persistent memory plugin on OpenClaw
b060 code 5176: curl -fsSL https://install.cmem.ai/openclaw.sh | bash
b063 text 5244: The installer handles dependencies, plugin setup, AI provide
b065 list 5372: 🧠 Persistent Memory - Context survives across sessions 📊 Pro
b067 heading 5693: Documentation
b069 text 5748: 📚 View Full Documentation - Browse on official website
b071 heading 5796: Getting Started
b073 list 5837: Installation Guide - Quick start & advanced installation Usa
b075 heading 5969: Best Practices
b077 list 6010: Context Engineering - AI agent context optimization principl
b079 heading 6086: Architecture
b081 list 6127: Overview - System components & data flow Architecture Evolut
b083 heading 6343: Configuration & Development
b085 list 6384: Configuration - Environment variables & settings Development
b087 heading 6541: How It Works
b090 list 6635: 5 Lifecycle Hooks - SessionStart, UserPromptSubmit, PostTool
b091 text 6839: See Architecture Overview for details.
b093 heading 6912: MCP Search Tools
b095 text 6966: Claude-Mem provides intelligent memory search through 4 MCP 
b096 text 7030: The 3-Layer Workflow:
b097 list 7070: search - Get compact index with IDs (~50-100 tokens/result) 
b099 list 7206: Claude uses MCP tools to search your memory Start with searc
b100 text 7358: Available MCP Tools:
b101 list 7398: search - Search memory index with full-text queries, filters
b103 code 7534: // Step 1: Search for index search(query="authentication bug
b106 text 7720: See Search Tools Guide for detailed examples.
b108 heading 7793: Release Branches
b110 text 7847: Stable releases ship from main and are published to npm. cor
b112 heading 7968: System Requirements
b114 list 8022: Node.js: 20.0.0 or higher Claude Code: Latest version with p
b116 heading 8207: Windows Setup Notes
b118 text 8248: If you see an error like:
b119 code 8288: npm : The term 'npm' is not recognized as the name of a cmdl
b122 text 8356: Make sure Node.js and npm are installed and added to your PA
b124 heading 8453: Configuration
b126 text 8507: Settings are managed in ~/.claude-mem/settings.json (auto-cr
b127 text 8571: To include observations from every harness in Claude Code an
b128 text 8683: See the Configuration Guide for all available settings and e
b130 heading 8731: Mode & Language Configuration
b132 text 8772: Claude-Mem supports multiple workflow modes and languages vi
b133 text 8812: This option controls both:
b134 list 8852: The workflow behavior (e.g. code, chill, investigation) The 
b136 heading 8928: How to Configure
b138 text 8964: Edit your settings file at ~/.claude-mem/settings.json:
b139 code 9004: { "CLAUDE_MEM_MODE": "code--zh" }
b142 text 9112: Modes are defined in plugin/modes/. To see all available mod
b143 code 9152: ls ~/.claude/plugins/marketplaces/thedotmack/plugin/modes/
b147 heading 9228: Available Modes
b149 table 9264: rows 0-3 (0 = header) Mode Description code Default English mode code--zh Simplifi
b150 text 9429: Language-specific modes follow the pattern code--[lang] wher
b151 quote 9493: Note: code--zh (Simplified Chinese) is already built-in — no
b153 heading 9565: After Changing Mode
b156 heading 9609: Restart Claude Code to apply the new mode configuration.
b159 heading 9671: Development
b161 text 9725: See the Development Guide for build instructions, testing, a
b163 heading 9798: Troubleshooting
b165 text 9852: If experiencing issues, describe the problem to Claude and t
b166 text 9916: See the Troubleshooting Guide for common issues and solution
b168 heading 9989: Bug Reports
b170 text 10043: Create comprehensive bug reports with the automated generato
b171 code 10083: cd ~/.claude/plugins/marketplaces/thedotmack npm run bug-rep
b175 heading 10179: Contributing
b177 text 10233: Contributions are welcome! Please:
b178 list 10273: Fork the repository Create a feature branch Make your change
b179 text 10425: Claude-Mem ships from three branches: main (stable), core-de
b180 text 10513: See Development Guide for contribution workflow.
b182 heading 10586: License
b184 text 10640: Claude-Mem is licensed under the Apache License 2.0.
b185 text 10680: We chose Apache-2.0 because durable agentic memory should be
b186 text 10744: See the LICENSE file for full details. See docs/license.md a
b187 text 10808: Note on Ragtime: The ragtime/ directory is licensed under th
b189 heading 10905: Support
b191 list 10959: Documentation: docs/ Issues: GitHub Issues Repository: githu
b192 text 11172: Built with Claude Agent SDK | Works with Claude Code | Made 
b194 heading 11245: What About CMEM?
b196 text 11286: CMEM is a token created by a 3rd party but officially embrac
b197 text 11374: Official BASE CA: 0x76b1967eec0ccaeb001bbbb2b40dc4badba31ba3
b198 media 3143: Claude-Mem Preview
b199 media 3122: Star History Chart

## Media
m00 block b198 animated 211f@10.0 640x360: Claude-Mem Preview
m01 block b199 still 800x533: Star History Chart