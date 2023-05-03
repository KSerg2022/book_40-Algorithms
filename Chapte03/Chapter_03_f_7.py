"""binary search"""

list_ = [12, 33, 55, 41, 7, 26, 17, 31, 20, 1]
print(list_)
print('\n1 -- ')


def binarysearch(list_, number):
    first = 0
    last = len(list_) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if list_[midpoint] == number:
            found = True
        else:
            if number < list_[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

list_ = sorted(list_)
number = 31
searched_result = binarysearch(list_, number)
print(searched_result)

number = 100
searched_result = binarysearch(list_, number)
print(searched_result)

number = 17
searched_result = binarysearch(list_, number)
print(searched_result)