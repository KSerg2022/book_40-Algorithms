"""selection sort"""

from random import randint


list_ = [randint(1, 100) for _ in range(10)]
print(list_)
print('\n1 -- ')

def selectionsort(list_):
    for fill_sort in range(len(list_) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_sort + 1):
            if list_[location] > list_[max_index]:
                max_index = location
        list_[fill_sort], list_[max_index] = list_[max_index], list_[fill_sort]

    return list_

sorted_list = selectionsort(list_)
print(sorted_list)
