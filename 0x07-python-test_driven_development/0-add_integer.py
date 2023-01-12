#!/usr/bin/python3

"""Module for 0-add_integer.It contains the function add_integer
which adds two integers and returns their sum
"""


def add_integer(a, b=98):
    """returns the sum of two integers
    Args:
        a = the first integer
        b = the second integer
    Return:
        The sum of a and b
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a and b must be integers or floats")
    a, b = int(a), int(b)
    return a + b
