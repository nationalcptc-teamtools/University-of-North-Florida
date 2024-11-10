#!/bin/bash

# Continue with the full setup if no specific repositories were specified
# Ask user if they want to install SecLists
read -p "Do you want to install SecLists? (y/n): " response1
sudo apt update
# Install required packages, gobuster, rlwrap, and remmina (RDP but kinda better than freexrdp)
sudo apt install -y ldap-utils gobuster remmina rlwrap metasploit-framework wordlists nmap hydra wireshark john hashcat burpsuite netexec

# install bopscrk (wordlist generator)
pip install bopscrk

# unzip rockyou.txt
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Clone all GitHub repositories if no -r option was used
mkdir -p ~/tools
cd ~/tools
pip install bloodhound

# Create linux-binary directory and download files
mkdir linux-binary
cd linux-binary
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_linux_386.gz
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_linux_amd64.gz
gunzip *.gz
mv chisel_1.9.1_linux_386 chisel32
mv chisel_1.9.1_linux_amd64 chisel64
git clone https://github.com/rebootuser/LinEnum.git
wget https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
cd ..

# Create windows-binary directory and download files
mkdir windows-binary
cd windows-binary
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_windows_386.gz
wget https://github.com/jpillora/chisel/releases/download/v1.9.1/chisel_1.9.1_windows_amd64.gz
gunzip *.gz
mv chisel_1.9.1_windows_386 chisel32
mv chisel_1.9.1_windows_amd64 chisel64
wget https://github.com/peass-ng/PEASS-ng/releases/download/20240519-fab0d0d5/winPEASx64.exe
git clone https://github.com/int0x33/nc.exe.git
git clone https://github.com/ParrotSec/mimikatz.git
wget https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/raw/master/Rubeus.exe
wget https://github.com/r3motecontrol/Ghostpack-CompiledBinaries/raw/master/Certify.exe
wget https://github.com/BloodHoundAD/BloodHound/raw/master/Collectors/SharpHound.exe
git clone https://github.com/Kevin-Robertson/Powermad.git
wget https://github.com/PowerShellMafia/PowerSploit/raw/master/Recon/PowerView.ps1
cd ..

# create webapp directory which stores all webapp related tools
mkdir webapp
cd webapp
git clone https://github.com/BlackArch/webshells.git
git clone https://github.com/ambionics/phpggc.git
# Install google chrome to be able to use chrome debugger. (rare to use but still cool to have)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
cd ..

# Install bloodhound and neo4j
sudo apt install -y bloodhound neo4j

# installs seclists if user wants
if [[ "$response1" = "y" || "$response1" = "Y" ]]; then
    wget https://github.com/danielmiessler/SecLists/archive/refs/heads/master.zip
    unzip master.zip
    mv SecLists-master SecLists
else
    echo "No action taken for SecLists."
fi

# Recursively change permissions to be correct
sudo chown -R $username:$username ~/tools

echo ""
echo ""
echo '============== Good luck and happy hacking! =============='
