# arecord -D plughw:2,0 -f cd --buffer-size=2048 --period-size=32 \
# | sox -t raw -r 44100 -e signed -b 16 -c 2 - -t raw - pitch 500 overdrive 10 tremolo 40 60 flanger \
# | aplay -D plughw:1,0 -f cd --buffer-size=2048 --period-size=32

arecord -D plughw:2,0 -f cd | aplay -D hw:Loopback,0,0 &

arecord -D hw:Loopback,1,0 -f cd --buffer-size=2048 --period-size=32 \
| sox -t raw -r 44100 -e signed -b 16 -c 2 - -t raw - pitch 500 overdrive 10 tremolo 40 60 flanger \
| aplay -D plughw:1,0 -f cd --buffer-size=2048 --period-size=32
