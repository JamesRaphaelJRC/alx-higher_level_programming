#!/usr/bin/python3

''' Defines a class 'Square' '''


class Square:

    ''' Initialize Square with a private instance int 'size' '''

    def __init__(self, size=0):
        self.__size = size

    ''' retrives value of size '''
    @property
    def size(self):
        return (self.__size)

    ''' sets the value of size '''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    ''' Returns the area of the square '''
    def area(self):
        return (self.__size ** 2)
