#!/usr/bin/python3


class Square:
    """A class Square initilized with size"""
    pass

    def __init__(self, size=0):
        """__init__

        The __init__ method to initilize a class Square.

        Args:
            size (int) = The size of the class Square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >+ 0")
        self.__size = size

    def area(self):
        return (self.size * self.size)
