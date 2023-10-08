#!/usr/bin/python3
"""Rectangle based class"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Properties of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width"""
        if type(width) is not int:
            raise TypeError("width is not an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

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

    def display(self):
        """public display"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        """string method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assining an argument
        Args:
        *args - List of Arguments
        **kwargs - a dictionary of key-values
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
