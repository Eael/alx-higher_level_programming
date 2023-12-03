#!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """Represent a rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError when height or width isn't an integer
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """Get width of the rectangle"""
    def width(self):
        return self.__width

    @property
    """Get height of the rectangle"""
    def height(self):
        return self.__height

    @widthsetter
    """Sets width of the rectangle
        Args:
            value (int): value for width
    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @heightsetter
    """Sets height of the rectangle
        Args:
            value (int): value for width
    """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
