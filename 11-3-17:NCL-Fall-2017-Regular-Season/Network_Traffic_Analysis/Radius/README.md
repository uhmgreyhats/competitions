# RADIUS
We have been using RADIUS to authenticate users on our network. Review a packet capture to see what information an attacker could obtain if they intercept our traffic.

## Questions
1. What is the IP address of the NAS?
2. What is the IP address of the RADIUS server?
3. How many requests were accepted by the RADIUS server?
4. What authentication scheme is being used with RADIUS?
5. How many access requests were made by "hana.harb"?
6. What is the MAC address for the device owned by "sally.berro"?
7. How many different access points had access requests?

## Answers
1. 10.0.252.13
2. 10.0.252.42
3. 84
4. EAP-TLS
5. 22
6. 30:07:4D:53:77:F5
7. 43

## Walkthroughs

We can get the IP address of the NAS by seeing the destination of the Access-Challenge packets.

Since we only have two ips, we know the other one must be the RADIUS server.

To get the amount of requests accepted, I used this tshark command.
`tshark -r Radius.pcap | grep 'Access-Accept' | wc -l`, which lists all the packets and searches for 'Access-Accept' and prints out how many were found.

We can see all the authentication methods for RADIUS [here](https://sites.google.com/site/sireeshajakku/networking/radius/radius-authentication-schemes).
Seeing how alot of the packets have EAP in them, we can guess the method is EAP-TLS.

I got the amount of access requests made by hana.harb with this command.
`tshark -nVr Radius.pcap | grep -C 8 'Access-Request' | grep 'AVP:' | grep "User-Name" | grep "hana.harb" | wc -l`

I got sally.berro's MAC address using this command.
`tshark -nVr Radius.pcap| grep -C 50 'sally.berro' | grep 'Acct-Session-Id'`

I got the amount of different access points in a similar fashion.
`tshark -nVr Radius.pcap| grep -A 21 'Access-Request' | grep 'Called-Station-Id' | sort | uniq -c | wc -l`

Keep in mind, these commands were formulated based on the needs of this challenge, and probably cannot be used for any other one.
