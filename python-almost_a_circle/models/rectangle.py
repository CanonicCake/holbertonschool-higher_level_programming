#!/usr/bin/python3
"""Rectangle based class"""
import json


class Rectangle:
    """Defines a Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Property of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Properties of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Properties of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setting y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of rectangle"""
        return self.height * self.width
