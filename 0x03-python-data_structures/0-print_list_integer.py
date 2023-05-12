#!/usr/bin/python3
"""
    print_list_integer: Prints all integers of a list.
    my_list: The list to be printed
"""


def print_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("Empty list")
    else:
        for num in my_list:
            print("{:d}".format(num))
