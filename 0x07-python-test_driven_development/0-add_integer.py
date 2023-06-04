#!/usr/bin/python3

''' Defines a function that add integers '''


def add_integer(a, b=98):
    ''' Returns a and b integer additions
        
        float arguments are typecasted to int before addition is performed

        Raises:
                TypeError if a and/or b is not an integer or a float
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
