#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a new rectangle."""
    def __init__(self, width=0, height=0):
        """Inialize a new rectangle.


        Args:
            width (int): The width of a rectangle
            height (int): The height of a rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Calculate the perimeter of a rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representaion of a rectangle."""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += "#" * self.width + "\n"

        return rectangle_str
