"""
Алгоритмы нейронных сетей
Построение модели Keras
"""
from keras.datasets import mnist

print('\n1 -- ')

# 1. Конструирование слоев.

# Последовательный API (Sequential API)1.
import tensorflow as tf

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from keras.datasets import mnist


# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.15),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.15),
    tf.keras.layers.Dense(10, activation='softmax'),
])
print(model)


print('\n2 -- ')
# Функциональный API (Functional API)

# inputs = tf.keras.Input(shape=(128, 128))
# x = tf.keras.layers.Flatten()(inputs)
# x = tf.keras.layers.Dense(512, activation='relu', name='d1')(x)
# x = tf.keras.layers.Dropout(0.2)(x)
# predictions = tf.keras.layers.Dense(10, activation=tf.nn.softmax, name='d2')(x)
# model = tf.keras.Model(inputs=inputs, outputs=predictions)
# print(model)


print('\n3 -- ')
# 2. Настройка процесса обучения.
# optimiser = tf.keras.optimizers.RMSprop
# model.compile(optimizer=optimiser, loss='mse', metrics=['accuracy'])


model.compile(optimizer='rmsprop', loss='mse', metrics=['accuracy'])

# 3. Обучение модели.
model.fit(x_train, y_train, batch_size=128, epochs=10)


