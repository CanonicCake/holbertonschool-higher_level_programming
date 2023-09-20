#!/bin/usr/python3
def no_c(my_string):
    """Remove all c and C from list"""
    new_str = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            new_str += i
    return new_str
