#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent class rectangle.
    Attribute:
        number_of_instance (int): The number of rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize new class rectangle.


        Args:
            width (int): The width of a new rectangle.
            height (int): The height of a new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= integer")
        self.__width = value

    @property
    def height(self):
        """Get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get the height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of rectangle."""
        return (2 * (self.__width * self.__height))

    def perimeter(self):
        """Calculate the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0

    def __str__(self):
        """Return the printable of represantation of rectangle.
        Represent the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
        if i != self.__height - 1:
            rect.append("\n")
        return "".join(rect)

    def __repre__(self):
        """Return the string represantation of the rectangle."""
        rect = "Rectangle (" + str(self.__width)
        retct += "," + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print massege of every deletation of rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
