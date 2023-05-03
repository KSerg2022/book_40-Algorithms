"""insertion sort"""
from random import randint

print('1 -- ')
list_ = [randint(1, 100) for _ in range(10)]
print(list_)

print('\n1 -- ')


def insertionsort(list_):
    for i in range(1, len(list_)):
        j = i - 1
        element_next = list_[i]
        while (list_[j] > element_next) and (j >= 0):
            list_[j+1] = list_[j]
            j -= 1
        list_[j + 1] = element_next
    return list_


sorted_list = insertionsort(list_)
print(sorted_list)

print('\n2 -- ')