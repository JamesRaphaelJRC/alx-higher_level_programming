#!/usr/bin/python3

''' A class 'Square' '''


class Square:
    ''' Initializes class Square with private instance attribute 'size' '''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
