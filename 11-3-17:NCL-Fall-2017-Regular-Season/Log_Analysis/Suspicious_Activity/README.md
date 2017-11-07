# Suspicious Activity
The Department of Cyber Crime has strict access requirements, anyone entering or exiting the restricted area must badge in and out. But the Director of the Department thinks there is something suspicious going on. Help the Director identify it.

## Questions
1. How many total employees are there?
2. How many total kilobytes were transfered by the employees?
3. When did the highly suspicious incident take place? (round to nearest minute)

## Answers
1. 300
2. 65179621
3. 2017/01/05 10:09

## Walkthroughs

Attached as a script `susactivity.py` is the solutions to these questions.

For question 1, just loop over both files and push unique names into an array and print the length.

For question 2, loop over `access.log` and get all the numbers before KB and add them all up at the end.

For question 3, loop over both files and check for access when not swiped in.
