#!/usr/bin/python3
"""Public instance of area and self for base geometry"""


class BaseGeometry:
    """Defines a base class geometry"""

    def area(self):
        """Defines the area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer Validation that raises value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        """Initilizes self width and height

        Augs:
        height: height of class
        width: width of class
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
