#!/usr/bin/python3
""" Defines an integer addition function"""


def add_integer(a, b=98):
    """
        Return an integer from addition

        Floats are changed into integers

        Raise:
            TypeError: if a or b is not an integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
