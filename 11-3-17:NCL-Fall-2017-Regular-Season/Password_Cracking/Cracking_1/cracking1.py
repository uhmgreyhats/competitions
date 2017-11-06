import hashlib

with open("rockyou.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

passwords = [
    'd4826c5e1070045824fb7ae673f4c28a',
    '8af00675c5f68b72e743b921d351f7d9',
    'f27af865808225ba9172ebe6d928b134',
    '7abbfc8318a0980fd801d450948678a6',
    '5a6d1e9587886eb84c6759188602c571'
]

for password in content:
    hash = hashlib.md5(password).hexdigest()
    if hash in passwords:
        print password
        print passwords.index(hash)
