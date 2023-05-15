"""
Криптография

"""

print('\n1 -- Шифр Цезаря')
import string

rotation = 3
P = 'CALM'
C = ''
for letter in P:
    C = C + (chr(ord(letter) + rotation))

print(P)
print(C)

print('\n2 -- Rotation 13 (ROT13)')
import codecs

P = 'CALM'
C = ''
C = codecs.encode(P, 'rot_13')

print(P)
print(C)

print('\n3 -- ')
import codecs
my_bytes = b"Algorithms are great"
r = codecs.encode(my_bytes, "base64")
print(my_bytes)
print(r)

