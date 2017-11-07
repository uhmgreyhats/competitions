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

## Walkthroughs

We can view the IP address of the DNS resolver by seeing which IP is responding to the queries.

We can find out which organization operates this DNS through a simple dig query `dig -x 209.244.0.3`.

We can view the IPv4 address in packet number 2, DNS --> Answers --> www.cityinthe.cloud

We can view the IPv6 address in packet number 4, DNS --> Answers --> www.cityinthe.cloud

We can view the mail provider in packet number 12, DNS --> Answers --> cityinthe.cloud and seeing answers of type MX (Mail eXchange).

We can view the hacker's handle in packet number 16, DNS --> Answers --> tagged.cityinthe.cloud --> TXT `zer0dark0 was here`.

We can view the ip address responsible for DNS reverse lookup and organization responsible for handling it in packet number 22. DNS --> Answers --> 10.10.174.108.in-addr.arpa --> Domain Name.
Reverse the IP to be in the correct format.

We can FQDNs responsible for handling TCP SIP traffic in packet number 20. DNS --> Answers --> _sip._tcp.cityinthe.cloud --> Target, and comparing their prorities/weights.
