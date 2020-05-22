#!/bin/bash

cat ~/.config/i3/emoji | dmenu -l 10 -fn Monospace-13 | awk '{print $1}' |
    xclip -selection clipboard

emoji=$(xclip -o -selection clipboard)

[ -n "$emoji" ] && dunstify "$emoji : copied to clipboard"

