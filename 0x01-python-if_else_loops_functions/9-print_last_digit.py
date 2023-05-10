#!/usr/bin/python3

def print_last_digit(number):
    abs_value = number * -1 if number < 0 else number
    unsigned_number = abs_value % 10
    print(unsigned_number, end="")
    return unsigned_number
