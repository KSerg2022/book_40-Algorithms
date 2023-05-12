"""
ПРАКТИЧЕСКИЙ ПРИМЕР — СОЗДАНИЕ РЕКОМЕНДАТЕЛЬНОЙ СИСТЕМЫ
"""

print('\n1 -- ')
# step 1
import numpy as np
import pandas as pd

import warnings
#suppress warnings
warnings.filterwarnings('ignore')

# step 2
df_reviews = pd.read_csv('reviews.csv')
df_movie_titles = pd.read_csv('movies.csv', index_col=False)
# print(df_reviews.columns)
# print(df_movie_titles.columns)

# step 3
df = pd.merge(df_reviews, df_movie_titles, on='movieId')
# print(df.columns)

# step 4
df_ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
df_ratings['number_of_ratings'] = df.groupby('title')['rating'].count()
# print(df_ratings.head())

# step 5
movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')

# step 6
Avatar_user_rating = movie_matrix['Avatar (2009)']
Avatar_user_rating = Avatar_user_rating.dropna()
print(Avatar_user_rating.head())

# step 7
similar_to_Avatar=movie_matrix.corrwith(Avatar_user_rating)
corr_Avatar = pd.DataFrame(similar_to_Avatar,
columns=['correlation'])
corr_Avatar.dropna(inplace=True)
corr_Avatar = corr_Avatar.join(df_ratings['number_of_ratings'])
print(corr_Avatar.head())

# step 8
print(corr_Avatar[df_ratings['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10))

# step 9
print('~' * 50)
Thor_user_rating = movie_matrix['Thor (2011)']
Thor_user_rating = Thor_user_rating.dropna()
print(Thor_user_rating)

similar_to_Thor=movie_matrix.corrwith(Thor_user_rating)
print(similar_to_Thor)

corr_Thor = pd.DataFrame(similar_to_Thor, columns=['correlation'])
corr_Thor.dropna(inplace=True)
corr_Thor = corr_Thor.join(df_ratings['number_of_ratings'])
print(corr_Thor.head())

print(corr_Thor[df_ratings['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10))

