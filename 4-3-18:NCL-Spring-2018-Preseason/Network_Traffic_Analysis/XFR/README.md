# XFR
Use the provided packet capture to answer some questions about a DNS zone transfer.

## Questions
1. How many unique zone transfers were requested?	
2. What domain successfully completed a zone transfer?	
3. How many resource records were returned from the successful zone transfer?	
4. What IP address would the browser use to access the domain that completed the zone transfer?	
5. What email service does the successfully zone-transferred domain use?
6. What is the DNSSEC key tag used to verify the records in the zone-transferred domain?	
7. What was the TTL of the Reddit A records in the capture?	

## Answers
1. 4
2. zonetransfer.me
3. 153
4. 217.147.177.157
5. aspmx.l.google.com
6. 44244
7. 5
