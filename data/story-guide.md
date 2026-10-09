# Writing story.json for a repo reel

The reel is a 9:16 English video over 60 s about one GitHub repository: the real repo page in 3D, a narrator, word captions,
music, 3D explainer scenes. The story is the product. Its source of truth is `repo/digest.md` (README by section, page blocks
with ids, media with ids, sentences with numbers). Never invent a fact, a feature or a number.

Arc: hook = the most surprising *sourced* number in the first 2 s; what it is; one 3D scene that shows how it works;
proof (numbers); how to start; end. 11-13 lines, 150-190 words in all: 65-80 s (the narrator speaks ~2.5 words/s). It
must stay over 60 s; longer than 80 s loses viewers.
Copy numbers verbatim from the digest. English only. Short spoken sentences, no marketing filler.
Social rules (Belkis, 06.10.2026): attention, value, trust, then a call to action. The hook lands its number in the
first 2 s; the middle gives value (what it does, how it works) and trust (benchmarks, safety, stars); the line before
`end` asks for a share or a save ("Send this to someone who ...", "Save this for ..."): shares weigh most with
non-followers. Never ask to follow: every reel ends on the channel outro, which does that.

```json
{"repo": "https://github.com/o/r", "accent": "#34d399", "mood": "dark-tech|bright-tech|cinematic|lo-fi",
 "keys": ["Name", "Python"],
 "lines": [{"id": "hook", "say": "This tiny engine / beats an 8B-parameter LLM. / And it's 11× faster.",
            "shots": [{"page": "name"}, {"at": "beats", "page": "b016"}, {"at": "11×", "stat": "11×", "sub": "optional line"}]}]}
```

- `say`: what the captions show; `/` marks a caption break (at most 4 words per part). `keys`: words drawn in the accent.
- A shot starts at `"at"` (a word of that line exactly as written incl. punctuation, `"word#2"` for its 2nd occurrence, or
  seconds after the line start), else at the line start. A line without shots keeps the previous camera.
- `accent`: a hue at least 40° away from the last three reels (Belkis, 06.10.2026: "not always orange"; check
  warns) - the repo's brand colour or its main language's GitHub colour when that hue is free, else any clear colour that reads on dark. `mood` picks the music.
- Shots (page blocks are ids from the digest, aliases `name` `header` `star` `files` `about` - only when the digest lists
  such a block - or `"~text prefix"` = the block whose text STARTS with it, as listed under "Page blocks" in the digest; words inside a
  block or a table row never match):
  - `{"page": "b025", "rows": [4, 4]}` table rows (0 = header) · `"part": [0, 0.2]` a vertical slice of a block
  - `{"code": "b036", "steps": [{"lines": [1, 7], "at": "Download."}, ...]}` code lines light up on their words
  - `{"stat": "0.45 s", "sub": "first answer · ORT: 2.06 s"}` a huge number over the dimmed page (sub at most ~40 chars)
  - `{"media": {"id": "m01", "from": 1, "to": 5.4}}` a README image/animation on a 3D screen (seconds of the source)
  - `{"flow": {"input": {"label": "...", "title": ["..."], "body": ["..."]}, "stream": "word", "pulse": "word",
    "outputs": [{"label": "department", "type": "choice", "value": "billing", "sub": "0.99", "at": "word"}]}}`
  - `{"grid": {"tiles": [["word", group], ...], "pulse": "word", "results": [{"tile": 9, "text": "billing", "at": "word"}]}}`
  - `{"bars": {"items": [{"label": "...", "value": 68, "show": "68/s", "at": "word"}, ...], "note": "...", "hot": 0}}`
  - `{"end": true}` logo (or repo name) over the header, URL - the last line only.

Rules: real values only (from the README) on cards; a README animation plays when there is one; something new every
1.5-3 s (two or three shots per line); never two 3D scenes (media, flow, grid, bars) back to back without a page, code or
stat shot between them; never the same pattern (e.g. page then media) in two lines in a row; table `rows` only on blocks the
digest shows as tables; the hook's first shot is `{"page": "name"}` (every reel opens on the repo header: the covers on the
@github_radar grid must match); flow outputs come on words after the `pulse` word (the input card dissolves until then and
would sit under the first card); light README screenshots and logos are dimmed under the bloom threshold by the engine: pick the one with visible
structure (a graph, a UI with content), not a near-white page.
