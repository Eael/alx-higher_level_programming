#!/usr/bin/python3
""" A fucntion to find similarities in class"""


def is_same_class(obj, a_class):
    """Compares to see if obj is an instance of a_class
    Args:
        obj :
        a_class: A random class

    Returns:
        True if isinstance or False if not
    """
    if type(obj) == (a_class):
        return True
    else:
        return False
