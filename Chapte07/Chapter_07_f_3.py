"""
АЛГОРИТМЫ КЛАССИФИКАЦИИ
"""

print('\n1 -- ')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.metrics as metrics

# print(sklearn.__version__)

dataset = pd.read_csv('Social_Network_Ads.csv')
dataset = dataset.drop(columns=['User ID'])
dataset.head(5)
# print(dataset.head(5))

enc = sklearn.preprocessing.OneHotEncoder()
enc.fit(dataset.iloc[:, [0]])
onehotlabels = enc.transform(dataset.iloc[:, [0]]).toarray()
genders = pd.DataFrame({'Female': onehotlabels[:, 0], 'Male': onehotlabels[:, 1]})
result = pd.concat([genders, dataset.iloc[:, 1:]], axis=1, sort=False)
result.head(5)
# print(result.head(5))

y = result['Purchased']
X = result.drop(columns=['Purchased'])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""
Ансамблевые методы
Реализация градиентного бустинга с помощью алгоритма XGBoost
"""

# step 1
from xgboost import XGBClassifier

classifier = XGBClassifier()
classifier.fit(X_train, y_train)

XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0,
              learning_rate=0.1, max_delta_step=0, max_depth=3,
              min_child_weight=1, missing=None, n_estimators=100, n_jobs=1,
              nthread=None, objective='binary:logistic', random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
              silent=None, subsample=1, verbosity=1)

# step 2
y_pred = classifier.predict(X_test)
cm = metrics.confusion_matrix(y_test, y_pred)
print(cm)

# step 3
accuracy = metrics.accuracy_score(y_test, y_pred)
recall = metrics.recall_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred)
print(accuracy, recall, precision)
