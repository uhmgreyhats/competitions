# Really Random
I was given this snippet of code. It generated a weird string. Can you figure out what word was used to generate that string?

## Questions
1. **What word was used to generate the randomized flag? scqdqzl?**

## Steps
1. Look at the code
2. Notice that its taking in the flag variable and looping over it to put a new character in encflag
3. So if we loop over encflag and reverse the the signs, it should be unencrypted

```python
#!/usr/bin/python -u
import random,string

flag = ""
encflag = "scqdqzl"
random.seed("random")
for c in encflag:
    flag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))

print "The flag unencrypted: " + flag
```
