# Cracking 3
Our officers have obtained password dumps storing hacker passwords. It appears that they are all in the format: "SKY-PWDS-" followed by 4 digits. Can you crack them?

## Questions
1. f085cd004172c971cdcc19a2fc52d09e
2. 9c4e95806cce83c4286f0f0fb5ccae5f
3. 51b7f45b2e6c6d883370ac70445443d4
4. 7bec7e80158930232b1ae144bab32189
5. 9dda6ca6930910d260f2aadf8a16519a

## Answers
1. SKY-PWDS-0687
2. SKY-PWDS-0430
3. SKY-PWDS-6406
4. SKY-PWDS-1568
5. SKY-PWDS-1929

## Walkthroughs
First, we generate all permutations of 4 digit numbers from 0000 to 9999. Generate hashes based off our new string, and compare them to what is in our list.

Solution is in `cracking3.py`.
