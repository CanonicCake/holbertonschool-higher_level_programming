#!/usr/bin/python3


class Square:
    """A class Square initilized with size"""

    def __init__(self, size=0):
        """__init__

        The __init__ method to initilize a class Square.

        Args:
            size (int) = The size of the class Square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """
            Return the current area of the class Square
            """
            return (self.__size * self.__size)
