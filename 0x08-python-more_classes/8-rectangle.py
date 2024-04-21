#!/usr/bin/python3

"""Define class Rectangle."""


class Rectangle:
    """Represent a new rectangle.
    Attributes:
        number_of_instances (int): The number of rectangle instances.
        print_symbol (any): The symbol used for string represantation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.


        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self. height = height

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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the width of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculate the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Return a printable represatation of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return a string represatation of rectangle."""
        rect = "Rectangle (" + str(self.__width)
        rect += "," + str(self.__heigth) + ")"
        return (rect)

    def __del__(self):
        """Print a massege for every delation of rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
