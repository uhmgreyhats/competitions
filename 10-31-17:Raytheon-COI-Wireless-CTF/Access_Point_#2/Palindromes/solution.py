ans = []

for one in range(1000, 9999):
    for two in range(1000, 9999):
        if str(one * two) == str(one * two)[::-1]:
            ans = [one, two, one * two]

print ans
