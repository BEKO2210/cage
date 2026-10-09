#!/bin/sh
# run.sh <tag> <film>... : cage + free with qwen3.5:9b, then the three judges. Existing outputs are kept.
cd ~/cage
M=qwen3.5:9b; D=qwen3.5_9b; TAG=$1; shift; CAGE=${CAGE:-cage2}
for f in "$@"; do
  for arm in $CAGE free; do
    [ -f out/$arm/$D/$f.json ] || python3 cage.py ~/motion-studio/films/$f $arm --model $M | head -1
  done
done
python3 -u judge.py $TAG "$@" --arms out/gold/gold out/free/$D out/$CAGE/$D
