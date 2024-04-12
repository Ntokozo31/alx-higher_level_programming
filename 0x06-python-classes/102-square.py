#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square with a given size.

        Args:
            size (int): The size of the square (default is 0)
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.__size

    @size.setter
    """Set the size of the square."""
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return (self.size * self.size)

    def __eq__(self, other):
        """Check if two squares are equl."""
        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal."""
        return not self == other

    def __gt__(self, other):
        """Check if one square is greater than the other"""
        if not isinstance(other, Square):
            raise TypeError("cannot compere Square with non-Square object")
        return self.area() > other.area()

    def __lt__(self, other):
        """Check if one square is less than the other."""
        if not isinstance(other, Square):
            raise TypeError("cannot compere Square with non-Square object")
        return self.area() < other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to the other."""
        if not isinstance(other, Square):
            raise TypeError("cannot compere Square with non-Square object")
        return self.area() >= other.area()

    def __le__(self, other):
        """Check if one square is less than or equal to the other."""
        if not isinstance(other, Square):
            raise TypeError("cannot compere Square with non-Square object")
        return self.area() <= other.area()
