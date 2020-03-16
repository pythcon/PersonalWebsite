#!/bin/bash
echo "Generating playlist for Channel"

python3 /path/to/tv/generatePlaylist.py no

sleep 5

/usr/bin/cvlc /path/to/tv/playlist.m3u --sout '#transcode{vcodec=h264, acodec=mp3, vb=800, ab=128} :standard{access=http, mux=ts, dst=<ip:port>}' --no-sout-all --sout-mux-caching=10000 &

sleep 5

echo -ne '\n'

sleep 5

python3 /path/to/tv/generatePlaylist.py yes
