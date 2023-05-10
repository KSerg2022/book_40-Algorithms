"""
Алгоритмы нейронных сетей
"""
import tensorflow as tf

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from keras.datasets import mnist

print('\n1 -- ')
# Понимание тензорной математики
print('Define constant tensors')
a = tf.constant(2)
print('a = ', a)

print('a = %i' % a)
# print(f'a = {a}')

b = tf.constant(3)
print('b = %i' % b)

print('Runnibg operations, wiyhout tf.Session')
c = a + b
print(f'a + b = {c}')

d = a * b
print(f'a * b = {d}')

# Создадим новый скаляр, сложив два тензора
c = a + b
print('a + b = %s' % c)


# Выполним сложные тензорные функции. ??????????????
d = tf.matmul(a, b)
print('a * b = %s' % d)
print(f'a * b = {d}')
print(d)

print('\n2 -- ')
# Понимание тензорной математики



