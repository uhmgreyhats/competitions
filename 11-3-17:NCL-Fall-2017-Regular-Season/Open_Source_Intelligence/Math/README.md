# Math
Help double check the work of some new recruits by doing some binary math. Provide your answers in base 10.

## Questions
1. 0x49  |  0xDE
2. 0x9E  &  0xFE
3. 0x5  ^  0x56
4. 0xDD  >>  1
5. 0x27  <<  2

## Answers
1. 223
2. 158
3. 83
4. 110
5. 156

## Resources
```
bit-hacks

notation

|   -  bitwise or
&   -  bitwise and
~   -  bitwise not
^   -  bitwise xor
<<  -  bitwise shift left
>>  -  bitwise shift right
operations

not(0) = 1 => ~0
not(1) = 0 => ~1

0 or 0 = 0 => 0|0
0 or 1 = 1 => 0|1
1 or 0 = 1 => 1|0
1 or 1 = 1 => 1|1

0 and 0 = 0 => 0&0
0 and 1 = 0 => 0&1
1 and 0 = 0 => 1&0
1 and 1 = 1 => 1&1

0 xor 0 = 0 => 0^0
0 xor 1 = 1 => 0^1
1 xor 0 = 1 => 1^0
1 xor 1 = 0 => 1^1
x & x = x   => 1010 & 1010 == 1010
x & 0s = 0  => 1010 & 0000 == 0000
x & 1s = x  => 1010 & 1111 == 1010

x | x = x   => 1010 | 1010 == 1010
x | 0s = x  => 1010 | 0000 == 1010
x | 1s = 1s => 1010 | 1111 == 1111

x ^ x = 0   => 1010 ^ 1010 == 0000
x ^ 0s = x  => 1010 ^ 0000 == 1010
x ^ 1s = ~x => 1010 ^ 1111 == 0101
shift-left & shift-right

2 << 1 => '4', the same as 2 * (2**1)
2 << 2 => '8', the same as 2 * (2**2)
8 >> 1 => '4', the same as 8 / (2**1)
8 >> 2 => '2', the same as 8 / (2**2)
9 >> 2 => '2', the same as 9 / (2**2)
9 << 4 => '144', the same as 9 * (2**4)
Credit

https://github.com/knoxknox/bit-hacks
```
