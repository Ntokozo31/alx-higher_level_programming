#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size

        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except ValueError:
            print("size must be an integer")
    def area(self):
        return self.__size * self.__size
