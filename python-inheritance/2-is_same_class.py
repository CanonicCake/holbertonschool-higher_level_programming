#!/usr/bin/python3
""" Returns True if the object is exactly and instance of a specified class,
returns False otherwise"""


def is_same_class(obj, a_class):
    """Finds if the same class"""
    if type(obj) == a_class:
        return True
    return False
