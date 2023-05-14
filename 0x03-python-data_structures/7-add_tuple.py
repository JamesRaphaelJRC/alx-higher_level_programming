#!/usr/bin/python3
'''
    add_tuple - Adds 2 tuples
    Returns a tuple with 2 integers:
    The first element is the addition of the first element of each
    argument
    The second element is the addition of the second element of each
    argument
'''


def add_tuple(tuple_a=(), tuple_b=()):
    if isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple):
        if len(tuple_a) < 2:
            if len(tuple_a) == 0:
                tuple_a = 0, 0
            else:
                tuple_a = tuple_a[0], 0
        if len(tuple_b) < 2:
            if len(tuple_b) == 0:
                tuple_b = 0, 0
            else:
                tuple_b = tuple_b[0], 0
        return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
