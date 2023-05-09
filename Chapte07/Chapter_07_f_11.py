"""
ПРАКТИЧЕСКИЙ ПРИМЕР — КАК ПРЕДСКАЗАТЬ ПОГОДУ
"""

print('\n1 -- ')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.metrics as metrics

# print(sklearn.__version__)

df = pd.read_csv('weather.csv')
# print(df.columns)
# print(df.iloc[:, 0:12].head())
# print(df.iloc[:, 12:25].head())

df['RainToday'] = df['RainToday'].apply(lambda x: 1 if x == "Yes" else 0)
df['RainTomorrow'] = df['RainTomorrow'].apply(lambda x: 1 if x == "Yes" else 0)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df = df.dropna()
# print(df.shape)

df.WindGustDir = le.fit_transform(df.WindGustDir)
df.WindDir3pm = le.fit_transform(df.WindDir3pm)
df.WindDir9am = le.fit_transform(df.WindDir9am)

from sklearn.model_selection import train_test_split

x = df.drop(['Date', 'RainTomorrow'], axis=1)
y = df['RainTomorrow']
train_x, train_y, test_x, test_y = train_test_split(x, y, test_size=0.2, random_state=2)

# print(train_x.shape)
# print(train_y.shape)

"""
Алгоритм градиентного бустинга для регрессии
"""
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(train_x, test_x)

LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='warn', n_jobs=None, penalty='l2',
                   random_state=None, solver='warn', tol=0.0001, verbose=0,
                   warm_start=False)

predict = model.predict(train_y)

from sklearn.metrics import accuracy_score

rt = accuracy_score(predict, test_y)
print(rt)
