#!/usr/bin/python3
"""Creates a rectangle that is a square based on base geometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle that is a class square"""
    def __init__(self, size):
        """Initilizes a squares size"""
        self.integer_validation("size", size)
        self.__size = size
        super().__init__(size, size)

    