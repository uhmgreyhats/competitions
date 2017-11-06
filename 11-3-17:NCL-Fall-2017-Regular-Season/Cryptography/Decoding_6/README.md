# Decoding 6
It looks like the hackers have gotten more creative and invented a custom protocol for encrypting messages. Good thing they are terrible at physical security. We've obtained a sticky note with the ruleset they are using. We have filtered the relevant parts. It is up to you to decrypt the message and find out what they are up to.

```
================RULESET================
| A = H | H = A  | E = 2E  | M = M+3  |
| 6 = S | G = K  | 16 = U  | 2J = D/2 |
| I = T | C = Y  | 3D = 15 |          |
| B = 3 | 22 = Q | 19 = 4C |          |
| N = D | U = 23 | Z-1 = 6 |          |
|===============MESSAGE===============|
|  QWOD AQHY LFLBJP TL UWCOTY SHYTDK  |
|---------------DECRYPT---------------|
|       H A                    A      |
=======================================
```

## Questions
1. What is the plaintext of the encrypted message?

## Answers
1. VULN HVAC SYSTEM IS PUBLIC FACING
