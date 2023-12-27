#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for new_list in my_list:
        if new_list % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
