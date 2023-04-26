#!/bin/bash

## PATH definitions
# Source directories
downloads=/home/$USER/Downloads

# Targeted destinations
wallpapers_dynamic=/home/$USER/Pictures/Wallpapers/Dynamic/

# Misc folders for manual sorting
pictures_misc=/home/$USER/Pictures/
documents_misc=/home/$USER/Documents/
videos_misc=/home/$USER/Videos/
music_misc=/home/$USER/Music/

sort_files () {
    # Sort into targeted directories
    find $downloads -regex '.*\.avif$' | xargs -I '{}' mv {} $wallpapers_dynamic

    # Move non-targeted files to the parent folders
    find $downloads -regex '.*\.\(jpe?g\|jpg\)' | xargs -I '{}' mv {} $pictures_misc
    find $downloads -regex '.*\.\(mp4\|mkv\)' | xargs -I '{}' mv {} $videos_misc
    find $downloads -regex '.*\.\(mp3\|flac\)' | xargs -I '{}' mv {} $music_misc
}

trap "echo Exited; exit;" SIGINT SIGTERM
while [[ 1=1 ]]
do
    watch --chgexit -n 1 "ls --all -l --recursive --full-time $downloads | sha256sum" && sort_files
    sleep 1
done
