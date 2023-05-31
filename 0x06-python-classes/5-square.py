#!/usr/bin/python3

''' Defines a class 'Square' '''


class Square:
    ''' Initializes Square with a private instance int 'size' '''

    def __init__(self, size):
        self.__size = size

    ''' Get/set the current size of square '''
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    ''' Returns the area of te square '''
    def area(self):
        return (self.__size ** 2)

    ''' that prints in stdout the square with the character # '''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
