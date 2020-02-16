#!/bin/bash

compton -b &
redshift -P &
mpd
xset -b &
flameshot &
/bin/bash /home/dmr/.config/i3/wp-change.sh &
sleep 3
fcitx &
sleep 1
xmodmap ~/.xmodmap &
