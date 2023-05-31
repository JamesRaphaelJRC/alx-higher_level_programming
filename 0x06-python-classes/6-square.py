#!/usr/bin/python3

''' Defines a class "Square' '''


class Square:
    ''' Initialize Square with a private instance size and
        position (a turple)
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    ''' Get/set current size and position of Square object '''
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) > 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    ''' returns the current square area '''
    def area(self):
        return (self.__size ** 2)

    ''' Prints in stdout the square with the character # '''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                j = 0
                while j < self.__position[0]:
                    print(" ", end='')
                    j += 1
                print("#" * self.__size)
