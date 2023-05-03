"""interpolation search"""

list_ = [12, 33, 55, 41, 7, 26, 17, 31, 20, 1]
print(list_)
print('\n1 -- ')


def intpolsearch(list_, x):
    idx0 = 0
    idxn = len(list_) - 1
    found = False

    while idx0 <= idxn and (x >= list_[idx0]) and (x <= list_[idxn]):

        mid = idx0 + int(((float(idxn - idx0) / (list_[idxn] - list_[idx0])) * (x - list_[idx0])))
        if list_[mid] == x:
            found = True
            return found
        if list_[mid] < x:
            idx0 = mid + 1

    return found

list_ = sorted(list_)
number = 31
searched_result = intpolsearch(list_, number)
print(searched_result)

number = 100
searched_result = intpolsearch(list_, number)
print(searched_result)

number = 17
searched_result = intpolsearch(list_, number)
print(searched_result)