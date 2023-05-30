#!/usr/bin/python3

''' Defines a class 'Square' '''


class Square:

    ''' Initialize square with a private instance int 'size'
        size must be >= 0
    '''

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    ''' Returns the current square area '''

    def area(self):
        return (self.__size ** 2)
