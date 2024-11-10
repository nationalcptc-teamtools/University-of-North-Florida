# Web Enumeration

**Gobuster**: 
- Can [brute-force](https://www.fortinet.com/resources/cyberglossary/brute-force-attack) directories and files 
- Uncover any hidden files or directories on the webserver that are not intended for public access
```bash:
gobuster dir -u http://10.10.10.121/ -w /usr/share/seclists/Discovery/Web-Content/common.txt
```
- gobuster: the program we are using
- dir : directory 
- -u : The target URL or Domain
- http://10.10.10.121/ : Target IP
- -w : The attacker needs to provide a [wordlist](https://hackeracademy.org/top-10-wordlists-for-pentesters/), which is a file (often a text document but not limited to it), containing a set of values to test a mechanism. 
- /usr/share/seclists/Discovery/Web-Content/common.txt ; Wordlist 

**Status Codes**:
- 200s : Success
- 300s : Redirected
- 400s : Access Denied 
- 500s : Server Error 

**Target:** http://Apples.com OR http://102.32.34.5

rockyou.txt:
password
1234567



```
gobuster dir -u http://Apples.com -w /home/listofdirectories
```
```shell-session
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

