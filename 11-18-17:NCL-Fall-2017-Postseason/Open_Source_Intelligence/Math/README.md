# Math
Help double check the work of some new recruits by doing some binary math. Provide your answers in base 10.

## Questions
1. 0x2A  |  0x14
2. 0x8  &  0x65
3. 0xBF  ^  0xE1
4. 0xFC  >>  1
5. 0x40  <<  2

## Answers
1. 62
2. 0
3. 94
4. 126
5. 256

## Walkthrough
Open up the python shell, and paste the binary math into the shell
```
❯ python
Python 2.7.13 (default, Apr  4 2017, 08:47:57)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x2A  |  0x14
62
>>> 0x8  &  0x65
0
>>> 0xBF  ^  0xE1
94
>>> 0xFC  >>  1
126
>>> 0x40  <<  2
256
```
