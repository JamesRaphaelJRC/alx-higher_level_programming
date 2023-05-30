#!/usr/bin/python3

def safe_print_integer(value):

    try:
        print("{:d}".format(value))
        condition = True
    except (ValueError, TypeError):
        condition = False

    return (condition)
