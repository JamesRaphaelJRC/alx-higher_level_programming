#!/usr/bin/python3
"""
    print_list_integer: Prints all integers of a list.
    my_list: The list to be printed
"""


def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num))
