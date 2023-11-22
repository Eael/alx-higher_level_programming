#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square
        """
        self.__size = size

    def area(self):
        """Return current area of square
        which is size * size"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns/Gets current size"""
        return (self.__size)

    @sizesetter
    def size(self, value):
        """Sets value for size

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
