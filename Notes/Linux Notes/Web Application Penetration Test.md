Reference: https://www.youtube.com/watch?v=odC720S63Fw

### Pen Test Steps

You are a person, or group who plan on doing a penetration test for a company. They may give you some possible targets:
- Eample.com
- ip address
- domain name

**Step 1: Recon/Enumeration**
Can use a tool like nmap to see what types of services are running on the target machine
- http
- database
- admin portal 

**Step 2: Weaponize**
Once you have found possible targets on the system, you want to find unpatched systems, and see if there are possible vulnerabilities you can use.
- Sometimes directly available as exploits 
- Can craft your own payloads (Don't be a script kitty)

**Step 3: Command and control**
You load the exploits you found into your target server, and get full control of their systems. 

You only need **ONE** entry point to get full control of a machine


### Example Scenario

Step 0: Choose the machine you're choosing to attack with 
*Example*:
**Attack Machine**: Kali
(The machine you use does not matter, you can install most things on any machine)

Step 1: Find out all the devices in a network or specific IP Address
*Example*: Any of those free wifis at cafes and malls.
- You want to uncover all the devices in the network and target the ones you are interested in
```
sudo netdiscover
```
- **sudo** applies elevated privileges
- **netdiscover** is a active/passive APT reconnaissance tool, used to gain information about wireless networks without DHCP servers in wardriving scenarios.
![[Pasted image 20240925164143.png]]
*As shown above, it is showing all devices connected to the network 192.168.0.1, that is the router*

**Find a target**
As show above, there are multiple devices we can target, the one we are interested in is **192.168.0.100**

**Check for any open ports**
Now that we have a target, we will be using **nmap** to check if they have any ports open, giving us information on what services they are running 
```
sudo nmap -sV 192.168.0.100
```
- **sudo** applies elevated privileges
- **nmap** is a network exploration tool that allows you find what services a network is running
	- **sV** argument looks specifically at what service/version the network is running
	- Due to the amount of ports nmap scans, it may take a couple minutes to finish 
![[Pasted image 20240925165310.png]]
*As you can see above, it provides a variety of information on a network:*
- Port: 22,23,25, etc...
- State: Open/Closed/Unknown
- Service: ssh, telnet, smtp, etc...
- Version: OpenSSH 5.3, Linux telnetd, MySQL 5.1.73, etc... 

You can use this new information to find possible vulnerabilities. Keep track on the versions of the services, and do some research on if any of them have known issues. If they are using an older version, there could be an exploit you can quickly upload


**Going on the web page on your browser**
*Now that we have gotten some information on the network, we see they are hosting a web sever at port 80, an Apache web server. Lets try to go on that IP from our browser and see what we find*

**Website Crawling**
Websites are known for having a variety of web pages, but sometimes we want to find the pages that cold be possibly storing sensitive information. We can possibly find some hidden pages by doing something called **crawling**.
**Crawling** is the act of searching across a website using a program to find directions the server owners did not want you to find. To do this, we will be using a command called `nikto`, which allows us to do exactly what we explained.
```
sudo nikto -h 192.168.0.100
```
- **sudo** applies elevated privileges
- **nikto** is a program that scans a web server for known vulnerabilities. These include server/software misconfigs, default files and programs, insecure files and programs, outdates servers and programs, and more.
	- **h** argument give some more information
![[Pasted image 20240925170924.png]]
*As seen below, the command looks for possible directories, vulnerabilities, and more

You can use the information above to look into the possible directories, or look into ways of exploiting old versions.
*Example*:
The **nikto** above showed 2 valuable directories, `/phpldapadmin` and `/phpmyadmin`. While you don't have any login information, the fact that you found the admin page is bad for the company, as now you can try injections or other vulnerabilities. 

**Finding Vulnerabilities**
If you look at the `nmap` command from earlier, and from `nikto`, there is a service called `Miniserve 0.01(Webmin)` at port 1000. The version 0.01 is quite early, and these services need some kind of tool to administer the server. So we can take this opportunity to check if there are already exploits online that we can use. We will be trying this by using the `searchsploit` command.
```
sudo searchsploit webmin
```
- **sudo** applies elevated privileges
- 