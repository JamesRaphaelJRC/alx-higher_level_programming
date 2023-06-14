#!/usr/bin/python3
''' Defines a function, class_to_json.'''


def class_to_json(obj):
    ''' Returns the dictionary description with simple data structuire
        (list, dictionary, string, integer and boolean) for JSON serialization
        of an object.
    '''
    return obj.__dict__
