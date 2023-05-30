#!/usr/bin/python3

'''
    Ddivides 2 integers and prints the result.

    Return: The value of the division otherwise none
'''


def safe_print_division(a, b):
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))

    return (quotient)
