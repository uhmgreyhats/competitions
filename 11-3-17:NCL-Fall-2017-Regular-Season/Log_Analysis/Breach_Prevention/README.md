# Breach Prevention
Analyze a log file from breach prevention software running on one of our servers.

## Questions
1. How many total attacks were blocked by the breach prevention software?
2. What IP address attempted the most attacks?
3. How many remote file inclusion attacks were prevented?
4. How many different types of attacks are listed in this log?
5. What software was used by 172.16.4.27 against this server?
6. How many different IP addresses attempted an attack on this server?
7. What URL was blocked the most often by the direct file inclusion defense?

## Answers
1. 340
2. 172.16.4.27
3. 12
4. 3
5. OpenVAS
6. 5
7. https://www.dc4-web-portal.cityinthe.cloud/uploadify/uploadify.php?folder=/

## Walkthroughs

I attached a script for questions 1, 2, 3, 4, 6, and 7.

It's pretty self explanatory, just looping through the lines of the file looking for certain things/keeping track of how often they appeared.

Question 5 is solved by looking at the User-Agent of each attack, and researching OpenVAS.
