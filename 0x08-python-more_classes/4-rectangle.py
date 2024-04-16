#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a new class"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of a rectangle.
            heigth (int): The height of a rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of a rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: width must be an integer.
            ValueErro: width must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of a rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of a rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: height must be an integer.
            ValueError: height must be >= 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """Calculate the perimeter of rectangle."""
        if width == 0 or height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Return string represatation of a ractangle."""
        if self.width == 0 or self.height == 0:
            return ""

        raw = "#" * self.width
        rectangle_str = "\n".join([raw] * self.height)
        return rectangle_str

    def __repr__(self):
        """Return string represantation of rectangle."""
        return f"Rectangle ({self.width}, {self.height})"
