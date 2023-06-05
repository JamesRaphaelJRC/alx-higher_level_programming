#!/usr/bin/python3

''' Defines a square printing function. '''


def print_square(size):
    ''' Prints square with the character '#'
        
        Arguments:
                    size: The size length of the square to be printed.
        Conditions:
                    size must be an integer
                    size must be >= 0
        Raises:
                    TypeError if size is not an integer
                    ValueError if size < 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
