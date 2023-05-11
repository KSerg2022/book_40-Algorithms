"""
Алгоритмы обработки естественного языка
РЕКУРРЕНТНЫЕ НЕЙРОСЕТИ В NLP

ИСПОЛЬЗОВАНИЕ NLP ДЛЯ АНАЛИЗА ЭМОЦИОНАЛЬНОЙ ОКРАСКИ ТЕКСТА
"""

print('\n1 -- ')
"""ПРАКТИЧЕСКИЙ ПРИМЕР — АНАЛИЗ ТОНАЛЬНОСТИ
В ОТЗЫВАХ НА ФИЛЬМЫ"""

# step 1
import pandas as pd
import numpy as np

# step 2
df = pd.read_csv("moviereviews.tsv", sep='\t')
# print(df.head())
# print(len(df))

# step 3
df.dropna(inplace=True)
# print(len(df))

# step 4
blanks = []
for i, lb, rv in df.itertuples():
    # print(i, '****', lb, '~~~~', rv)
    if rv.isspace():
        blanks.append(i)
        df.drop(blanks, inplace=True)

# step 5
# substep 5.1
from sklearn.model_selection import train_test_split
X = df['review']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# substep 5.2
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
text_clf_nb = Pipeline([('tfidf', TfidfVectorizer()), ('clf', MultinomialNB()), ])

# substep 5.3
text_clf_nb.fit(X_train, y_train)

predictions = text_clf_nb.predict(X_test)

# substep 5.4
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

print(confusion_matrix(y_test, predictions))
print()

print(classification_report(y_test, predictions))
print()

print(accuracy_score(y_test, predictions))
