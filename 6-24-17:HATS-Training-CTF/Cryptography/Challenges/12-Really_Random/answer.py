#!/usr/bin/python -u
import random,string

flag = ""
encflag = "scqdqzl"
random.seed("random")
for c in encflag:
    flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))

print "The flag unencrypted: " + flag
