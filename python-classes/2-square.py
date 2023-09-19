#!/usr/bin/python3
"""A Square Class

A Square Class

"""


class Square:
    """A class Square initilized with size"""
    pass

    def __init__(self, size=0):
        """__init__

        The __init__ method of class Square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
