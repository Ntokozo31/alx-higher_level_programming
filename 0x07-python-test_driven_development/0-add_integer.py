#!/usr/bin/python3

def add_integer(a, b=98):
    """
    adds two integers.

    Parameters:
    a (int or float): The first number
    b (int or float, optional): The second number (Default to 98).

    Returns:
    int: The sum of a and b, converted to integer

    Raise:
    TypeError: If a or b is not an integer or float.
               Error message specifies wheather 'a' or 'b' must be an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
