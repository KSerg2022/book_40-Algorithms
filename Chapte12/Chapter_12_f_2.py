"""
Криптография
ТИПЫ КРИПТОГРАФИЧЕСКИХ МЕТОДОВ

Криптографические хеш-функции.
"""

print('\n1 -- Алгоритм MD5')
from passlib.hash import md5_crypt

myHash = md5_crypt.hash("myPassword")
print(myHash)

md5_crypt.verify("myPassword", myHash)
print(md5_crypt.verify("myPassword", myHash))

md5_crypt.verify("myPassword2", myHash)
print(md5_crypt.verify("myPassword2", myHash))


print('\n2 -- Алгоритм SHA')
from passlib.hash import sha512_crypt

myHash = sha512_crypt.using(salt="qIo0foX5", rounds=5000).hash("myPassword")
print(myHash)


print('\n3 -- ')
