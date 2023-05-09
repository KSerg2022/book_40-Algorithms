"""
МАШИННОЕ ОБУЧЕНИЕ С УЧИТЕЛЕМ

АЛГОРИТМЫ КЛАССИФИКАЦИИ
"""
print('\n1 -- ')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.metrics as metrics

print(sklearn.__version__)

dataset = pd.read_csv('Social_Network_Ads.csv')
dataset = dataset.drop(columns=['User ID'])
dataset.head(5)
print(dataset.head(5))

enc = sklearn.preprocessing.OneHotEncoder()
enc.fit(dataset.iloc[:, [0]])
onehotlabels = enc.transform(dataset.iloc[:, [0]]).toarray()
genders = pd.DataFrame({'Female': onehotlabels[:, 0], 'Male': onehotlabels[:, 1]})
result = pd.concat([genders, dataset.iloc[:, 1:]], axis=1, sort=False)
result.head(5)
print(result.head(5))

y = result['Purchased']
X = result.drop(columns=['Purchased'])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=0)


from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



