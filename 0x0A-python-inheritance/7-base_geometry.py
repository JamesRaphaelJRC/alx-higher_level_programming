#!/usr/bin/python3

''' Defines a clas BaseGeometry.'''


class BaseGeometry():
    ''' Defines a method 'area'.'''
    def area(self):
        ''' Raises exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' A public instance method that validates the argument 'value'.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
