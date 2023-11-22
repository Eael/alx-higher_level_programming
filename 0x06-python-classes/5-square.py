#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square
        """
        self.size = size

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the # character"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")







