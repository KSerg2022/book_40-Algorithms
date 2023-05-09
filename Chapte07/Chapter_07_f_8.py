"""
АЛГОРИТМЫ РЕГРЕССИИ
"""

print('\n1 -- ')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.metrics as metrics

# print(sklearn.__version__)

dataset = pd.read_csv('auto.csv')
dataset = dataset.drop(columns=['NAME'])
dataset.head(5)
# print(dataset.head(5))

dataset = dataset.apply(pd.to_numeric, errors='coerce')
dataset.fillna(0, inplace=True)

from sklearn.model_selection import train_test_split

y = dataset['MPG']
X = dataset.drop(columns=['MPG'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


"""
Линейная регрессия
"""

# step 1, 2
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# step 3
y_pred = regressor.predict(X_test)
from sklearn.metrics import mean_squared_error
from math import sqrt
rt = sqrt(mean_squared_error(y_test, y_pred))

# step 4
print(rt)
"RMSE — это стандартное отклонение для ошибок. " \
"Оно указывает на то, что 68,2 % прогнозов будут находиться в пределах 4.36 " \
"от значения целевой переменной."
