#!/usr/bin/python3

"""Defines a class Square."""


class Square:

    """Represent a square.

    This class provide a blueprint for creating square objects.

    Attribute:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """Constructor that initializes a private attribute."""
        self.__size = size
