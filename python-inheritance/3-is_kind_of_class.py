#!/usr/bin/python3
""" Returns True if the object is an instance of, or if the obkect is an
instance of a class that inherited from the specified class, return False
otherwise"""


def is_kind_of_class(obj, a_class):
    """Is an instance of obj and a_class"""
    return isinstance(obj, a_class)
