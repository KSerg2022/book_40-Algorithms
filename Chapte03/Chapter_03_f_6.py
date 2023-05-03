"""linear search"""

list_ = [12, 33, 55, 41, 7, 26, 17, 31, 20, 1]
print(list_)
print('\n1 -- ')


def linearsearch(list_, number):
    for i in range(len(list_) - 1):
        if list_[i] == number:
            return True
    return False

number = 31
searched_result = linearsearch(list_, number)
print(searched_result)

number = 100
searched_result = linearsearch(list_, number)
print(searched_result)
