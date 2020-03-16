#!/bin/bash
echo "Generating playlist for Todderang"

python3 /mnt/plexNAS/Files/tv/generatePlaylist.py no

sleep 5

/usr/bin/cvlc /mnt/plexNAS/Files/tv/playlist.m3u --sout '#transcode{vcodec=h264, acodec=mp3, vb=800, ab=128} :standard{access=http, mux=ts, dst=192.168.1.43:1234}' --no-sout-all --sout-mux-caching=10000 &

sleep 5

echo -ne '\n'

sleep 5

python3 /mnt/plexNAS/Files/tv/generatePlaylist.py yes
