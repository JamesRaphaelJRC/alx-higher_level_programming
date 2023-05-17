#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ''' Returns a new dictiionary with all values multiplied by 2
    Long format:
     new_dictionary = {}
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
    '''
    return({k: a_dictionary[k] * 2 for k in a_dictionary})
