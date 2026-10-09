# storytold/photocraft
An open-source, clean-room reimplementation of Adobe Photoshop in pure Rust
stars 14646 · forks 1939 · Rust · licence Apache-2.0 · release v0.3.0 (2026-10-07) · pushed 2026-10-07 · topics adobe, adobe-photoshop-2026, adobe-photoshop-2026-ai, art, image-editing, image-editing-software, image-editor, images
languages {'Rust': 99.1, 'WGSL': 0.4, 'Shell': 0.3, 'PowerShell': 0.1, 'HTML': 0.0}

## README by section
### (intro)
PhotoCraft Image editing; an open-source, clean-room reimplementation of Adobe Photoshop, rebuilt in pure Rust.
### Features
Every screenshot here is the real app at work on public-domain art, rendered offscreen through its control channel.
### Everything in the box
🧰 34 tools Move · Rectangular and Elliptical Marquee · Lasso · Polygonal Lasso · Magic Wand · Quick Selection · Object Selection · Crop · Eyedropper · Brush · P
### PSD without compromise
PhotoCraft's PSD support is a standalone crate written from Adobe's public specification and tested against a corpus of real-world files.
### Built for agents
Every menu item, tool and dialog runs a command from one registry of 500+ commands.
```
# Headless: open, edit, save
photocraft-cli run wave.psd \
  --cmd filter.sharpen.smartSharpen     --params '{"amount":80}' \
  --cmd layer.newAdjustmentLayer.curves --params '{"points":[[0,0],[64,48],[192,212],[255,255]]}' \
...
```
### Under the hood
- **Engine first:** a pure-data document model and a command engine, with a thin egui UI on top.
### Get started
Japanese fonts for the UI and Type tool come from craft-fonts, an optional build input (desktop release builds always include it).
```
git clone https://github.com/storytold/photocraft
cd photocraft
cargo run --release -p photocraft -- image.psd   # the desktop app
cargo test --workspace                           # the test suite
```
```
git clone https://github.com/storytold/craft-fonts ../craft-fonts
CRAFT_FONTS_DIR="$PWD/../craft-fonts" cargo run --release -p photocraft
```
### Documentation
Developer, architecture, automation, format, and security documentation is maintained in the PhotoCraft documentation book.
### Security
Security architecture, threat modeling, parser hardening, fuzzing, and vulnerability reporting are covered in the security documentation and the repository secu
### Test corpora
PhotoCraft is tested against real files: our own Photoshop-authored oracle PSDs in photocraft-corpus plus the psd-tools, ag-psd and PngSuite sets, pinned and sh
### The Crafting Apps
PhotoCraft is one of the **Crafting Apps**: free, open-source creative tools from the ArtCraft team, each written from scratch in Rust and each able to stand on
| | App | What it's for | Code | Learn more |
| | **PhotoCraft** | **Image editing: layers, masks, type and real PSD files · you are here** | GitHub | Website |
| | **VectorCraft** | Vector illustration | GitHub | Website |
| | **FilmCraft** | Video editing, color and sound | GitHub | Website |
| | **LightCraft** | Photo library and raw development | GitHub | Website |
| | **PrintCraft** | Reading, organizing and protecting PDFs | GitHub | Website |
|...
### License and credits
PhotoCraft is dual-licensed under MIT or Apache-2.0, at your option.
### Star history
![Star History Chart](https://www.star-history.com/?repos=storytold%2Fphotocraft&type=date&legend=top-left)

## Sentences with numbers (verbatim)
- Re-saving keeps the render of 307 of the 309 psd-tools test files.
- 16 adjustment layers that also apply directly to pixels, including Curves with per-channel editing, Levels with a live histogram, Black &amp; White, Channel Mixer, Gradient Map, Ph
- 116 of 116 shape layers in our PSD corpus match Photoshop's pixels.
- Large-radius blurs use running-sum box passes across all cores: a radius-180 Gaussian on 3.6 MP takes under a second.
- ## Everything in the box 🧰 34 tools Move · Rectangular and Elliptical Marquee · Lasso · Polygonal Lasso · Magic Wand · Quick Selection · Object Selection · Crop · Eyedropper · Brus
- 🗃️ Layers, done properly Groups, clipping masks, pixel and vector masks, fill layers (solid, gradient and pattern), adjustment layers, live smart objects with smart filters and los
- 🎨 Any colour, any depth RGB, Grayscale, CMYK and Lab documents at 8, 16 and 32 bits per channel.
- 🗂️ Formats PSD and PSB, plus PNG, JPEG, TIFF, WebP, GIF, BMP, TGA, ICO, QOI, PNM, OpenEXR, Radiance HDR and AVIF, with symmetric read and write at 8, 16 and 32 bits, HEIC photos fr
- - **Faithful round trips:** opening and re-saving a document renders the same for 307 of the 309 files in the psd-tools test set and 169 of 170 in our mixed ag-psd/psd-tools set (`
- ## Built for agents Every menu item, tool and dialog runs a command from one registry of 500+ commands.
- Layering is enforced at build time across 24 crates.
- - **Tested:** more than 1,700 tests, including PSD round trips, synthetic generators, compositor oracles and multi-depth checks.

## Page blocks (id kind y: text)
b000 header 172: photocraft Public Notifications Fork1.9k (1.9k) Star14.6k (1
b001 star 192: Star14.6k (14.6k)
b002 about 250: About An open-source, clean-room reimplementation of Adobe P
b003 files 368: Name Last commit message Last commit date .cargo one-shot .g
b007 heading 1665: PhotoCraft
b009 text 1731: Image editing; an open-source, clean-room reimplementation o
b012 text 1937: PhotoCraft on getartcraft.com · ArtCraft · All Crafting Apps
b014 text 2001: A caption card with a drop shadow, live type, and Vibrance a
b015 text 2596: Note ArtCraft is a community of artists from all walks of li
b017 text 2636: ArtCraft is a community of artists from all walks of life. D
b018 text 2708: Features · Everything in the box · PSD · Agents · Under the 
b020 table 2772: rows 0-0 (0 = header) 🎛️ Familiar by design The menus, shortcuts, panels and tools
b023 heading 3132: Features
b025 text 3186: Every screenshot here is the real app at work on public-doma
b026 table 3250: rows 0-3 (0 = header) Levels and Vibrance adjustment layers, with the live Histogr
b029 heading 6099: Everything in the box
b031 table 6153: rows 0-1 (0 = header) 🧰 34 tools Move · Rectangular and Elliptical Marquee · Lasso
b034 heading 7060: PSD without compromise
b036 text 7114: PhotoCraft's PSD support is a standalone crate written from 
b037 list 7178: Faithful round trips: opening and re-saving a document rende
b039 heading 7498: Built for agents
b041 text 7553: Every menu item, tool and dialog runs a command from one reg
b042 code 7641: # Headless: open, edit, save photocraft-cli run wave.psd \ -
b045 text 7964: The desktop app also offers an authenticated, loopback-only 
b047 heading 8060: Under the hood
b049 list 8115: Engine first: a pure-data document model and a command engin
b051 heading 8423: Get started
b053 code 8477: git clone https://github.com/storytold/photocraft cd photocr
b056 text 8604: Japanese fonts for the UI and Type tool come from craft-font
b057 code 8668: git clone https://github.com/storytold/craft-fonts ../craft-
b060 text 8755: New contributors and AI agents: start with AGENTS.md, then d
b061 text 8795: Installers for macOS, Windows, Linux, FreeBSD and the web ar
b062 code 8883: flatpak install --user photocraft-<version>-linux-x86_64.fla
b065 text 8970: On macOS, the command-line tool comes as photocraft-cli-<ver
b066 code 9082: ditto -x -k photocraft-cli-<version>-macos-universal.zip . s
b069 text 9190: On FreeBSD 14 (x86_64), the release has a tarball laid out l
b070 code 9254: pkg install libxkbcommon wayland libX11 libXcursor libXrandr
b073 text 9361: Maintainers: docs/releasing.md explains how releases are bui
b074 text 9401: Important Status: PhotoCraft is in early alpha, and we want 
b076 text 9441: Status: PhotoCraft is in early alpha, and we want to be stra
b078 heading 9665: Documentation
b080 text 9719: Developer, architecture, automation, format, and security do
b082 heading 9791: Security
b084 text 9845: Security architecture, threat modeling, parser hardening, fu
b086 heading 9917: Test corpora
b088 text 9971: PhotoCraft is tested against real files: our own Photoshop-a
b090 heading 10067: The Crafting Apps
b092 text 10121: PhotoCraft is one of the Crafting Apps: free, open-source cr
b093 table 10185: rows 0-7 (0 = header) App What it's for Code Learn more PhotoCraft Image editing: 
b094 text 10568: And ArtCraft itself, our AI image and video studio for artis
b095 text 10608: The Crafting Apps share the same conventions: clean-room and
b099 heading 10755: Come make things with us
b101 text 10796: Our Discord is where artists of every kind hang out: people 
b102 text 10908: discord.gg/artcraft · getartcraft.com · The Crafting Apps · 
b104 heading 10981: License and credits
b106 text 11035: PhotoCraft is dual-licensed under MIT or Apache-2.0, at your
b107 text 11099: Bundled fonts, icons, images and other assets keep their own
b108 text 11163: Every artwork shown is in the public domain (Wikimedia Commo
b109 text 11227: The ArtCraft name, wordmark and logos in docs/brand/ are tra
b110 text 11315: Adobe, Photoshop, Illustrator, Premiere Pro, Lightroom, Acro
b111 text 11403: Made by the ArtCraft team and community.
b113 heading 11486: Star history
b116 media 2001: PhotoCraft editing Hokusai's The Great Wave: a caption card 
b117 media 3257: Monet's Impression, Sunrise with Levels and Vibrance adjustm
b119 media 3995: Vermeer's Girl with a Pearl Earring: an elliptical selection
b121 media 4662: A lotus badge built from shape layers (Lotus, Water, Sun, Ba
b123 media 5447: Free Transform handles around a rotated copy of Ansel Adams'
b125 media 11540: Star History Chart

## Media
m00 block b116 still 2400x1500: PhotoCraft editing Hokusai's The Great Wave: a caption card with a drop shadow, 
m01 block b117 still 2400x1500: Monet's Impression, Sunrise with Levels and Vibrance adjustment layers; the Leve
m02 block b118 still 2400x1500: The Layer Style dialog editing an Outer Glow on the EARTHRISE type layer, with S
m03 block b119 still 2400x1500: Vermeer's Girl with a Pearl Earring: an elliptical selection around the face, an
m04 block b120 still 2400x1500: Bierstadt's Among the Sierra Nevada with the headline SIERRA NEVADA being edited
m05 block b121 still 2400x1500: A lotus badge built from shape layers (Lotus, Water, Sun, Badge and Dotted Ring)
m06 block b122 still 2400x1500: The Twirl filter dialog at a 320 degree angle, previewing live inside an ellipti
m07 block b123 still 2400x1500: Free Transform handles around a rotated copy of Ansel Adams' The Tetons and the 
m08 block b124 still 2400x1500: The Export As dialog in the light theme over Klimt's The Kiss: JPG at quality 90
m09 block b125 still NonexNone: Star History Chart