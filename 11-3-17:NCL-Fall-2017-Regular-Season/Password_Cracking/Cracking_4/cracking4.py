import hashlib

with open("sportsteams.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

passwords = [
    'ad091ecdce588b802857e26fe84ebe66',
    '23e89ae6a99e3dbebe501a38f5d35819',
    '9a675ec8fe4e79fbcc475709970fc228',
    '4d4813d4c34d235560527a7c0897b00a'
]

for password in content:
    hash = hashlib.md5(password).hexdigest()
    if hash in passwords:
        print password
        print passwords.index(hash)
