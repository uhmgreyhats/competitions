# Database Dump
It seems that a database at the Metro General Hospital has been compromised. Analyze the database dump to help them recover.

## Questions
1. What is the name of the database (case-sensitive)?
2. How many tables are in the database?
3. How many patients are included in this database dump?
4. What hashing algorithm is used for User passwords?
5. We think Andreas has an unsecure password. What is it?
6. What is the email address of the account that the hacker created?
7. What is the plaintext password for the hacker's account?

## Answers
1. hospital
2. 25
3. 4
4. sha1
5. KramBamBuli
6. cyph3r@hacknet.cityinthe.cloud
7. Astrid

## Walkthroughs

We can see the name of the database in line 8 and 10 of the log.
`DROP DATABASE IF EXISTS hospital;`
and
`CREATE DATABASE hospital;`.

We can see the amount of tables by finding the amount of `CREATE TABLE` strings there are in the file.

We can view the amount of patients included by getting the amount of `INSERT INTO `PATIENT`` strings there are.

We can get the hashing algorithm by viewing one of the User entries and seeing what encoding is used for their passwords.
```
INSERT INTO `User`
(`uid`,`LastName`,`FirstName`,`Email`,`Password`)
VALUES ('fu','Fuerst','Andreas','afeurst@metrogeneral.cityinthe.cloud','6e58f76f5be5ef06a56d4eeb2c4dc58be3dbe8c7');
```
A simple search reveals that this is sha1.

We can plug Andreas's password into any [sha1 decrypter](https://hashkiller.co.uk/sha1-decrypter.aspx).
This reveals the password is `KramBamBuli`.

The same set of steps can be applied to find the password of the hacker's entry. Using this suspicious entry,

```
INSERT INTO `User`
(`uid`,`LastName`,`FirstName`,`Email`,`Password`)
('1337','Hacker','Happy','cyph3r@hacknet.cityinthe.cloud','6b97f534c330b5cc78d4cc23e01e48be3377105b');
```
and plugging the password hash into a sha1 decrypter to reveal the password of `Astrid`.
