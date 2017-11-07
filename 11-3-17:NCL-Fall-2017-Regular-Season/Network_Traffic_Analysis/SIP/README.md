# SIP
We have been using SIP and VoIP for telecommunication within the organization. Review a packet capture to see what information an attacker could obtain if they intercept our traffic.

## Questions
1. What is the IP address of the SIP proxy?
2. What is the name of the software running SIP on the SIP proxy?
3. How many total voicemails does 542@10.21.2.75 have?
4. What is the SIP address of the caller in the only call?
5. What is the IP address of the caller in the only call?
6. What is the SIP address of the recipient of the only call?
7. What is the IP address of the recipient of the only call?
8. What is the SIP address of the individual who hangs up the call?
9. What brand of physical phone was the recipient of the call using?
10. How many seconds into the capture is the first word of the call said? (Round down to nearest second)
11. How many different SIP agents registered with the SIP proxy?

## Answers
1. 10.21.128.1
2. Asterisk
3. 14
4. 282@10.21.128.1
5. 10.21.1.109
6. 635@10.21.128.1
7. 10.21.1.132
8. 282@10.21.128.1
9. Apple
10. 27
11. 63

## Walkthroughs
We can get the IP address of the SIP proxy by looking for which IP is getting REGISTER requests.

We can get the sotware running by viewing any response packet.
Session Initiation Protocol --> Message Header --> WWW-Authenticate --> Realm. Or by viewing the User-Agent of some responses.

We can get the amount of voicemails by using the filter `ip.src == 10.21.128.1`, looking for the NOTIFY packet to `542@10.21.2.75`, and viewing the message body. This happens in packet 311. Packet --> Session Initiation Protocol --> Message Body --> Voice-Message.

We can get the SIP address of the caller and recipient of the call by using Wireshark's Telephony section --> VoIP calls.

We can get their IP addresses by searching for packets with those specific SIP addresses, and viewing where the SIP proxy is sending those packets.

We can see who hangs up the call in packet 1351. Session Initiation Protocol --> Message Header and viewing the To and From fields.

We can view the brand of phone by using the filter `ip.src == 10.21.1.132` and viewing the Ethernet II header of the packet, revealing an Apple phone.

We can see how many seconds the first word was said by using Wireshark's Telephony section --> SIP flows, selecting all the packets, and hitting Play Streams. Hitting the play button here reveals the first word was said 27 seconds in.
