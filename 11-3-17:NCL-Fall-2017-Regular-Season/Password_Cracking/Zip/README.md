# Zip
We have recovered a flash drive with a password-protected archive. Help us decrypt it.

## Questions
1. What is the password used to encrypt the archive?
2. What is the flag found in the archive?

## Answers
1. youcantseemee
2. SKY-ZIPD-7190

## Walkthroughs
Cracked using `fcrackzip` with `rockyou.txt`.
`fcrackzip -u -D -p "rockyou.txt" Flag.zip`
