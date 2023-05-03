"""merge sort"""
from random import randint

print('1 -- ')
list_ = [randint(1, 100) for _ in range(10)]
print(list_)


print('\n1 -- ')
def mergesort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2  # splits list in half
        left = list_[:mid]
        right = list_[mid:]

        mergesort(left)  # repeats until length of each list is 1
        mergesort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list_[c] = left[a]
                a = a + 1
            else:
                list_[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            list_[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list_[c] = right[b]
            b = b + 1
            c = c + 1
    return list_


sorted_list = mergesort(list_)
print(sorted_list)
