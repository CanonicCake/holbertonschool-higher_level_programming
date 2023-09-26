#!/usr/bin/python3
"""Return true if object is inhereted, False otherwise"""


def inherits_from(obj, a_class):
    """Inherits from an instance of object and a_class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
