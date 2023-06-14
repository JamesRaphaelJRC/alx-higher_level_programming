#!/usr/bin/python3
''' Defines a class Student'''


class Student:
    ''' Represents the class Student.'''
    def__init__(self, first_name, last_name, age):
        ''' Instantation'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrives the dictionary presentation of a Student instance
            if attrs is a list of strings, only attributes contained in this
            string will be retrived otherwise, all attributes are retrived.
        '''
        if attrs and isinstance(attrs, list):
            return {at: getattr(self, at) for at in attrs if hasattr(self, at)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        ''' Replaces all attributes of the Student instance.
            This assumes that json will always be a dictionary.
            A dictionary key wll be the public attribute name
            A dictionary value will be the value of the public attribute.
        '''
        for key, value in json.items():
            setattr(self, key, value)
