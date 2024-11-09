#!/bin/bash

# Usage: ./screenshot.sh <screenshot_directory>
DIR=$1

# Check if directory is provided
if [ -z "$DIR" ]; then
    DIR="screenshots"
fi

mkdir -p $DIR
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FILENAME="$DIR/screenshot_$TIMESTAMP.png"

# Take screenshot
gnome-screenshot -f $FILENAME
echo "[*] Screenshot saved as $FILENAME"
