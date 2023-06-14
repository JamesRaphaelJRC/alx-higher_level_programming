#!/usr/bin/python3
''' Defines a function, from_json_string.'''
import json


def from_json_string(my_str):
    ''' Returns an object (python data structure) represented by a JSON string.
    '''
    return (json.load(my_str))
