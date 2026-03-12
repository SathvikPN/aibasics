#!/bin/bash

# usage: source setup.sh

alias py="python3"

# activate virtual environment from current directory if not already activated
if [ -d "./venv" ]; then
    # Check if VIRTUAL_ENV points to ./venv
    if [ "$VIRTUAL_ENV" != "$(pwd)/venv" ]; then
        source ./venv/bin/activate
        pip3 install -r requirements.txt > /dev/null 2>&1 || echo "Error installing requirements."
    
    fi
else
    echo "virtual environment ./venv not found. creating one."
    py -m venv venv
    source ./venv/bin/activate
    pip3 install -r requirements.txt
fi

function cs50_getcode() {
    # Check if the CS50 code is provided as an argument
    if [ -z "$1" ]; then
        echo "Example: cs50_getcode https://cs50.harvard.edu/ai/2024/projects/0/degrees/degrees.zip  "
        return 1
    fi

    # Extract the filename from the URL (everything after the last '/')
    local zip_file="${1##*/}"

    # Download the zip file (fail on HTTP errors)
    curl -fsSL -o "$zip_file" "$1" || {
        echo "Download failed (HTTP error or network issue)."
        return 1
    }

    # Verify it’s actually a zip archive
    if ! unzip -t "$zip_file" > /dev/null 2>&1; then
        echo "Downloaded file is not a valid zip archive. Removing $zip_file."
        rm -f "$zip_file"
        return 1
    fi

    # Unzip the file
    unzip -o "$zip_file" &&

    # Delete the original zip file
    echo "Removing $zip_file..." && rm "$zip_file" &&

    # print the folder name that was created without .zip extension
    echo &&
    echo "downloaded: ${zip_file%.zip}/"
    echo
}

# view CS50 AI - https://cs50.harvard.edu/ai/
# toolings: https://cs50.readthedocs.io/render50/
# pip3 install check50 submit50 render50