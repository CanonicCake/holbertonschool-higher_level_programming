#!/usr/bin/python3
"""Defines a Class Square"""

class Square:
    """Initilize Class Square"""

    def __init__(self, size=0):
        """__init__ method of class Square"""
        self.size = size

    @property
    def size(self):
        """Property of Self"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >+ 0")
        self.__size = size

    def area(self):
        """Area of Class Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints class Square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
