
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

