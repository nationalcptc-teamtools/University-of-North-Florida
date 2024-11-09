#!/bin/bash

# Usage: ./crack_hash.sh <hash_file> <wordlist>
HASH_FILE=$1
WORDLIST=$2

# Check if hash file and wordlist are provided
if [ -z "$HASH_FILE" ] || [ -z "$WORDLIST" ]; then
    echo "Usage: $0 <hash_file> <wordlist>"
    exit 1
fi

# Run Hashcat
echo "[*] Running Hashcat for dictionary attack..."
hashcat -m 0 -a 0 $HASH_FILE $WORDLIST -o cracked_passwords.txt --quiet

echo "[*] Password cracking complete. Check cracked_passwords.txt for results."
