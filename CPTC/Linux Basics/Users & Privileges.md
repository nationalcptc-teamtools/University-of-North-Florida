use `ls -la` to get permission information on a file/directory and show hidden files starting with `.`
![[Pasted image 20240919234259.png]]
*directory or file? | owner | group | everyone*
`d` - directory
`r` - readable 
`w` - writable 
`x` - executable 

Create a new text file using `echo` and `<`
*echo "hello" > hello.txt* 

`chmod` - change permissions of a file 
`777` - full permissions 
`+x` - give executable permissions

`adduser` - add a new user, give them information 

`/etc/passwd` - displays all users created 
`/etc/shadow` - displays all hashed passwords for users 

`su` - switch user 
- su bob 

`sudo` - can use root commands 
- user must be in sudoers file to use sudo command 
