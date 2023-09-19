#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """ Print a replacement of an element"""

    if idx < 0 or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)
