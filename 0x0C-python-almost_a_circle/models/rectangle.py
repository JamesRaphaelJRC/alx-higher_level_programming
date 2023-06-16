#!/usr/bin/python3
''' Defines a class, Rectangle that inherits from class Base.'''
from models.base import Base


class Rectangle(Base):
    ''' Represents the class Rectangle.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initializes each instance of Rectangle.'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
        super().__init__(id)

    @property
    def width(self):
        ''' Get/set the current value of width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        ''' Gets/sets the current value of height.'''
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        ''' Gets/sets the current value of x.'''
        return (self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        ''' Gets/sets the current value of y.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
