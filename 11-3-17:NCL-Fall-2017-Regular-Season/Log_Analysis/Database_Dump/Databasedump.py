with open("Datbase Dump.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

# How many tables are in the database?
for line in content:
    if 'CREATE TABLE' in line:
        print line
