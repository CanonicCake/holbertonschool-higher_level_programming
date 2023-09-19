#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a Square."""
    pass
    __size = None

    def __init__(self, size=0):
        """ Initilizes size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the class Square"""
        return (self.__size * self.__size)
