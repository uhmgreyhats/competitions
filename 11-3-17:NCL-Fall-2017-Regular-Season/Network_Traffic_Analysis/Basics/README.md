# Basics
Some of our new recruits are starting to learn about analyzing packet captures. Help generate an answer key for them to use as they practice their skills.

## Questions
1. What is the IP address of the device that is pinging other devices?
2. According to the ping traffic, what is the IP address of the host that is not up?
3. What is the IP address of the device at 00:50:56:F9:77:70 given by ARP
4. What is the first website that 10.0.0.132 visited?
5. How many bytes large is the only .ico file downloaded via HTTP?
6. What is the IP address of the FTP server the user at 10.0.0.132 connects to?
7. What was the password used to log in to the FTP server?
8. How many folders are directly (not including child folders) in the /ubuntu folder on the FTP server?

## Answers
1. 10.0.0.132
2. 209.85.225.104
3. 10.0.0.2
4. www.offensive-security.com
5. 318
6. 91.189.88.40
7. mozilla@example.com
8. 4

## Walkthroughs

We can guess that the IP `10.0.0.132` is pinging other devices due to the sheer amount of times this IP appears in the source column.

We can get this ip `209.85.225.104` by viewing the ICMP protocol traffic and seeing that this host does not respond to the probes.

Using `ip.src == 10.0.0.132 && http.request` as the filter and viewing the first packet, we can see that this ip sent a get request to `www.offensive-security.com`.

We can view the amount of bytes of the .ico file by using `File --> Export Objects --> HTTP`.

We can find the FTP server `91.189.88.40` by using the filter `ip.src == 10.0.0.132`, and searching for FTP data.

Right click a FTP packet, Follow --> TCP stream and view the password.

We can view the response of the `LIST` command in `tcp.stream eq 30`.
Just follow the FTP TCP stream, and increment the frame until you find the response packet.
