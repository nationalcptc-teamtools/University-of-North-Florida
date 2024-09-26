`ifconfig` - displays all interface types, and the Ip addresses associated with them
![[Pasted image 20240919234728.png]]
- Ip address 
- MAC address 
- interface name

`iwconfig` - shows wireless devices 
`ping` - try to talk to a specific address
`arp -a` - shows Ip address it talks to, and the MAC address it's associated with
`netstat -ano` - shows active connections running on current machine 
`route` - prints your routing table, showing you where your traffic exits

## Update 
`ip` - new command that can do multiple commands on its own 
- `ip a` = `ifconfig`
- `ip n` = `arp -a`
- `ip r` = `route`