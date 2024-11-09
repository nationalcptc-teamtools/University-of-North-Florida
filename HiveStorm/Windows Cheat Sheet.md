---

### **Windows Server 2022 Security Cheat Sheet**

---
### **Windows Server 2022 Security Cheat Sheet (with CTF and Issue-Specific Methods)**

---

### **1. Active Directory (AD) Security**
- **Remove Unauthorized Users**:  
  AD Users and Computers → Locate user → Right-click → "Delete".
- **Create a New User**:  
  AD Users and Computers → Right-click Users → New → User → Fill out details.
- **Give a User Administrator Privileges**:  
  AD Users and Computers → Locate user → Right-click → Add to group → Select "Administrators".
- **Give a User Domain Admin Privileges**:  
  AD Users and Computers → Locate user → Right-click → Add to group → Select "Domain Admins".
- **Find a User with an Insecure Password**:  
  Check via PowerShell:
  ```powershell
  net user <username>
  ```
  If insecure, force a reset:
  ```powershell
  Set-ADAccountPassword -Identity <username>
  ```
  Apply a stronger password policy via Group Policy.
- **Set Secure Minimum Password Age**:  
  Group Policy Management → Computer Configuration → Security Settings → Account Policies → Password Policy → Minimum Password Age.
- **Set Secure Lockout Threshold**:  
  Group Policy Management → Computer Configuration → Security Settings → Account Policies → Account Lockout Policy → Set the lockout threshold.

#### **CTF Forensic Task**:
- **Find Alias that Points to a DNS Entry**:  
  Run:
  ```bash
  nslookup
  ```
  Enter the alias name, and it will resolve to the DNS entry.

---

### **2. DNS and Firewall Security**
- **DNS Service Management**:  
  Run:
  ```bash
  dnsmgmt.msc
  ```
  Ensure DNS is running and properly configured.
  
- **Enable Firewall Protection**:  
  Run:
  ```bash
  wf.msc
  ```
  Ensure the appropriate firewall rules are enabled, especially for RDP and DNS.

- **Find Unauthorized DNS Aliases**:  
  Using DNS Manager (`dnsmgmt.msc`), review DNS entries and aliases (CNAME records).

#### **Run Dialogs**:
- **AD Users and Computers**: `dsa.msc`
- **DNS Manager**: `dnsmgmt.msc`
- **Firewall**: `wf.msc`
- **Group Policy Management**: `gpmc.msc`
- **Event Viewer**: `eventvwr.msc`
- **IIS Manager**: `inetmgr`

---

### **3. RDP (Remote Desktop Protocol) Security**
- **Enable RDP Network Level Authentication**:  
  System Properties → Remote tab → Check "Allow connections only from computers using NLA".
  
- **Disable Unnecessary Services**:  
  Task Manager → Services tab → Identify and stop unnecessary services. Services to disable include **Telnet**, **Remote Registry**, and others not required by the environment.

---

### **4. General Windows Server Security**
- **Check for Pending Updates**:  
  Settings → Update & Security → Check for updates.
- **Install Updates**:  
  Same as above.
- **Enable Auto Updates**:  
  Group Policy Management → Windows Update settings → Configure automatic updates.
- **Stop FTP and Disable It**:  
  IIS Manager → Sites → Select FTP site → Stop → Right-click → Manage FTP Site → "Stop FTP".
  
- **Disable File Sharing for C Drive**:  
  File Explorer → Right-click C: drive → Properties → Sharing tab → Disable sharing.

- **Find and Remove Plain Text Password Files**:  
  Use PowerShell to search for files with potential sensitive data:
  ```powershell
  Get-ChildItem -Path C:\ -Recurse -Include *.txt,*.log | Select-String -Pattern "password"
  ```

- **Remove Unauthorized Software (CCleaner, Netcat, etc.)**:
  - **Remove CCleaner**:
    Control Panel → Programs → Uninstall CCleaner.
  - **Remove Netcat Backdoor**:
    Task Manager → Details → Find suspicious processes (e.g., **nc.exe** or **netcat**). Right-click → Open File Location → Delete executable after killing the process.

- **Chrome Security**:
  - **Update Google Chrome**:  
    Chrome → Settings → About → Update.
  - **Block Intrusive Ads in Chrome**:  
    Chrome → Settings → Privacy and Security → Site Settings → Ads → Block.

#### **Run Dialogs**:
- **Task Manager**: `taskmgr`
- **IIS Manager**: `inetmgr`

---

### **5. CTF Forensic and Issue-Specific Tasks**
#### **Handling Processes & Backdoors**:
- **Finding and Removing Backdoors (GooseDesktop.exe example)**:
  1. **Find the Process**:  
     Task Manager → Details → Locate **GooseDesktop.exe**.
  2. **Open File Location**:  
     Right-click → Open File Location.
  3. **Kill Process**:  
     Right-click the process → End task.
  4. **Delete the Executable**:  
     In File Explorer, right-click the file → Delete.

---

### **6. Issues to Avoid (Penalties)**
- **Account Lockout Policy Less Than 5**:  
  Group Policy Management → Security Settings → Account Lockout Policy → Ensure it is set to 5 or more.
- **Remote Desktop Disabled**:  
  Ensure RDP is enabled if required, especially for management.
- **DNS Service Stopped/Disabled**:  
  Make sure DNS is running if it is critical for the machine (use `dnsmgmt.msc` to verify).
- **SMB Client Disabled**:  
  Do not disable SMB if required for file sharing services.
- **File Sharing Disabled for SYSVOL or NETLOGON**:  
  Keep file sharing enabled for SYSVOL/NETLOGON directories.
- **Google Chrome Not Installed at the Default Location**:  
  Ensure Chrome is installed at the default location (`C:\Program Files\Google\Chrome`).

---