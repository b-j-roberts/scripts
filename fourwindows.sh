#!/bin/bash
gnome-terminal
sleep .1
id1="$(xdotool getwindowfocus)"
xdotool windowsize $id1 48% 50%
xdotool windowmove $id1 0 0
gnome-terminal
sleep .1
id2="$(xdotool getwindowfocus)"
xdotool windowsize $id2 48% 50%
xdotool windowmove $id2 0% 50%
gnome-terminal
sleep .1
id3="$(xdotool getwindowfocus)"
xdotool windowsize $id3 50% 50%
xdotool windowmove $id3 50% 50%
gnome-terminal
sleep .1
id4="$(xdotool getwindowfocus)"
xdotool windowsize $id4 50% 50%
xdotool windowmove $id4 50% 0%
