import hashlib
import itertools

passwords = [
    'f085cd004172c971cdcc19a2fc52d09e',
    '9c4e95806cce83c4286f0f0fb5ccae5f',
    '51b7f45b2e6c6d883370ac70445443d4',
    '7bec7e80158930232b1ae144bab32189',
    '9dda6ca6930910d260f2aadf8a16519a'
]

words = []

for combination in itertools.product(xrange(10), repeat=4):
    words.append('SKY-PWDS-' + ''.join(map(str, combination)))

for word in words:
    hash = hashlib.md5(word).hexdigest()
    if hash in passwords:
        print word
        print passwords.index(hash)
