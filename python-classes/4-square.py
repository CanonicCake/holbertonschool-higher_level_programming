#!/usr/bin/python3
"""Defines a class square."""

class Square:
    """
    Initilize Class Square
    """

    def __init__(self, size=0):
        """
        __init__ method of class Square
        """
        self.size = size

    @property
    def size(self):
        """Properties of self"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >+ 0")
        self.__size = size

    def area(self):
        """Defines the area"""
        return (self.__size * self.__size)
