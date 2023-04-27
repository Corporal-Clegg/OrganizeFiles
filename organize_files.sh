

#!/bin/bash

# Source directories
downloads=/home/$USER/Downloads

# Folder definitions
pictures=/home/$USER/Pictures/
documents=/home/$USER/Documents/
videos=/home/$USER/Documents/
music=/home/$USER/Documents/

sort_files () {

    # Move files to the designated folders by filetype
    find $downloads -regex '.*\.\(jpe?g\|jpg\|png\|tiff\|gif\)' | xargs -I '{}' mv {} $pictures
    find $downloads -regex '.*\.\(mp4\|mkv\)' | xargs -I '{}' mv {} $videos
    find $downloads -regex '.*\.\(mp3\|flac\)' | xargs -I '{}' mv {} $music
    find $downloads -regex '.*\.\(pdf\|txt\|doc\|docx\|odt\|ppt\|pptx\|xls\|xlsx\)' | xargs -I '{}' mv {} $documents
}

trap "echo Exited; exit;" SIGINT SIGTERM
while [[ 1=1 ]]
do
    watch --chgexit -n 1 "ls --all -l --recursive --full-time $downloads | sha256sum" && sort_files
    sleep 1
done