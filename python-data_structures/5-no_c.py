#!/bin/usr/python3
def no_c(my_string):
    """Remove all c and C from list"""
    str = ''
    for i in my_string:
        if i != 'C' and i != 'c':
            str += i
    return str
