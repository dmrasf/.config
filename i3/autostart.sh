#!/bin/bash

compton -b &
redshift -P &
/bin/bash /home/dmr/.config/i3/wp-change.sh &
xset -b &
xset r rate 210 30 &
sleep 3
fcitx &
sleep 1
xmodmap ~/.Xmodmap &
flameshot &
~/.config/polybar/launch &
