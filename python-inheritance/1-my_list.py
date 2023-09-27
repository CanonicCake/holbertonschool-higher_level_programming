#!/usr/bin/python3
""" My List class that inherits sorted self"""


class MyList:
    """ Defines MyList class"""

    def __init__(self):
        """Initilize self"""
        super().__init__()

    def print_sorted(self):
        """ Prints a sorted list from self"""
        sorted_list = sorted(self)
        return sorted(self)
