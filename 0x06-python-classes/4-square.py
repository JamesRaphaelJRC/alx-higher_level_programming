#!/usr/bin/python3

''' Defines a class 'Square' '''


class Square:

    ''' Initialize Square with a private instance int 'size' '''

    def __init__(self, size=0):


        self.__size = size

    @property
    ''' retrives value of size '''
    def size(self):
        return (self.__size)
    
    @size.setter
    ''' sets the value of size '''
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    ''' Returns the area of the square '''
    def area(self):
        return (self.__size ** 2)
