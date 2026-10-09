# t8y2/dbx
25 MB lightweight cross-platform database client for 100+ databases, including MySQL, PostgreSQL, SQLite, Redis, MongoDB, DuckDB, SQL Server, and Dameng. Built-in AI, MCP Server, CLI, desktop and Docker. | 轻量级跨平台数据库管理工具，支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、达梦等 100+ 数据库，提供桌面端、Docker、CLI、内置 AI 助手和 MCP。
stars 25380 · forks 2296 · Rust · licence Apache-2.0 · release v0.6.38 (2026-10-09) · pushed 2026-10-09 · topics ai, cli, clickhouse, database, database-client, database-management, docker, gui
languages {'Rust': 39.6, 'TypeScript': 30.0, 'Vue': 17.7, 'Go': 5.8, 'Java': 5.2}

## README by section
### (intro)
100+ databases in 25 MB.
### ❤️ Sponsors
JumpServer is an Open-source Privileged Access Management (PAM) platform with AI-powered capabilities, providing DevOps and IT teams a unified workspace to secu
### 🤝 Partners
1Panel is a modern open-source Linux server management panel and lightweight AI management platform, offering an intuitive web interface for one-stop management
### Why DBX?
🪶 25 MB, zero runtime bloat No Java JRE.
### Features
### 100+ Databases, One Tool
MySQL, PostgreSQL, SQLite, Cloudflare D1, Redis, MongoDB, DuckDB, ClickHouse, SQL Server, Oracle, Elasticsearch, Easysearch, Meilisearch, CouchDB, Qdrant, Milvu
### Query Editor
CodeMirror 6 with SQL syntax highlighting, metadata-aware autocomplete, `Cmd+Enter` execution, selected SQL execution, SQL formatting, diagnostics, and 9 editor
### AI SQL Assistant
Describe what you want in plain language — get SQL back.
### Data Grid
Virtual-scrolled table that handles large result sets.
### Schema Tools
- **Schema browser** — databases, schemas, tables, columns, indexes, foreign keys, triggers, with sidebar search & pin - **Object browser** — grouped procedures
### Data Operations
- **Table import** — CSV, Excel - **Data transfer** — migrate between databases - **Database export** — full database dump - **Data compare** — compare table da
### Specialized Browsers
- **Redis** — key pattern search, batch key operations, command runner, TTL editing, and all data types (String, Hash, List, Set, ZSet, Stream) - **MongoDB** — 
### Message Queue & Middleware Consoles
- **Kafka / RocketMQ / RabbitMQ / Pulsar** — topics, consumer groups, message browsing, query and trace, broker monitoring, permissions and policies - **MQTT** 
### Plugin System
- **Extensible by design** — new connection types and tools arrive as plugins: S3 browsing, Kubernetes, LDAP, and more from the built-in store - **Signed & sand
### Safety & Connectivity
SSH tunnel (key & password) · database and AI proxy settings · auto-reconnect on connection loss · confirmation dialogs for destructive operations · encrypted c
### Polished UI
Dark mode with native title bar sync · 9 editor themes · English, 简体中文 & Español · layout preferences · built-in auto-update
### AI Agent Integration (MCP)
DBX provides a separate Rust-powered MCP server that lets AI coding agents query databases using connections configured in DBX.
```
npx @dbx-app/mcp-server
```
```
{
  "mcpServers": {
    "dbx": { "command": "npx", "args": ["-y", "@dbx-app/mcp-server"] }
  }
...
```
### Install
Download the latest release from the Releases page.
```
brew install --cask dbx
```
```
scoop bucket add dbx https://github.com/t8y2/scoop-bucket
scoop install dbx
```
### Self-Hosted (Docker)
For scheduled backups after closing the desktop app or browser, see Background Database Backups, including Windows/macOS/Linux startup and persistent container 
```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```
```
docker compose -f deploy/docker-compose.release.yml up -d
```
### Getting Started
### Prerequisites
- Node.js >= 18 - pnpm - Rust >= 1.88 #### System Dependencies **macOS:** No additional dependencies required.
```
sudo apt-get install -y libwebkit2gtk-4.1-dev libgtk-3-dev libappindicator3-dev librsvg2-dev patchel
```
### Development
`make` installs root dependencies when needed and starts the local Tauri desktop development environment.
```
make
```
```
make dev-web       # frontend
make dev-backend   # backend
```
### Build
The installer will be in `src-tauri/target/release/bundle/`.
```
make package
```
### Tech Stack
| Layer | Technology |
| Framework | Tauri 2 |
| Frontend | Vue 3 + TypeScript |
| UI | shadcn-vue + Tailwind CSS |
| Editor | CodeMirror 6 |
| Backend | Rust + sqlx / tiberius / redis-rs / mongodb |
### Documentation
- Official docs — feature guides and tutorials - Plugin development — create plugins and submit Marketplace listings to the correct repository - Database Test L
### Support DBX
DBX is free and open source, but ongoing maintenance, database compatibility testing, infrastructure, and release work require sustained time and resources.
### Contributors
### Community
![LINUX DO](https://linux.do) ![1Panel](https://1panel.cn)
### Star History
### License
Apache-2.0

## Sentences with numbers (verbatim)
- 100+ databases in 25 MB.
- AICodeMirror provides a high-stability official relay service for Claude Code / Codex / Gemini CLI, with enterprise-grade concurrency, fast invoicing, and 7×24 dedicated support.
- Official-channel pricing for Claude Code / Codex / Gemini is as low as 38% / 2% / 9% of list price, with extra discounts on top-ups!
- AICodeMirror offers a special benefit for DBX users: register through this link to enjoy 20% off your first top-up, and enterprise customers up to 25% off.
- Visit AICodeMirror HuaLongAI is a model API relay built for heavy AI developers, offering 100% official-source Codex and Claude models with transparent token-level billing, enterpr
- Visit HuaLongAI UCloud is the first public cloud provider listed on China's STAR Market, with 28 global regions for cloud hosting, databases, and CDN; its AstraFlow platform offers
- 🪶 25 MB, zero runtime bloat No Java JRE.
- New native and agent-driven drivers also cover Databricks, SAP HANA, Teradata, Vertica, Firebird, Exasol, YashanDB, GBase 8a/8s, Databend, RQLite, Turso, InfluxDB, QuestDB, IoTDB, 
- All in a single ~25 MB app.
- ### Query Editor CodeMirror 6 with SQL syntax highlighting, metadata-aware autocomplete, `Cmd+Enter` execution, selected SQL execution, SQL formatting, diagnostics, and 9 editor th
- ### Schema Tools - **Schema browser** — databases, schemas, tables, columns, indexes, foreign keys, triggers, with sidebar search & pin - **Object browser** — grouped procedures, f

## Page blocks (id kind y: text)
b000 header 172: dbx Public Sponsor Notifications Fork2.3k (2.3k) Star25.4k (
b001 star 192: Star25.4k (25.4k)
b002 about 250: About 25 MB lightweight cross-platform database client for 1
b003 files 368: Name Last commit message Last commit date .cargo feat(export
b005 text 2146: 100+ databases in 25 MB. Desktop, Docker, CLI, built-in AI a
b006 text 2146: 100+ databases in 25 MB. Desktop, Docker, CLI, built-in AI a
b015 heading 3459: ❤️ Sponsors
b017 table 3514: rows 0-8 (0 = header) JumpServer is an Open-source Privileged Access Management (P
b019 heading 4477: 🤝 Partners
b021 table 4531: rows 0-1 (0 = header) 1Panel is a modern open-source Linux server management panel
b023 heading 4754: Why DBX?
b025 table 4809: rows 0-2 (0 = header) 🪶 25 MB, zero runtime bloat No Java JRE. No Python venv. No 
b027 heading 5428: Features
b030 heading 5490: 100+ Databases, One Tool
b032 text 5531: MySQL, PostgreSQL, SQLite, Cloudflare D1, Redis, MongoDB, Du
b034 heading 5771: Query Editor
b036 text 5812: CodeMirror 6 with SQL syntax highlighting, metadata-aware au
b038 heading 5908: AI SQL Assistant
b040 text 5949: Describe what you want in plain language — get SQL back. DBX
b042 heading 6045: Data Grid
b044 text 6086: Virtual-scrolled table that handles large result sets. Inlin
b046 heading 6206: Schema Tools
b048 list 6247: Schema browser — databases, schemas, tables, columns, indexe
b050 heading 6515: Data Operations
b052 list 6556: Table import — CSV, Excel Data transfer — migrate between da
b054 heading 6772: Specialized Browsers
b056 list 6813: Redis — key pattern search, batch key operations, command ru
b058 heading 6913: Message Queue & Middleware Consoles
b060 list 6954: Kafka / RocketMQ / RabbitMQ / Pulsar — topics, consumer grou
b062 heading 7082: Plugin System
b064 list 7123: Extensible by design — new connection types and tools arrive
b066 heading 7299: Safety & Connectivity
b068 text 7340: SSH tunnel (key & password) · database and AI proxy settings
b070 heading 7436: Polished UI
b072 text 7477: Dark mode with native title bar sync · 9 editor themes · Eng
b074 heading 7549: AI Agent Integration (MCP)
b076 text 7603: DBX provides a separate Rust-powered MCP server that lets AI
b077 code 7691: npx @dbx-app/mcp-server
b080 text 7759: Add to your .mcp.json:
b081 code 7799: { "mcpServers": { "dbx": { "command": "npx", "args": ["-y", 
b084 text 7945: Manage the connection allowlist and the Read only, Data read
b085 text 8033: For upgrade compatibility, an existing DBX_MCP_ALLOW_WRITES=
b086 text 8121: Windows portable builds need DBX_DATA_DIR in the MCP config,
b087 text 8185: For DBX Web or Docker deployments, point the MCP server at t
b088 code 8249: { "mcpServers": { "dbx": { "command": "npx", "args": ["-y", 
b091 text 8534: Works with Claude Code, Cursor, Windsurf, and any MCP-compat
b092 text 8598: Precompiled native binaries are also published for macOS, Li
b093 text 8686: DBX also provides a dedicated CLI package for terminal, scri
b094 code 8726: npm install -g @dbx-app/cli # or via Homebrew brew tap t8y2/
b097 text 8892: The CLI includes the official DBX Agent Skill. dbx agent set
b098 text 8956: See the MCP server README and CLI README for details.
b100 heading 9004: Install
b102 text 9058: Download the latest release from the Releases page.
b104 code 9138: brew install --cask dbx
b108 code 9246: scoop bucket add dbx https://github.com/t8y2/scoop-bucket sc
b113 code 9374: winget install t8y2.dbx
b116 code 9481: flatpak remote-add --if-not-exists flatpark https://dl.flatp
b119 text 9569: Updates then arrive through the regular flatpak update. See 
b121 heading 9617: Self-Hosted (Docker)
b123 text 9671: For scheduled backups after closing the desktop app or brows
b124 text 9735: DBX provides a web version that can be deployed via Docker. 
b125 code 9799: # The default keeps the key in the persistent /app/data volu
b128 text 9926: This uses the cross-platform dbx-data named volume. Users in
b129 text 9990: For Docker Compose, deploy/docker-compose.yml remains the so
b130 code 10054: docker compose -f deploy/docker-compose.release.yml up -d
b133 code 10122: services: dbx: image: t8y2/dbx:latest # For faster pulls in 
b136 text 10446: Open http://localhost:4224 in your browser. Multi-arch image
b137 text 10486: Connection, plugin, AI, and tunnel credentials are encrypted
b138 text 10670: For production deployments, replace the managed key with a D
b139 text 10782: When running the binary directly, set DBX_DATA_DIR=/var/lib/
b140 text 10846: When upgrading from a release that stored credentials in pla
b141 text 11054: Local CLI and standalone MCP can reuse the existing platform
b142 text 11190: Cross-device exports use a separate sync passphrase and neve
b143 text 11278: For the complete design, migration state machine, implementa
b144 text 11342: To publish DBX under a reverse-proxy context path such as /d
b145 code 11406: environment: - DBX_PUBLIC_BASE_PATH=/dbx
b148 text 11493: When building the frontend yourself with an absolute asset b
b150 heading 11565: Getting Started
b153 heading 11627: Prerequisites
b155 list 11668: Node.js >= 18 pnpm Rust >= 1.88
b157 heading 11772: System Dependencies
b160 text 11848: No additional dependencies required.
b161 text 11888: Linux (Ubuntu/Debian):
b162 code 11928: sudo apt-get install -y libwebkit2gtk-4.1-dev libgtk-3-dev l
b168 text 12116: No additional dependencies required.
b170 heading 12164: Development
b172 code 12205: make
b175 text 12273: make installs root dependencies when needed and starts the l
b176 text 12337: Development builds can run alongside an installed DBX instan
b177 text 12401: Tip DuckDB compilation takes a while. If you're not working 
b179 text 12441: DuckDB compilation takes a while. If you're not working on D
b180 code 12505: # Fast checks (skip DuckDB) make cargo-check-fast make cargo
b181 text 12671: The --no-default-features flag only affects local developmen
b183 code 12783: make dev-web # frontend make dev-backend # backend
b187 code 12911: make docs
b190 text 12979: The official DBX documentation site lives in docs/. If you w
b191 text 13043: Plugin authors should start with Develop and Submit DBX Plug
b192 text 13131: For clean, reproducible local database instances, use the ve
b193 code 13195: make db-list make db-verify DB=mysql@8.4
b196 text 13282: JDBC agent driver development projects live in agents/:
b197 code 13322: cd agents ./gradlew test
b200 text 13410: Build artifacts from agents/drivers/<db-type>/build/libs/ ar
b202 heading 13482: Build
b204 code 13523: make package
b207 text 13591: The installer will be in src-tauri/target/release/bundle/.
b209 heading 13639: Tech Stack
b211 table 13693: rows 0-5 (0 = header) Layer Technology Framework Tauri 2 Frontend Vue 3 + TypeScri
b213 heading 13940: Documentation
b215 list 13994: Official docs — feature guides and tutorials Plugin developm
b217 heading 14182: Support DBX
b219 text 14236: DBX is free and open source, but ongoing maintenance, databa
b220 list 14300: Support DBX — voluntary donations via WeChat or Alipay Spons
b222 heading 14376: Contributors
b226 heading 15580: Community
b231 heading 15728: Star History
b235 heading 16347: License
b238 media 2186: DBX screenshot
b239 media 2912: 
b240 media 2914: 
b241 media 3183: 
b242 media 3182: 
b243 media 14430: 
b244 media 15782: Star History Chart

## Media
m00 block b238 still 1792x896: DBX screenshot
m01 block b239 still 3014x1886: 
m02 block b240 still 3018x1874: 
m03 block b241 still 3018x1876: 
m04 block b242 still 3018x1882: 
m05 block b243 still NonexNone: 
m06 block b244 still NonexNone: Star History Chart