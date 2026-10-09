# h4ckf0r0day/obscura
The headless browser for AI agents and web scraping
stars 28716 · forks 2133 · Rust · licence Apache-2.0 · release v0.2.4 (2026-10-04) · pushed 2026-10-08 · topics antidetect, antidetect-browser, browser, browser-automation, cdp, headless, playwright, puppeteer
languages {'Rust': 95.4, 'Python': 3.1, 'HTML': 1.2, 'JavaScript': 0.1, 'Shell': 0.1}

## README by section
### (intro)
Obscura The open-source headless browser for AI agents and web scraping.
### Why Obscura over headless Chrome?
Obscura inspired Cloudflare Kitesurf’s first prototype Cloudflare began by porting Obscura to Workers while developing its new agent-first browser.
| Metric | Obscura | Headless Chrome |
| Memory | **30 MB** | 200+ MB |
| Binary size | **~70 MiB** | 300+ MB |
| Anti-detect | **Built-in** | None |
| Page load | **85 ms** | ~500 ms |
| Startup | **Instant** | ~2s |
|...
### Obscura Cloud
We are working on **Obscura Cloud** the hosted version, with managed infrastructure, residential proxies, and dedicated support.
### Open Source Support
### Sponsors
**Obscura** is supported by organizations helping us build independent open-source browser infrastructure.
### Install
### Download
Grab the latest binary from Releases: No Chrome, no Node.js, no dependencies.
| Archive suffix | Rendering | Stealth transport |
| none | Yes | No |
| `-stealth` | Yes | Yes |
| `-no-render` | No | No |
| `-no-render-stealth` | No | Yes |
```
# Linux x86_64
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-linux.tar.gz
tar xzf obscura-x86_64-linux.tar.gz
./obscura fetch https://example.com --eval "document.title"
...
```
### Docker
Image on Docker Hub.
```
docker run -d --name obscura -p 127.0.0.1:9222:9222 \
  -e OBSCURA_CDP_TOKEN="$(openssl rand -hex 32)" \
  h4ckf0r0day/obscura
```
### Build from source
Requires Rust 1.75+ (rustup.rs).
```
git clone https://github.com/h4ckf0r0day/obscura.git
cd obscura

# Rendering
...
```
```
sudo apt-get install build-essential cmake clang libclang-dev llvm-dev
```
### Quick Start
### Fetch a page
obscura fetch http://127.0.0.1:3000 --allow-private-network --dump text
```
# Get the page title
obscura fetch https://example.com --eval "document.title"

# Extract all links
...
```
### Works on any subcommand, e.g. the CDP server for local Puppeteer/Playwright:
obscura serve --port 9222 --allow-private-network
```

See [docs/Environment-variables.md](docs/Environment-variables.md) for the
full allow/deny rules (DNS-resolution-time checks included).
```
### Rendering
Official release archives and the Docker image include the rendering engine.
```
await page.setViewport({ width: 1440, height: 1000 });
await page.goto('https://example.com', { waitUntil: 'load' });
await page.screenshot({ path: 'page.png', fullPage: true });
await page.pdf({ path: 'page.pdf', format: 'A4', printBackground: true });
```
### Start the CDP server
```
obscura serve --port 9222

# With stealth mode (anti-detection + tracker blocking)
obscura serve --port 9222 --stealth
```
### Scrape in parallel
```
obscura scrape url1 url2 url3 ... \
  --concurrency 25 \
  --eval "document.querySelector('h1').textContent" \
  --format json
...
```
### Puppeteer / Playwright
### Puppeteer
```
npm install puppeteer-core
```
```
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.connect({
  browserWSEndpoint: 'ws://127.0.0.1:9222/devtools/browser',
...
```
### Playwright
```
npm install playwright-core
```
```
import { chromium } from 'playwright-core';

const browser = await chromium.connectOverCDP({
  endpointURL: 'ws://127.0.0.1:9222',
...
```
### Form submission & login
```
await page.goto('https://quotes.toscrape.com/login');
await page.evaluate(() => {
  document.querySelector('#username').value = 'admin';
  document.querySelector('#password').value = 'admin';
...
```
### Benchmarks
Page load: The full benchmark suite (WPT conformance, obstacle course, real-world corpus, and vs-Chrome speed) lives in a separate repo: https://github.com/h4ck
| Page | Obscura | Chrome |
| Static HTML | **51 ms** | ~500 ms |
| JS + XHR + fetch | **84 ms** | ~800 ms |
| Dynamic scripts | **78 ms** | ~700 ms |
### Stealth Mode
Build with `--features render,stealth`, then enable stealth at runtime with the global `--stealth` flag.
### Anti-fingerprinting
- Per-session fingerprint randomization (GPU, screen, canvas, audio, battery) - Realistic `navigator.userAgentData` (Chrome 145, high-entropy values) - `event.i
### Tracker Blocking
- 3,520 domains blocked - Blocks analytics, ads, telemetry, and fingerprinting scripts - Prevents trackers from loading entirely - Enabled automatically with `-
### CDP API
Obscura implements the Chrome DevTools Protocol for Puppeteer/Playwright compatibility.
| Domain | Methods |
| **Target** | createTarget, closeTarget, attachToTarget, createBrowserContext, disposeBrowserContext |
| **Page** | navigate, getFrameTree, lifecycleEvents, captureScreenshot, start/stopScreencast, printToPDF |
| **Runtime** | evaluate, callFunctionOn, getProperties, addBinding |
| **DOM** | getDocument, querySelector, querySelectorAll, getOuterHTML, resolveNode |
| **Network** | enable, setCookies, getCookies, setExtraHTTPHeaders, setUserAgentOverride |
|...
### CLI Reference
### Tuning V8
Obscura embeds V8 directly.
```
obscura --v8-flags "--max-old-space-size=4096" fetch <url>
```
### Heavy SPAs (script execution budget)
Obscura caps the page's script-execution phase so one slow or hung page cannot stall a worker.
```
OBSCURA_SCRIPT_DEADLINE_MS=60000 obscura serve --port 9222
```
```
OBSCURA_MODULE_BUDGET_MS=10000 obscura serve --port 9222
```
### `obscura serve`
Start a CDP WebSocket server.
| Flag | Default | Description |
| `--port` | `9222` | WebSocket port |
| `--proxy` | — | HTTP/SOCKS5 proxy URL |
| `--stealth` | off | Enable anti-detection + tracker blocking |
| `--workers` | `1` | Number of parallel worker processes |
| `--font-dir` | — | Recursively load fonts once per worker (repeatable; render build) |
|...
### `obscura fetch `
Fetch and render a single page.
| Flag | Default | Description |
| `--dump` | `html` | Output: `html`, `text`, `links`, `markdown`, `assets` (NDJSON of every sub-resource URL the page references)
| `--eval` | — | JavaScript expression to evaluate |
| `--wait-until` | `load` | Wait: `load`, `domcontentloaded`, `networkidle0` |
| `--timeout` | `30` | Maximum navigation time in seconds |
| `--wait` | adaptive, up to `5` | Post-load settling; an explicit value is a fixed delay in seconds |
|...
### `obscura scrape `
Scrape multiple URLs in parallel with worker processes.
| Flag | Default | Description |
| `--concurrency` | `10` | Parallel workers |
| `--eval` | — | JS expression per page |
| `--format` | `json` | Output: `json` or `text` |
| `--quiet` | off | Suppress scrape progress on stderr |
| `--proxy` | — | Inherited global HTTP/SOCKS5 proxy URL for all workers |
### MCP (Model Context Protocol)
Obscura ships an MCP server that exposes browser automation tools to AI agents (Claude Desktop, Cursor, etc.).
### Start
**stdio** (default) — for Claude Desktop and MCP clients that launch a subprocess: **HTTP** — for clients that connect over the network: Optional flags (both tr
| Flag | Description |
| `--proxy ` | HTTP/SOCKS5 proxy |
| `--user-agent ` | Custom User-Agent string |
| `--stealth` | Enable anti-detection mode |
```
obscura mcp
```
```
obscura mcp --http --port 8080
# endpoint: http://127.0.0.1:8080/mcp
```
### Claude Desktop config
```
{
  "mcpServers": {
    "obscura": {
      "command": "obscura",
...
```
### Tools
The MCP server exposes still-image and PDF output.
| Tool | Description |
| `browser_navigate` | Navigate to a URL (`url`, optional `waitUntil`: `load` / `domcontentloaded` / `networkidle0`) |
| `browser_snapshot` | Return the current page URL, title, readable body text, and element references |
| `browser_screenshot` | Return the current page as an MCP PNG image (render-enabled build) |
| `browser_pdf` | Return the current page as an embedded PDF resource (render-enabled build) |
| `browser_click` | Click by current snapshot reference or CSS selector |
|...
### Integrations
- **Hermes agent plugin**: run Hermes agent browser tasks on Obscura.
### License
Apache 2.0 ---

## Sentences with numbers (verbatim)
- It runs real JavaScript via V8, supports the Chrome DevTools Protocol, and acts as a drop-in replacement for headless Chrome with Puppeteer and Playwright.
- | Metric | Obscura | Headless Chrome | |--------------|--------------|------------------| | Memory | **30 MB** | 200+ MB | | Binary size | **~70 MiB** | 300+ MB | | Anti-detect | *
- ZIP targeting 99.9% uptime IP filtering: all proxies have fraud score &lt;97% No KYC required Unique free tools: Proxy Bandwidth Checker, Meta Tag Checker, IP Lookup and others!
- 🎁 Special codes for Obscura users: OBSCURA35 - 35% off to Mobile and Residential Proxies OBSCURA40 - 40% off to ISP (Static) Proxies 🚀 Obscura × ProxyEmpire Using Obscura for AI ag
- 🌍 30M+ residential IPs in 170+ countries 📱 4G/5G mobile proxies 🔄 Rotating & sticky sessions 🎯 City, region & ISP targeting 🔐 HTTP, HTTPS & SOCKS5 support 🎁 Use code OBSCURA35 for 
- 💸 Try it free for 30 days.
- 🎁 Use code OBSCURA25 for 25% off your first month.
- Multi-stage build on `distroless/cc:nonroot` — no shell, no package manager, runs as uid 65532, ~57 MB compressed.
- First build takes ~5 min (V8 compiles from source, cached after).
- ### Start the CDP server ### Scrape in parallel ## Puppeteer / Playwright ### Puppeteer ### Playwright ### Form submission & login ## Benchmarks Page load: | Page | Obscura | Chrom
- ### Anti-fingerprinting - Per-session fingerprint randomization (GPU, screen, canvas, audio, battery) - Realistic `navigator.userAgentData` (Chrome 145, high-entropy values) - `eve
- Response bodies over the cache limit (`OBSCURA_NETWORK_BODY_BUFFER_BYTES`, default 2 MiB) are not retained, so raise that limit when you intend to stream large downloads.
- The default budget is 30s; pages that finish sooner return immediately, so the cap only affects pages that keep running.
- Raise the budget with `OBSCURA_SCRIPT_DEADLINE_MS` (milliseconds), and pair it with a matching navigation timeout in your CDP client: Modules that enhance an already-rendered page 

## Page blocks (id kind y: text)
b000 header 172: obscura Public Notifications Fork2.1k (2.1k) Star28.7k (28.7
b001 star 192: Star28.7k (28.7k)
b002 about 250: About The headless browser for AI agents and web scraping ob
b003 files 368: Name Last commit message Last commit date .cargo Improve Pla
b007 heading 1518: Obscura
b011 text 1701: The open-source headless browser for AI agents and web scrap
b013 heading 1773: Native rendering is here. No Chromium required. 🎉
b015 text 1814: Capture screenshots, screencast live pages, and export PDFs 
b016 text 1887: Obscura is a headless browser engine written in Rust, built 
b018 heading 1983: Why Obscura over headless Chrome?
b020 table 2024: rows 0-7 (0 = header) Metric Obscura Headless Chrome Memory 30 MB 200+ MB Binary s
b021 table 2337: rows 0-0 (0 = header) Obscura inspired Cloudflare Kitesurf’s first prototype Cloud
b023 heading 2471: Obscura Cloud
b025 text 2525: We are working on Obscura Cloud the hosted version, with man
b026 text 2589: The open-source engine stays Apache-2.0, fully featured. No 
b027 text 2629: Get on the waitlist → 📅 Book a demo →
b029 heading 2701: Open Source Support
b033 heading 2797: Sponsors
b035 text 2851: Obscura is supported by organizations helping us build indep
b036 text 2915: Want to sponsor? Email hello@obscura.sh.
b037 table 2955: rows 0-2 (0 = header) NodeMaven: The most efficient proxy provider for Web Scrapin
b039 heading 3979: Install
b042 heading 4041: Download
b044 text 4082: Grab the latest binary from Releases:
b045 code 4122: # Linux x86_64 curl -LO https://github.com/h4ckf0r0day/obscu
b048 text 4604: No Chrome, no Node.js, no dependencies. Release archives inc
b049 table 4668: rows 0-4 (0 = header) Archive suffix Rendering Stealth transport none Yes No -stea
b050 text 4870: Linux release builds target Ubuntu 22.04 so the downloaded b
b052 heading 4942: Docker
b054 code 4983: docker run -d --name obscura -p 127.0.0.1:9222:9222 \ -e OBS
b057 text 5090: Image on Docker Hub. Multi-stage build on distroless/cc:nonr
b059 heading 5186: Build from source
b061 code 5227: git clone https://github.com/h4ckf0r0day/obscura.git cd obsc
b064 text 5551: Requires Rust 1.75+ (rustup.rs). First build takes ~5 min (V
b065 code 5639: sudo apt-get install build-essential cmake clang libclang-de
b068 text 5707: The rendering build uses rustls. The rendering-and-stealth b
b070 heading 5779: Quick Start
b073 heading 5841: Fetch a page
b075 code 5882: # Get the page title obscura fetch https://example.com --eva
b078 text 6817: See docs/Environment-variables.md for the full allow/deny ru
b080 code 6857: ## Rendering Official release archives and the Docker image 
b082 text 7161: The current implementation covers block, inline, flex, grid,
b084 heading 7305: Start the CDP server
b086 code 7346: obscura serve --port 9222 # With stealth mode (anti-detectio
b090 heading 7481: Scrape in parallel
b092 code 7522: obscura scrape url1 url2 url3 ... \ --concurrency 25 \ --eva
b096 heading 7775: Puppeteer / Playwright
b099 heading 7837: Puppeteer
b101 code 7878: npm install puppeteer-core
b104 code 7946: import puppeteer from 'puppeteer-core'; const browser = awai
b108 heading 8317: Playwright
b110 code 8358: npm install playwright-core
b113 code 8426: import { chromium } from 'playwright-core'; const browser = 
b117 heading 8699: Form submission & login
b119 code 8740: await page.goto('https://quotes.toscrape.com/login'); await 
b123 heading 8934: Benchmarks
b126 table 9028: rows 0-3 (0 = header) Page Obscura Chrome Static HTML 51 ms ~500 ms JS + XHR + fet
b127 text 9193: The full benchmark suite (WPT conformance, obstacle course, 
b129 heading 9265: Stealth Mode
b131 text 9319: Build with --features render,stealth, then enable stealth at
b133 heading 9415: Anti-fingerprinting
b135 list 9456: Per-session fingerprint randomization (GPU, screen, canvas, 
b137 heading 9644: Tracker Blocking
b139 list 9685: 3,520 domains blocked Blocks analytics, ads, telemetry, and 
b141 heading 9817: CDP API
b143 text 9871: Obscura implements the Chrome DevTools Protocol for Puppetee
b144 table 9911: rows 0-10 (0 = header) Domain Methods Target createTarget, closeTarget, attachToTar
b145 text 10407: To download a large resource without one giant Network.getRe
b147 heading 10527: CLI Reference
b150 heading 10589: Tuning V8
b152 text 10630: Obscura embeds V8 directly. Use --v8-flags to pass raw flags
b153 code 10718: obscura --v8-flags "--max-old-space-size=4096" fetch <url>
b157 heading 10794: Heavy SPAs (script execution budget)
b159 text 10835: Obscura caps the page's script-execution phase so one slow o
b160 code 10971: OBSCURA_SCRIPT_DEADLINE_MS=60000 obscura serve --port 9222
b163 text 11039: Modules that enhance an already-rendered page have a separat
b164 code 11127: OBSCURA_MODULE_BUDGET_MS=10000 obscura serve --port 9222
b167 text 11195: An unmounted SPA shell already gives its app modules the ful
b169 heading 11291: obscura serve
b171 text 11332: Start a CDP WebSocket server.
b172 table 11372: rows 0-6 (0 = header) Flag Default Description --port 9222 WebSocket port --proxy 
b173 text 11648: With multiple workers, exited children are reaped and restar
b175 heading 11744: obscura fetch <URL>
b177 text 11785: Fetch and render a single page.
b178 table 11825: rows 0-11 (0 = header) Flag Default Description --dump html Output: html, text, lin
b180 heading 12390: obscura scrape <URL...>
b182 text 12431: Scrape multiple URLs in parallel with worker processes.
b183 table 12471: rows 0-5 (0 = header) Flag Default Description --concurrency 10 Parallel workers -
b185 heading 12718: MCP (Model Context Protocol)
b187 text 12773: Obscura ships an MCP server that exposes browser automation 
b189 heading 12845: Start
b191 text 12886: stdio (default) — for Claude Desktop and MCP clients that la
b192 code 12926: obscura mcp
b195 text 12994: HTTP — for clients that connect over the network:
b196 code 13034: obscura mcp --http --port 8080 # endpoint: http://127.0.0.1:
b199 text 13121: Optional flags (both transports):
b200 table 13161: rows 0-3 (0 = header) Flag Description --proxy <URL> HTTP/SOCKS5 proxy --user-agen
b202 heading 13334: Claude Desktop config
b204 code 13375: { "mcpServers": { "obscura": { "command": "obscura", "args":
b208 heading 13589: Tools
b210 table 13630: rows 0-14 (0 = header) Tool Description browser_navigate Navigate to a URL (url, op
b211 text 14298: The MCP server exposes still-image and PDF output. Use CDP w
b213 heading 14370: Integrations
b215 list 14424: Hermes agent plugin: run Hermes agent browser tasks on Obscu
b217 heading 14520: License

## Media