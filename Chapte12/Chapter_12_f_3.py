"""
Криптография
Симметричное шифрование


"""

print('\n1 -- Реализация симметричного шифрования')
import cryptography as crypt
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

file = open('mykey.key', 'wb')
file.write(key)
file.close()

file = open('mykey.key', 'rb')
key = file.read()
file.close()


from cryptography.fernet import Fernet
message = "Ottawa is really cold".encode()
print(message)

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)


print('\n2 -- ')
