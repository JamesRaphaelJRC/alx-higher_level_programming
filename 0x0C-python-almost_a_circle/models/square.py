#!/usr/bin/python3
''' Defines a class, Square that inherits from another class Rectangle.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Represents class Square.'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initialize an instance of class Sqaure.'''
        super().__init__(id, x, y, size, size)

