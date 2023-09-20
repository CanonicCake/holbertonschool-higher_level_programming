#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    my_l = min(my_list)
    for i in my_list:
        if my_l < i:
            my_l = i
    return my_l
