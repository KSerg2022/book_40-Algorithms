"""ОБУЧЕНИЕ БЕЗ УЧИТЕЛЯ"""

print('\n1 -- ')
"""АЛГОРИТМЫ КЛАСТЕРИЗАЦИИ"""

print('\n2 -- ')
"""Логика кластеризации методом k-средних"""
# step 1
from sklearn import cluster
import pandas as pd
import numpy as np

# import warnings
# warnings.filterwarnings("ignore")

# step 2
dataset = pd.DataFrame({
    'x': [11, 21, 28, 17, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53,
          55, 61, 62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23,
          14, 8, 18, 7, 24, 10]
})

# step 3
k = 2
# myKmeans = cluster.KMeans(n_clusters=k)
myKmeans = cluster.KMeans(n_clusters=k, n_init='auto')
myKmeans.fit(dataset)

# step 4
centroids = myKmeans.cluster_centers_
labels = myKmeans.labels_

# step 5
print(centroids)
print(labels)

# step 6
import matplotlib.pyplot as plt
plt.scatter(dataset['x'], dataset['y'], s=10)
plt.scatter(centroids[0], centroids[1], s=100)
# plt.scatter([x[0] for x in centroids], [x[1] for x in centroids], s=100)  # k=3
plt.show()

print('\n3 -- ')
