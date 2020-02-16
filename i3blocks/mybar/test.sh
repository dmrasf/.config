#!/bin/bash

FG_COLOR=${FG_COLOR:-#bbbbbb}
BG_COLOR=${BG_COLOR:-#111111}
HLFG_COLOR=${HLFG_COLOR:-#111111}
HLBG_COLOR=${HLBG_COLOR:-#bbbbbb}
BORDER_COLOR=${BORDER_COLOR:-#222222}

# Options not related to colors
ROFI_TEXT=${ROFI_TEXT:-Menu:}
ROFI_OPTIONS=(${ROFI_OPTIONS:--width 11 -location 3 -hide-scrollbar -bw 2})

# Zenity options
ZENITY_TITLE=${ZENITY_TITLE:-Menu}
ZENITY_TEXT=${ZENITY_TEXT:-Action:}
ZENITY_OPTIONS=${ZENITY_OPTIONS:---column= --hide-header}

# Whether to ask for user's confirmation
enable_confirmation=${ENABLE_CONFIRMATIONS:-false}

# Preferred launcher if both are available
preferred_launcher=${LAUNCHER:-rofi}

usage="$(basename "$0") [-h] [-c] [-p name] -- display a menu for shutdown, reboot, lock etc.

where:
    -h  show this help text
    -c  ask for user confirmation
    -p  preferred launcher (rofi or zenity)

This script depends on:
  - systemd,
  - i3,
  - rofi or zenity."

launcher_list=(rofi zenity)

function check_launcher() {
  if [[ ! "${launcher_list[@]}" =~ (^|[[:space:]])"$1"($|[[:space:]]) ]]; then
    echo "Supported launchers: ${launcher_list[*]}"
    exit 1
  else
    # Get array with unique elements and preferred launcher first
    # Note: uniq expects a sorted list, so we cannot use it
    i=1
    launcher_list=($(for l in "$1" "${launcher_list[@]}"; do printf "%i %s\n" "$i" "$l"; let i+=1; done \
      | sort -uk2 | sort -nk1 | cut -d' ' -f2- | tr '\n' ' '))
  fi
}
















