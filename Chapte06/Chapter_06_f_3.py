"""
СНИЖЕНИЕ РАЗМЕРНОСТИ
Метод главных компонент (PCA) (principal component analysis)
"""

print('\n1 -- ')
import pandas as pd
import numpy as np

dataset = pd.DataFrame({
    'x': [11, 21, 28, 17, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53,
          55, 61, 62, 70, 72, 10],
    'y': [39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23,
          14, 8, 18, 7, 24, 10]
})

from sklearn.decomposition import PCA

iris = pd.read_csv('iris.csv')
X = iris.drop('Species', axis=1)
pca = PCA(n_components=4)
pca.fit(X)

print(pd.DataFrame(pca.components_, columns=X.columns))
print()


pca_df = (pd.DataFrame(pca.components_, columns=X.columns))

# Рассчитаем PC1, используя генерируемые коэффициенты
X['PC1'] = X['Sepal.Length'] * pca_df['Sepal.Length'][0] + X['Sepal.Width'] *\
           pca_df['Sepal.Width'][0] + X['Petal.Length'] * \
pca_df['Petal.Length'][0] + X['Petal.Width'] * pca_df['Petal.Width'][0]
# Вычислим PC2
X['PC2'] = X['Sepal.Length'] * pca_df['Sepal.Length'][1] + X['Sepal.Width'] *\
           pca_df['Sepal.Width'][1] + X['Petal.Length'] * \
pca_df['Petal.Length'][1] + X['Petal.Width'] * pca_df['Petal.Width'][1]
# Вычислим PC3
X['PC3'] = X['Sepal.Length'] * pca_df['Sepal.Length'][2] + X['Sepal.Width'] *\
           pca_df['Sepal.Width'][2] + X['Petal.Length'] *\
pca_df['Petal.Length'][2] + X['Petal.Width'] * pca_df['Petal.Width'][2]
# Вычислим PC4
X['PC4'] = X['Sepal.Length'] * pca_df['Sepal.Length'][3] + X['Sepal.Width'] *\
           pca_df['Sepal.Width'][3] + X['Petal.Length'] *\
pca_df['Petal.Length'][3] + X['Petal.Width'] * pca_df['Petal.Width'][3]

print(X)
print()


print(pca.explained_variance_ratio_)
