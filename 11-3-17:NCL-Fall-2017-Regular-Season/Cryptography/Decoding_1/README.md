# Decoding 1
Our officers have obtained password dumps storing hacker passwords. After obtaining a few plaintext passwords, it appears that they are all encoded using different number bases. See if you can decode them.

## Questions
1. 6672616e636f31323132
2. 01101010 01101111 01101011 01100101 01110011 00110001 00110011 00110010 00110101

## Answers
1. franco1212
2. jokes1325

## Walkthroughs

### Question 1
Realize from the decription that we need to convert this to a certain type of base encoding.

Look up a base alphabet and use it to find out which base this is

Base | Alphabet
------------- | -------------
2 | `01`
8 | `01234567`
11 | `0123456789a`
16 | `0123456789abcdef`
32 | `0123456789ABCDEFGHJKMNPQRSTVWXYZ`
36 | `0123456789abcdefghijklmnopqrstuvwxyz`
58 | `123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz`
62 | `0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`
64 | `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`
66 | `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.!~`

from this we know it's Base 16, since it's the only one that fits the alphabet.

http://www.simplycalc.com/base16-decode.php

### Question 2
We know that this is binary from the zeros and the ones.

http://www.rapidtables.com/convert/number/binary-to-ascii.htm
