#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        self.size = size
    

    @property
    def size(self):
        """
        Retrieves the size of the square.

        
        Return:
            int: The size of the square
        """
        return self.__size


    @size.setter
    def size(self, value):
        """
        sets the size of the square


        Args:
            value (int): The size of the square


        Return:
            TypeValue: if value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    

    def area(self):
        """
        Compute the area of the square.


        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
