#!/usr/bin/python3

''' Defines an instance checking function.'''


def is_same_class(obj, a_class):
    ''' eturns 'True' if the object is exactly an instance of the specified
        class otherwise 'False'

        obj: The object to be checked
        a_class: The class used for comparism
    '''
    return (issubclass(a_class))
