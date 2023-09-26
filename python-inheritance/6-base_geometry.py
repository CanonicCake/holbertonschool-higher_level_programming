#!/usr/bin/python3
"""Public instance of area and self for base geometry"""


class BaseGeometry:
    """Defines a base class geometry"""

    def area(self):
        """Defines the area of geometry"""
        raise Exception("area() is not implemented")
