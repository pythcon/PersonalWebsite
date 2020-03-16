#!/bin/bash

#Do not run script if characters less than 10 (if uptime is less than 10 minutes)
uptime=`uptime -p | cut -d " " -f2-`
if [ "${#uptime}" -lt 10 ]
then
    echo "Uptime has not reached 10 minutes!"
    exit 1
fi

if ps ax | grep $0 | grep -v $$ | grep "tvStart.sh" | grep -v grep
then
    echo "tvStart.sh running...exiting"
else
    if ps ax | grep $0 | grep -v $$ | grep "tvContinue.sh" | grep -v grep
    then
        echo "tvContinue.sh running...exiting"
    else
        if ps ax | grep $0 | grep -v $$ | grep "vlc" | grep -v grep
        then
            echo "VLC running...exiting"
        else
            mv -f /mnt/plexNAS/Files/tv/showList1.txt /mnt/plexNAS/Files/tv/showList.txt
            mv -f /mnt/plexNAS/Files/tv/playlist1.m3u /mnt/plexNAS/Files/tv/playlist.m3u
            mv -f /mnt/plexNAS/Files/tv/xmltv1.xml /mnt/plexNAS/Files/tv/xmltv.xml

            sleep 3

            echo "VLC stopped...starting it"
            /usr/bin/cvlc /mnt/plexNAS/Files/tv/playlist.m3u --sout '#transcode{vcodec=h264, acodec=mp3, vb=800, ab=128} :standard{access=http, mux=ts, dst=192.168.1.43:1234}' --no-sout-all --sout-mux-caching=10000 &

            sleep 5

            echo -ne '\n'
    
            #Generate a new playlist
            python3 /mnt/plexNAS/Files/tv/generatePlaylist.py yes

            sleep 2

            echo -ne '\n'
        fi
    fi
fi
