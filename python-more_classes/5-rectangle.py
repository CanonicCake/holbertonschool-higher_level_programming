#!/usr/bin/python3
"""Defines a Rectangle class"""


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

    def area(self):
        """Area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Defines the parameter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Returns a string that represents the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += "#"
            rect_str += "\n"
        return rect_str[:-1]

    def __print__(self):
        """prints to the stdout to the console"""
        print(self)

    def __repr__(self):
        """Returns a string representation that uses eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message when a instance is deleted"""
        print("Bye rectangle...")
