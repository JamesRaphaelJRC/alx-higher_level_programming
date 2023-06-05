#!/usr/bin/python3

''' Defines a function that prints a statement. '''


def say_my_name(first_name, last_name=""):
    '''
        Prints My name is <first name> <last name>

        Arguments:
                First_name and last_name must be strings
        Raises:
                TypeError if first_name and/or last_name is not a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
