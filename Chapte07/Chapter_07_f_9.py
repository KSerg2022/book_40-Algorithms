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
Алгоритм дерева регрессии
"""

# step 1
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(max_depth=3)
regressor.fit(X_train, y_train)

DecisionTreeRegressor(criterion='mse', max_depth=3, max_features=None,
                      max_leaf_nodes=None, min_impurity_decrease=0.0,
                      # min_impurity_split=None,
                      min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      # presort=False,
                      random_state=None, splitter='best')

# step 2
y_pred = regressor.predict(X_test)

# step 3
from sklearn.metrics import mean_squared_error
from math import sqrt

rt = sqrt(mean_squared_error(y_test, y_pred))

print(rt)
"RMSE — это стандартное отклонение для ошибок. " \
"Оно указывает на то, что 68,2 % прогнозов будут находиться в пределах 4.36 " \
"от значения целевой переменной."
