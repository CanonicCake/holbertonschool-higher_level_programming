#!/usr/bin/python3
"""Public instance of area and self for base geometry"""


class BaseGeometry:
    """Defines a base class geometry"""

    def __init__(self, width, height):
        """Initilizes self width and height"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
