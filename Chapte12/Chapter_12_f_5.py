"""
Криптография

ПРАКТИЧЕСКИЙ ПРИМЕР — ПРОБЛЕМЫ БЕЗОПАСНОСТИ ПРИ РАЗВЕРТЫВАНИИ МОДЕЛИ МО

"""
import pickle

print('\n1 -- Шифрование данных и моделей')
# step 1
import cryptography as crypt
from sklearn.linear_model import LogisticRegression
from cryptography.fernet import Fernet
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LogisticRegression()
model.fit(X_train, y_train)


# step 2
filename_source = 'myModel_source.sav'
filename_destination = "myModel_destination.sav"
filename_sec = "myModel_sec.sav"


# step 3
from pickle import dump
dump(model, open(filename_source, 'wb'))


# step 4
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# step 5
def load_key():
    return open("key.key", "rb").read()


# step 6
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename_source, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename_sec, "wb") as file:
        file.write(encrypted_data)


# step 7
write_key()
encrypt(filename_source,load_key())


# step 8
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename_sec, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename_destination, "wb") as file:
        file.write(decrypted_data)


# step 9
decrypt(filename_sec,load_key())


# step 10
loaded_model = pickle.load((open(filename_destination, 'rb')))
result = loaded_model.score(X_test, y_test)
print(result)
