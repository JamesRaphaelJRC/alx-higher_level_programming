#!/usr/bin/python3

''' Defines a function that returns the attributes of an object.'''


def lookup(obj):
    ''' Returns the list of available attributes and methods of an object
        obj: The object
    '''
    return (dir(obj))
