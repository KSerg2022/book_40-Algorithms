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
Алгоритм градиентного бустинга для регрессии
"""

# step 1
from sklearn import ensemble

params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01,
          # 'loss': 'ls',
          'loss': 'squared_error'
          }
regressor = ensemble.GradientBoostingRegressor(**params)

regressor.fit(X_train, y_train)

from sklearn.ensemble import GradientBoostingRegressor
GradientBoostingRegressor(alpha=0.9, criterion='friedman_mse', init=None,
                          learning_rate=0.01,
                          # loss='ls',
                          loss='squared_error',
                          max_depth=4,
                          max_features=None, max_leaf_nodes=None,
                          min_impurity_decrease=0.0,
                          # min_impurity_split=None,
                          min_samples_leaf=1, min_samples_split=2,
                          min_weight_fraction_leaf=0.0, n_estimators=500,
                          n_iter_no_change=None,
                          # presort='auto',
                          random_state=None, subsample=1.0, tol=0.0001,
                          validation_fraction=0.1, verbose=0, warm_start=False)


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
