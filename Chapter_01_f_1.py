import pandas as pd

df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]])
df.columns = ['id', 'name', 'age', 'decision']
print('1 -- ')
print(df)

print('\n2 -- ')
print(df[['name', 'age']])

print('\n3 -- ')
print(df.iloc[:, 3])

print('\n4 -- ')
print(df.iloc[1:3, :])

print('\n5 -- ')
print(df[df.age > 30])
print()
print(df[(df.age < 35) & (df.decision == True)])


print('\n6 -- ')
import numpy as np

myMatrix = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(myMatrix)

print(type(myMatrix))
transpose_myMatrix = myMatrix.transpose()
print(transpose_myMatrix)
print('\n7 -- ')
print('\n8 -- ')
