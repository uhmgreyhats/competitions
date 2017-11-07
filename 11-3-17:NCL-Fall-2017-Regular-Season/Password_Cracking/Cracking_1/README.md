# Cracking 1
Our officers have obtained password dumps storing hacker passwords. After obtaining a few plaintext passwords, it appears that they overlap with the passwords from the rockyou breach.

## Questions
1. d4826c5e1070045824fb7ae673f4c28a
2. 8af00675c5f68b72e743b921d351f7d9
3. f27af865808225ba9172ebe6d928b134
4. 7abbfc8318a0980fd801d450948678a6
5. 5a6d1e9587886eb84c6759188602c571

## Answers
1. msaf12
2. nadia24
3. brat47
4. rl2909
5. Quantegy01

## Walkthroughs
Loop through `rockyou.txt`, generate the md5 hash for each word, and compare to the hashes above.

Solution in `cracking1.py`.
