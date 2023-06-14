#!/usr/bin/python3
''' Defines a class, Student.'''


class Student:
    ''' Represents a class, Student.'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrives a dictionary representation of a Student instance.
            If attrs is a list of strings, only attribute names contained in
            the list must be retrived otherwise, all attributes must be
            retrived.
            It filters which dictionary representation to be retrived
        '''
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        
