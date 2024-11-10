#!/bin/bash

# Usage: ./web_enum.sh <target URL>
TARGET=$1

# Directory brute-forcing
echo "[*] Running Gobuster for directory brute-forcing..."
gobuster dir -u $TARGET -w /usr/share/wordlists/dirb/common.txt -o gobuster_$TARGET.txt

echo "[*] Directory brute-forcing complete. Check gobuster_$TARGET.txt for results."
