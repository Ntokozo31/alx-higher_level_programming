#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    my_set = set(my_list)
    sum_result = 0
    for num in my_set:
        sum_result += num
    return sum_result

