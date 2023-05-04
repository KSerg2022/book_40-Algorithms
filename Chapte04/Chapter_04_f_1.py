"""стратегию «разделяй и властвуй"""

print('\n1 -- ')

import findspark
findspark.init()

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext

wordsList = ['python', 'java', 'ottawa', 'ottawa', 'java', 'news']
wordsRDD = sc.parallelize(wordsList, 4)
# Напечатать тип wordsRDD
print(wordsRDD.collect())

wordsPairs = wordsRDD.map(lambda w: (w, 1))
print(wordsPairs.collect())

wordcountscollected = wordsPairs.reduceByKey(lambda x, y: x + y)
print(wordcountscollected.collect())

print('\n2 -- ')
