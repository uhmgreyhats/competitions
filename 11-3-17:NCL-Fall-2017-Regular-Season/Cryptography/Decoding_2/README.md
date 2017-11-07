# Decoding 2
Our officers have obtained some encrypted codes. See if you can decode them. We know they should start with "SKY".

## Questions
1. FXL-TUHX-0026
2. HZN-ADQU-7992

## Answers
1. SKY-GHUK-0026
2. SKY-LOBF-7992

## Walkthroughs

We can guess that both of these are some sort of shift cipher due to the fact that the amount of characters don't actually change.

From here, we can brute force the amount the characters are being shifted by and seeing which ones start with either `NCL` or `SKY`, since it seems that is the flag format they are using.
