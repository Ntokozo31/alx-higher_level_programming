#!/usr/bin/python3

"""Define a class Square"""

class Square:

    def __init__(self, size):

        self.__size = size

    def size(self):

        return self.__size

    def size(self, value):

        self.__size = value
