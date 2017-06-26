# SNORT this
Bobby is always visiting an unacceptable website via http. We need to to create a snort rule that throws an alert when his source IP 172.16.31.10 connects to 128.171.224.109. Remember to specify protocol, port, our custom message and an SID. msg:"Bobby's at it again"; sid:2000001; Clue 1:Connection to a webserver uses TCP or UDP? Clue 2:Who's the server and who's the client? Is the server listening on port 80 or is the client listening on port 80? Clue 3:alert XXX XXX.XX.XX.XX aXy -> XXX.XXX.XXX.XXX 80 (msg:"Bobby's at it again"; sid:2000001;)

## Questions
1. **What is the snort rule needed to complete this request?**
2. **Who is the Network Owner of that IP address (128.171.224.109)**
3. **What is the hostname of the machine?**

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
