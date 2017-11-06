# How many total kilobytes were transfered by the employees?

import re

with open("access.log") as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0

for line in content:
    kb = re.findall(r'\d+', line)[-1]
    total += int(kb)

print 'How many total kilobytes were transfered by the employees?'
print total

# Suspicious Activity

import re
from dateutil import parser

obj = {}

with open("badge.log") as f:
    content = f.readlines()
content = [x.strip() for x in content]

# Check for double swipe in or double swipe outs
# Didn't work, revised to store time of swipe in and swipe outs

for line in content:
    person = line[line.find("[")+1:line.find("]")]
    if (person not in obj):
        datestring = line[0:line.find("[")]
        dt = parser.parse(datestring)
        obj[person] = {
            'times': [{
                'in': dt
            }],
            'status': 'In'
        }
    else:
        if ('Swipe In' in line):
            if (obj[person]['status'] == 'In'):
                print 'Already in!'
                print line
                break
            else:
                obj[person]['status'] = 'In'
                datestring = line[0:line.find("[")]
                dt = parser.parse(datestring)
                obj[person]['times'].append({
                    'in': dt
                })
        else:
            if (obj[person]['status'] == 'Out'):
                print 'Already out!'
                print line
                break
            else:
                obj[person]['status'] = 'Out'
                datestring = line[0:line.find("[")]
                dt = parser.parse(datestring)
                obj[person]['times'][-1]['out'] = dt

# Check for Access when not swiped in
with open("access.log") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for line in content:
    person = line[line.find("[")+1:line.find("]")]
    datestring = line[0:line.find("[")]
    dt = parser.parse(datestring)
    times = obj[person]['times']
    valid = False
    for time in times:
        if 'out' in time:
            if dt >= time['in'] and dt <= time['out']:
                valid = True
        else:
            if dt >= time['in']:
                valid = True

    if valid == False:
        print 'Suspicious Activity'
        print line
