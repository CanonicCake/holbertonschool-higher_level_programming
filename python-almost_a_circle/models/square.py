#!/usr/bin/python3
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
        """Set the value of size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates and asignes attributes"""
        if args:
            args_dec = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, args_dec[i], arg)
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
