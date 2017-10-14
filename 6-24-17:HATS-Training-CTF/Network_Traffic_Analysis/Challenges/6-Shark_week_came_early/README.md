# Shark week came early
There has been a network breach and we need our best analyst on the job. Answer these questions and I will give you a huge tip: Download wireshark.

## Questions
1. **What IP address (IPv4) is the malicious actor?**
2. **What IP address (IPv4) is the victim?**
3. At what time of day was the initial contact (XX:XX:XX)?
4. **What protocol was used at initial contact?**
5. **What NMAP switch was used to conduct the port scan (Example:”-xX”)?**
6. **What website did the malicious actor go to (www.SOMETHING.com)?**
7. **What is the Servers IP address?**
8. **What was the username the malicious actor used to log into the server?**
9. **What protocol was used for a file transfer?**
10. **What was the file name transferred?**
11. Recover the file and read the contents of the file... What does the secret message say?

## Steps

### Question 1
1. Look up what a snort rule is
2. Find a [generator](http://snorpy.com/)
3. Plug in the information given and get the resulting snort rule

### Question 2
1. Go to 128.171.224.109
2. See thats its UH website
3. `whois 128.171.224.109`
4. See OrgName:

### Question 3
1. Go to 128.171.224.109
2. See thats its UH website
3. `dig -x 128.171.224.109`
4. See `www00.honolulu.hawaii.edu`
