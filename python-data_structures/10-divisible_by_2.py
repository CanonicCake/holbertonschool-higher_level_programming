#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_l = []
    for i in my_list:
        if i % 2 == 0:
            my_l.append(True)
        else:
            my_l.append(False)
    return my_l
