#!/usr/bin/python3
"""Creates a rectangle that is a square based on base geometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle that is a class square"""

    def __init__(self, size):
        """Initilizes a squares size"""
        super().__init__(size, size)

        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Area of square"""
        return self.__size * self.__size
