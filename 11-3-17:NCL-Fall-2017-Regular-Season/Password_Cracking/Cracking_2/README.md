# Cracking 2
Our officers have obtained password dumps storing hacker passwords. Try your hand at cracking them.

## Questions
1. 56564EA65F4FCF6525AD3B83FA6627C7:FECFBBB7EF48BF30809F5E750B5C108D
2. 2399282AB08FDAAF9797D56B534FC4AA:57DE71FF5A243FF4741936805F0DB204
3. 036A3F894D2952B9BC38DC1ED04728A3:67A42D17DAABDA8185B6DCA035EBA1F9
4. 23282069BD000B4F1AF20D40CE60A309:CF986DDF1D29AE0589DEBDFE926DEC81
5. F7F7CB8FA131FF971E5DEC7B7AE875E5:9ACE387CB1BB2B50A3A06381A2038BBE

## Answers
1. obopim20
2. ufanuj526
3. xitezonoca1261
4. mint412ruth999
5. NewsListen6

## Walkthroughs
These are NTLM hashes, so we need to crack them a bit differently.

We can download [ophcrack](http://ophcrack.sourceforge.net/), then run the following command.

`ophcrack -g -t . -f hashfile`.

This cracks all the passwords.
