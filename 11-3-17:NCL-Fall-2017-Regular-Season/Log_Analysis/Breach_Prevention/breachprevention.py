with open("Breach Prevention.log") as f:
    content = f.readlines()
content = [x.strip() for x in content]

# How many total attacks were blocked by the breach prevention software?
i = 0
for line in content:
    if ('Blocking reason:' in line):
        i += 1
print 'How many total attacks were blocked by the breach prevention software?'
print i

# How many different types of attacks are listed in this log?
obj = {}
for line in content:
    if ('Blocking reason' in line):
        string = line.replace('Blocking reason: ', '')
        if string in obj:
            obj[string] += 1
        else:
            obj[string] = 0
print 'How many different types of attacks are listed in this log?'
print len(obj)

# How many remote file inclusion attacks were prevented?
i = 0
for line in content:
    if ('Blocking reason: rfishield' == line):
        i += 1
print 'How many remote file inclusion attacks were prevented?'
print i

# What IP address attempted the most attacks?
# How many different IP addresses attempted an attack on this server?
obj = {}
for line in content:
    if ('IP' in line):
        string = line.replace('IP        : ', '')
        if string in obj:
            obj[string] += 1
        else:
            obj[string] = 0
print 'What IP address attempted the most attacks?'
for key in obj:
    if (obj[key] == max(obj[key] for key in obj)):
        print key
print 'How many different IP addresses attempted an attack on this server?'
print len(obj)

# What URL was blocked the most often by the direct file inclusion defense?
urls = {}
dfishield = False
for line in content:
    if dfishield == True:
        if 'URL' in line:
            url = line.replace('URL       : ', '')
            if url in urls:
                urls[url] = urls[url] + 1
            else:
                urls[url] = 0
            dfishield = False
    else:
        if ('dfishield' in line):
            dfishield = True

for key in urls:
    if (urls[key] == max(urls[key] for key in urls)):
        print 'What URL was blocked the most often by the direct file inclusion defense?'
        print key
