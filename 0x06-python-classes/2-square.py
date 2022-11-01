#!/usr/bin/python3
"""Write a class that defines a square with
    private instance attribute size that must be
    an integer, otherwise raise a TypeErroe exception
    and if size < 0, raise a ValueError exception"""


class Square:
    """Represent a square"""


    def __init__(self, size=0):
        self.__size = size

        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
