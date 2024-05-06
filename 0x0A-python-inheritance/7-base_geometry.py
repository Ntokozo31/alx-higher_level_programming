#!/usr/bin/python3


"""Define a new class."""


class BaseGeometry:
    """Base class representing geometric entities."""

    def area(self):
        """
        Calculate the area of base geometric

        Raise:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validation of name and value

        Args:
            name(str): The name being validated
            value(int): The value being validated

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
