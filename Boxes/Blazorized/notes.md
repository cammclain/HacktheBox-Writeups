
# Intro / Recon

## System Information

### Network Version:
**System IP**: 10.10.11.22
**System OS**: Windows 
**OS Version**: ?



I cheated a little an read an article that gave hints to solving this box but it was a week ago so all i remember is that this is an active directory environment. I will try and remember to come back and link to that article if I can find it.


Starting off, I am running an nmap scan


## Scanning
---
### Scan 1
*scan output*: `Boxes/Blazorized/scans/1st_scan.txt`
```bash
[ 12:20PM ]  [ user@parrot:~ ]
 $ sudo nmap -sT -sV --version-all -Pn 10.10.11.22 -p- -n --disable-arp -oN /home/user/Documents/HacktheBox-Writeups/Boxes/Blazorized/scans/1st_scan.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-01 12:20 UTC

```





I