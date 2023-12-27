#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        my_list.sort()
        my_biggest_num = my_list[-1]
        return my_biggest_num
