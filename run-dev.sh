#!/bin/sh
# Dev set: pick the model. Test set stays untouched until the final run.
cd ~/cage
for m in qwen3.5:9b granite4.2:8b qwen3:8b; do
  for f in caveman statim-auto archify openclaw; do
    [ -f "out/cage/$(echo $m | tr ':/' '__')/$f.json" ] && continue
    python3 cage.py ~/motion-studio/films/$f cage --model $m | head -1
  done
done
