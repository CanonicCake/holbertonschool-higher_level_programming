#!/usr/bin/python3
"""Class that defines a square."""


class Square:
    """
    Initilize Class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ method of class Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >+ 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Grab position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(elem, int) for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(elem >= 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """The area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout"""
        if self.__size == 0:
            print()
            return
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
