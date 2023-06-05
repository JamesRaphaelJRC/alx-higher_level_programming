#!/usr/bin/python3

''' Defines a class 'Rectangle'
'''


class Rectangle:
    ''' Represents a rectangle.'''
    def __init__(self, width=0, height=0):
        ''' Initializes a new object of class Rectangle.'''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Gets and sets the value of width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Gets and sets the value of height.'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Returns the area of the rectangle.'''
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
