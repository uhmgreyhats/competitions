# DNS
We think that a hacker was able to modify some of our DNS records. Analyze a packet capture that we have created from running DNS queries.

## Questions
1. What was the IP address of the DNS resolver used in this packet capture?
2. What organization operates the DNS resolver used in this capture?
3. What is the IPv4 address responsible for www.cityinthe.cloud?
4. What is the IPv6 address responsible for www.cityinthe.cloud?
5. Who is the mail provider for cityinthe.cloud?
6. What is the handle of the hacker that tampered with the DNS records?
7. What IP address was queried for reverse lookup?
8. What organization operates the IP adddress that was queried for reverse lookup?
9. Which FQDN is responsible for the majority of TCP SIP traffic to cityinthe.cloud?
10. Which FQDN is the backup for TCP SIP traffic if all other servers are not available for cityinthe.cloud?

## Answers
1. 209.244.0.3
2. level3
3. 232.135.80.85
4. c2d1:e1b:5bdd:3fbd:addd:3793:6078:ad97
5. google
6. zer0dark0
7. 108.174.10.10
8. linkedin
9. sip2.cityinthe.cloud
10. sip3.cityinthe.cloud
