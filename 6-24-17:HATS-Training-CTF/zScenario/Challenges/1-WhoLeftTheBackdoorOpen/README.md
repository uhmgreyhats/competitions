# WhoLeftTheBackdoorOpen
A previous "Grey HAT" penetration tester has installed a not so persistent backdoor to the target machine. It's a good thing we were able to get a memory dump of the malicious file, but we were unable to pull back the file due to my mom saying that I have to get off the computer. I stashed the file in the HATS home directory. You'll need to find a way to pull the file back in order to answer some questions... BUT!!!! before you even pull that file back, I need you to get me some basic information about the box... then do the analytical work on the memdump. I only remember the creds and an IP address. HATS // P@ssw0rd #10.1.1.151 GOOD LAQQQ

## Questions
1. **What port number is the SSH service running on?**
2. **What port does SSH normally run on?**
3. **What is the Distributor ID of the Operating System?**
4. **What is the operating system's code name**
5. **Search for a .hats file. What is the full file name including the extention?**
6. **Look at the contents of the .hats file what is the secret code?**
7. **What is the full name of the hidden directory?**
8. **What is the name of the backdoor process?**
9. **What is the MD5 Hash of the malicious file?**
10. What port does the backdoor listen on?
11. **Who is the owner of the malicious file?**
12. **What type of shell does the malicous program execute?**
13. What is the service that is allowing the malware to persist on boot?
14. **What is the md5sum of the memdump file? **
15. Within the memdump, what was the date that the VM was built? Format to enter is MMDDYYYY

## Steps

### Question 1
1. nmap port scan the box
2. find the port to ssh in

### Question 2
1. 22

### Question 3
1. [Link](https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command)

### Question 4
1. [Link](https://unix.stackexchange.com/questions/88644/how-to-check-os-and-version-using-a-linux-command)

### Question 5
1. Find all user groups
2. See "crook"
3. Go to crook's home directory
4. Find the .hats file

### Question 6
1. `cat crumbz.hats`

### Question 7
1. `ls -lah`
2. See .hidden

### Question 8
1. cd .hidden
2. ls
3. See 'xenial'

### Question 9
1. md5sum xenial

### Question 11
1. ls -lah
2. crook

### Question 12
1. file xenial
2. bash script

### Question 14
1. md5sum memdump
