# Check sudo permissions
sudo -l

# Check if root can be impersonated
sudo su

# List SUID files
find / -perm -4000 -type f 2>/dev/null

# Search for writable files
find / -writable -type f 2>/dev/null

# List all network connections
netstat -tuln

# List running processes
ps aux
