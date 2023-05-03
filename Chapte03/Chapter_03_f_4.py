"""Shell sort"""
from random import randint


list_ = [randint(1, 100) for _ in range(10)]
print(list_)
print('\n1 -- ')

def shellsort(list_):
    distanse = len(list_) // 2
    while distanse > 0:
        for i in range(distanse, len(list_)):
            temp = list_[i]
            j = i
            while j >= distanse and list_[j - distanse] > temp:
                list_[j] = list_[j - distanse]
                j = j - distanse
            list_[j] = temp

        distanse = distanse // 2
    return list_

sorted_list = shellsort(list_)
print(sorted_list)

