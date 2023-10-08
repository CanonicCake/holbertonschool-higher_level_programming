#!/usr/bin/bash
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """The init class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Properties of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value
