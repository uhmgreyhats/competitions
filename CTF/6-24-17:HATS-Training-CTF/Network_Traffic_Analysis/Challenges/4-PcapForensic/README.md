# PcapForensic
Find the hidden message.

## Questions
1. **What is the md5 sum of the picture captured in the pcap?**
2. **What is NOT a well known TCP flag that was captured in this pcap file (Answer should be exactly as how the flag displays in the pcap)?**
3. What is the hidden flag?

## Steps

### Question 1
1. Open the pcap in Wireshark
2. File > Export Objects > HTTP
3. Get the Image
4. md5sum `{imagefile}`

### Question 2
1. Open the pcap in Wireshark
2. Look at a packet
3. See Urgent pointer: 0
4. Try Urgent pointer
5. Doesn't work
6. Try URG (the abbreviation)
