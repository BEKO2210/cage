# chenglou/pretext
Fast, accurate & comprehensive text measurement & layout
stars 50736 · forks 2751 · TypeScript · licence NOASSERTION · release None () · pushed 2026-10-08 · topics 
languages {'TypeScript': 67.5, 'C': 18.3, 'C++': 11.6, 'HTML': 2.3, 'Swift': 0.3}

## README by section
### Pretext
Pure JavaScript/TypeScript library for multiline text measurement & layout.
### Installation
```
npm install @chenglou/pretext
```
### Demos
The demos are exemplary API usage patterns we encourage you to read.
### API
Pretext serves 2 use cases:
### 1. Measure a paragraph's height _without ever touching DOM_
`prepare()` does the one-time work: normalize whitespace, segment the text at its break opportunities, measure the segments with canvas, and return an opaque ha
```
import { prepare, layout } from '@chenglou/pretext'

const prepared = prepare('AGI 春天到了. بدأت الرحلة 🚀‎', '16px Inter')
const { height, lineCount } = layout(prepared, 320, 20) // pure arithmetic. No DOM layout & reflow!
```
```
const prepared = prepare(textareaValue, '16px Inter', { whiteSpace: 'pre-wrap' })
const { height } = layout(prepared, textareaWidth, 20)
// A <textarea> shows one more line than this when its value is empty or ends with \n

...
```
### 2. Lay out the paragraph lines manually yourself
Switch out `prepare` with `prepareWithSegments` (the APIs that return a line's text need it: `layoutWithLines()`, `layoutNextLine()`, `materializeLineRange()`),
```
import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext'

const prepared = prepareWithSegments('AGI 春天到了. بدأت الرحلة 🚀', '18px "Helvetica Neue"')
const { lines } = layoutWithLines(prepared, 320, 26) // 320px max width, 26px line height
...
```
```
import { measureLineStats, walkLineRanges } from '@chenglou/pretext'

const { lineCount, maxLineWidth } = measureLineStats(prepared, 320)
let maxW = 0
...
```
### API Glossary
Use-case 1 APIs: Use-case 2 APIs: Helper for rich-text inline flow: Other helpers: Notes: - `LayoutCursor` is a segment/grapheme cursor, not a raw string offset
```
prepare(text: string, font: string, options?: { whiteSpace?: 'normal' | 'pre-wrap', wordBreak?: 'nor
layout(prepared: PreparedText, maxWidth: number, lineHeight: number): { height: number, lineCount: n
```
```
prepareWithSegments(text: string, font: string, options?: { whiteSpace?: 'normal' | 'pre-wrap', word
layoutWithLines(prepared: PreparedTextWithSegments, maxWidth: number, lineHeight: number): { height:
walkLineRanges(prepared: PreparedText, maxWidth: number, onLine: (line: LayoutLineRange) => void): n
measureLineStats(prepared: PreparedText, maxWidth: number): { lineCount: number, maxLineWidth: numbe
...
```
### Caveats
Pretext doesn't try to be a full font rendering engine (yet?).
### Develop
See DEVELOPMENT.md for the demo server, engine data and releases.
### Credits
Sebastian Markbage first planted the seed with text-layout last decade.

## Sentences with numbers (verbatim)
- ## API Pretext serves 2 use cases: ### 1.
- For a size not known yet, prepare with a placeholder and again when it arrives; for an image capped at `max-width: 100%`, pass `min(its width, the paragraph's width)` and prepare a
- Set `-webkit-text-size-adjust: 100%` on the page.

## Page blocks (id kind y: text)
b000 header 172: pretext Public Notifications Fork2.8k (2.8k) Star50.7k (50.7
b001 star 192: Star50.7k (50.7k)
b002 about 250: About Fast, accurate & comprehensive text measurement & layo
b003 files 368: Name Last commit message Last commit date .cursor/rules Name
b006 heading 1531: Pretext
b008 text 1598: Pure JavaScript/TypeScript library for multiline text measur
b009 text 1662: Pretext side-steps the need for DOM measurements (e.g. getBo
b011 heading 1782: Installation
b013 code 1836: npm install @chenglou/pretext
b017 heading 1912: Demos
b019 text 1966: The demos are exemplary API usage patterns we encourage you 
b021 heading 2134: API
b023 text 2188: Pretext serves 2 use cases:
b025 heading 2236: 1. Measure a paragraph's height without ever touching DOM
b027 code 2277: import { prepare, layout } from '@chenglou/pretext' const pr
b030 text 2404: prepare() does the one-time work: normalize whitespace, segm
b031 text 2516: If you want textarea-like text where ordinary spaces, \t tab
b032 code 2580: const prepared = prepare(textareaValue, '16px Inter', { whit
b035 text 2766: Other prepare() options are { wordBreak: 'keep-all' } for CS
b036 text 2830: The returned height is the crucial last piece for unlocking 
b037 list 2870: proper virtualization/occlusion without guesstimates & cachi
b038 text 3042: The same prepare() handle also works with the APIs below tha
b040 heading 3138: 2. Lay out the paragraph lines manually yourself
b042 text 3179: Switch out prepare with prepareWithSegments (the APIs that r
b043 list 3243: layoutWithLines() gives you all the lines at a fixed width:
b044 code 3283: import { prepareWithSegments, layoutWithLines } from '@cheng
b047 list 3429: measureLineStats() and walkLineRanges() give you line counts
b048 code 3493: import { measureLineStats, walkLineRanges } from '@chenglou/
b051 text 3660: Size an element to Math.ceil(maxW), capped at the maxWidth y
b052 list 3772: layoutNextLineRange() lets you route text one row at a time 
b053 code 3812: import { layoutNextLineRange, materializeLineRange, prepareW
b056 text 4195: See the /demos/dynamic-layout demo for a richer example, and
b057 text 4283: For hyphenation, insert soft hyphens before calling prepare(
b058 text 4395: To lay out text with mixed fonts, code spans, mentions, chip
b059 code 4459: import { materializeRichInlineLineRange, prepareRichInline, 
b062 text 4763: Pass a flat list of items. For an image, a custom emoji, a f
b063 text 4971: A line count is a height only while no item grows its line. 
b064 text 5107: For white-space: pre-wrap or word-break: keep-all on the par
b066 heading 5299: API Glossary
b069 code 5380: prepare(text: string, font: string, options?: { whiteSpace?:
b073 code 5507: prepareWithSegments(text: string, font: string, options?: { 
b076 text 6205: Helper for rich-text inline flow:
b077 code 6245: prepareRichInline(items: Array<RichInlineItem | RichInlineBo
b081 code 7338: clearCache(): void // clears Pretext's shared internal cache
b085 list 7466: LayoutCursor is a segment/grapheme cursor, not a raw string 
b087 heading 8482: Caveats
b089 text 8536: Pretext doesn't try to be a full font rendering engine (yet?
b090 list 8576: white-space: normal and pre-wrap word-break: normal and keep
b092 heading 10040: Develop
b094 text 10094: See DEVELOPMENT.md for the demo server, engine data and rele
b096 heading 10142: Credits
b098 text 10196: Sebastian Markbage first planted the seed with text-layout l

## Media