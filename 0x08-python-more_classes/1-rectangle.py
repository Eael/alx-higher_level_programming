#!/usr/bin/python3

"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

            Args:
                width (int): The width of the rectangle
                height (int): The height of the rectangle

            Raises:
                TypeError when height or width isn't an integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width


    @width.setter
    def width(self, value):
        """Sets width of the rectangle
            Args:
                  value (int): value for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    
    @property
    def height(self):
        """Get height of the rectangle"""
        return self.__height

    
    @height.setter
    def height(self, value):
        """Sets height of the rectangle
            Args:
                value (int): value for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
