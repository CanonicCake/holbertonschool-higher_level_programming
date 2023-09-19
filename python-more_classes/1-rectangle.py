#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Initialization of properties

        Args:
        width: width must be an integer
        height: height must be an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get Properties of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
