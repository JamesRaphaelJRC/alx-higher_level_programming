#!/usr/bin/python3
''' Defines a function read_file.'''


def read_file(filename=""):
    ''' Reads a textfile (UTF8) and prints it to stdout.'''
    if type(filename) is str:
        with open(filename, 'r', encoding="UTF-8") as f:
            print(f.read(), end='', end='')
