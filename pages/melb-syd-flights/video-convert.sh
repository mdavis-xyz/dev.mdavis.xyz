#!/bin/bash
for f in ./docs/*.mp4; do
    ffmpeg -i "$f" -c:v libvpx-vp9 -crf 33 -b:v 0 -an "${f%.mp4}.webm"
done
