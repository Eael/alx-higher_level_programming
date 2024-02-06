#!/usr/bin/python3
"""A lookup function to return list of available methods and attributes"""


def lookup(obj):
    """returns the list of available attributes and methods of an object
    Args:
        obj (class): a class object
    Returns:
        list of attributes and methods of obj
    """
    return (dir(obj))
