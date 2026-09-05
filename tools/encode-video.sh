#!/usr/bin/env bash
# Encode an iPhone clip into a web-friendly MP4 + poster for the site.
#
#   tools/encode-video.sh ~/Desktop/IMG_1234.MOV studio
#
# Produces images/video/studio.mp4 and images/video/studio.jpg.
# H.264 + AAC in MP4 with faststart plays everywhere, iPhone Safari included.
# HEVC (what Cinematic mode records) does NOT play in Chrome or Firefox, which
# is why we re-encode rather than committing the original.
set -euo pipefail

SRC="${1:?usage: encode-video.sh <input.mov> <output-name>}"
NAME="${2:?usage: encode-video.sh <input.mov> <output-name>}"
OUT="$(dirname "$0")/../images/video"
mkdir -p "$OUT"

# -vf scale: cap the long edge at 1280px. Plenty for a web page, and it is what
# takes a 200 MB iPhone clip down to something a git repo should hold.
# -crf 26 is the quality knob: lower = better and bigger, 23-28 is the useful range.
ffmpeg -y -i "$SRC" \
  -vf "scale='if(gt(iw,ih),min(1280,iw),-2)':'if(gt(iw,ih),-2,min(1280,ih))',format=yuv420p" \
  -c:v libx264 -profile:v high -level 4.0 -preset slow -crf 26 \
  -c:a aac -b:a 128k -ac 2 \
  -movflags +faststart \
  "$OUT/$NAME.mp4"

# Poster frame at 1 second in, so the <video> shows something before it loads.
ffmpeg -y -ss 1 -i "$OUT/$NAME.mp4" -frames:v 1 -q:v 3 "$OUT/$NAME.jpg"

echo
echo "Wrote:"
ls -lh "$OUT/$NAME.mp4" "$OUT/$NAME.jpg"
echo
echo "Now set  VIDEO = \"$NAME\"  in tools/build_site.py, and note the real"
echo "width/height in VIDEO_W / VIDEO_H (ffprobe prints them):"
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$OUT/$NAME.mp4"
