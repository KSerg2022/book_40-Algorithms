"""bubble sort"""
from random import randint

print('1 -- ')
list_ = [randint(1, 100) for _ in range(10)]
print(list_)
print()


def bubblesort(list_):
    last_element_index = len(list_) - 1
    for pass_num in range(last_element_index, 0, -1):
        for i in range(pass_num):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
    return list_

print()
sorted_list = bubblesort(list_)
print(sorted_list)


print('\n2 -- ')


print('\n3 -- ')


print('\n4 -- ')


print('\n5 -- ')

print('\n6 -- ')
print('\n7 -- ')
print('\n8 -- ')
