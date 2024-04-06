#!/usr/bin/python3
"""Define a class Square."""


class Square:
    def __init__(self, size=0):
        """
        Constructor for the Square class.

        Parameters:
            size (int) The size of the square (default is 0).
        """

        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except ValueError:
            print("size must be an integer")

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
