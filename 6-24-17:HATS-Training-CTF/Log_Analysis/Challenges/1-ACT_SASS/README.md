# ACT SASS
Here's this access log. Better get them all.

## Questions
1. **How many clients are trying to access stuff?**
2. **What IP has a dragon in it?**
3. **What version of OS X is used?**
4. **How many requests were bad?**
5. **How many requests were not found?**
6. **How many requests had a bad gateway?**
7. **How many requests were moved?**
8. **What was ringing?**
9. **How many instances of the earliest geckotrail are there?**


## Steps

### Question 1
1. [Google 'How to find unique IP addresses in log file'](https://stackoverflow.com/questions/18682308/sort-uniq-ip-address-in-from-apache-log)
2. `cat access.log | awk '{print $1}' | sort -n | uniq -c | sort -nr | head -20 | wc -l`

### Question 2
1. Try to find 'dragon' using grep
2. `egrep -i 'dragon'`
3. No results
4. Read the log file
5. See 'COMODO SSL Checker'
6. Input that IP

### Question 3
1. `egrep -i 'os x' access.log`

### Question 4
1. [Google 'status code bad http request'](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
2. See that it is '400'
3. `egrep -i '400' access.log | wc -l`

### Question 5
1. Know that Not Found is '404'
2. `egrep -i '404' access.log | wc -l`

### Question 6
1. See that Bad Gateway is '502'
2. `egrep -i '502' access.log | wc -l`

### Question 7
1. See that Moved Permanently is '301'
2. `egrep -i '301' access.log | wc -l`

### Question 8
1. `egrep -i 'ring' access.log`
2. See '/Ringing.at.your.dorbell!'

### Question 9
1. `egrep -i 'gecko' access.log`
2. See 19 results
3. Try 19
4. Fail
5. Earliest Version?
6. Look for smallest version number
7. See that its '20100101'
8. `egrep -i '20100101' access.log | wc -l`
