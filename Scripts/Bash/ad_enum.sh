#!/bin/bash

# Usage: ./ad_enum.sh <target IP>
TARGET=$1

# CrackMapExec scan for SMB shares and local admins
echo "[*] Running CrackMapExec on SMB shares and local admins"
crackmapexec smb $TARGET --shares --u <user> -p <password> > cme_smb_enum_$TARGET.txt
crackmapexec smb $TARGET --local-auth --u <user> -p <password> > cme_local_enum_$TARGET.txt

# LDAP search for user and group info (using anonymous bind)
echo "[*] Running LDAP enumeration..."
ldapsearch -x -H ldap://$TARGET -b "dc=example,dc=com" "(objectclass=user)" > ldap_users_$TARGET.txt
ldapsearch -x -H ldap://$TARGET -b "dc=example,dc=com" "(objectclass=group)" > ldap_groups_$TARGET.txt

echo "[*] Active Directory enumeration complete. Check output files."
