#!/usr/bin/python3
''' Defines a class Rectangle.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rectangle inherits the properties of the parent base class
        BaseGeometry.
    '''
    def __init__(self, width, height):
        ''' Instantiation with width and height.'''
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
