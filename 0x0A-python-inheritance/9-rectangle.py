#!/usr/bin/python3
''' Defines a class Rectangle.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Represents a class Rectangle.'''
    def __init__(self, width, height):
        super().integer_validator('width', width)
        self.__width = width
        super().integer_validator('height', height)
        self.__height = height

    def area(self):
        ''' Returns the area of the rectangle.'''
        return (self.__width * self.__height)

    def __str__(self):
        ''' Returns the str() and print() representation of the Rectangle'''
        str_rep = "[" + str(self.__class__.__name__) + "] "
        str_rep += str(self.__width) + "/" + str(self.__height)
        return (str_rep)
