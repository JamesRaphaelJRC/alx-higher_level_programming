#!/usr/bin/python3
''' Defines a function, load_from_json_file.'''
import json


def load_from_json_file(filename):
    ''' Creates an object from a JSON file.'''
    with open(filename, 'r', encoding="UTF-8") as jFile:
        return (json.load(jFile))
