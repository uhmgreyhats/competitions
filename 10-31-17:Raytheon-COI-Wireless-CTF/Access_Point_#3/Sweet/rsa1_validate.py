#!/usr/bin/python

# rsa challenge, straight forward
#
# example name/serial pairs:
#
# knowledge/26582066182495701597915248727138888909
#        is/141271412203160330710342183730048971956
#     power/135066534443646675683259471815808056369
#    Mortal/125332528239055605555179231197739673804
#    Kombat/97493559731364222970517291247384579880

import sys

# globals
d = 65537
n = 152415787532388368909312594615759791673

# args?
if len(sys.argv) != 3:
    print "usage: ", sys.argv[0], " <name> <serial>";
    quit()

# convert name to number eg: "AAAA" -> 0x41414141
m = 0;
for char in sys.argv[1]:
    m = m*256 + ord(char);

if m > n:
    m = m % n;

# convert serial to number eg: "1234" -> 1234
c = int(sys.argv[2], 10);

# process, check
print pow(c, d, n)
print m
if pow(c, d, n) == m:
    print "good"
else:
    print "bad"
