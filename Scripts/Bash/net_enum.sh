#!/bin/bash

# Usage: ./enum.sh <target IP>
TARGET=$1

# Check if target IP is provided
if [ -z "$TARGET" ]; then
    echo "Usage: $0 <target IP>"
    exit 1
fi

# Run Nmap quick scan
echo "[*] Running Nmap scan..."
nmap -sC -sV -oN nmap_$TARGET.txt $TARGET

# Perform SMB enumeration if port 445 is open
if grep -q "445/tcp open" nmap_$TARGET.txt; then
    echo "[*] SMB Enumeration on $TARGET"
    smbclient -L \\$TARGET -N > smb_enum_$TARGET.txt
fi

# FTP anonymous login check
if grep -q "21/tcp open" nmap_$TARGET.txt; then
    echo "[*] Checking for anonymous FTP login..."
    ftp -nv $TARGET <<END_SCRIPT
quote USER anonymous
quote PASS ftp@domain.com
ls
quit
END_SCRIPT
fi

echo "[*] Enumeration Complete. Check output files."
