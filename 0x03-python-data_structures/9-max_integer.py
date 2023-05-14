#!/usr/bin/python3
'''
    max_integer - Finds the biggest integer in a list
    my_list - The list

    Return: None if list is empty and biggest int if not empty.
'''


def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return(None)

        maximum = my_list[0]
        for integer in my_list:
            if integer > maximum:
                maximum = integer
        return(maximum)
