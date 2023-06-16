#!/usr/bin/python3
''' Defines a class, Rectangle that inherits from class Base.'''
from models.base import Base


class Rectangle(Base):
    ''' Represents the class Rectangle.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initializes each instance of Rectangle.

            where:
                width = The width of the new Rectangle
                height = The height of the new Rectangle
                x = The x coordinate of the new Rectangle
                y = The y coordinate of the new Rectangle
                id = The identity of the new Rectangle
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' Get/set the current value of width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' Gets/sets the current value of height.'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        ''' Gets/sets the current value of x.'''
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        ''' Gets/sets the current value of y.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        ''' Returns the area of the Rectangle instance '''
        return (self.__width * self.__height)

    def display(self):
        ''' Prints in stdout the Rectangle instance with the character '#'.'''
        [print("") for n in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for i in range(self.__width)]
            print("")

    def __str__(self):
        ''' Returns the str() representation of the Rectangle.'''
        string = '[' + type(self).__name__ + '] ' + '(' + str(self.id) + ')'
        string += str(self.__x) + '/' + str(self.__y) + ' - '
        string += str(self.__width) + '/' + str(self.__height)
        return string
