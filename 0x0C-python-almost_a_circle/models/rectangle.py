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

    def update(self, *args, **kwargs):
        ''' Updates class Rectangle by re-arranging the order of its arguments

            Order of re-arrangement:
                1st argument will be the id attribute
                2nd argument will be the width attribute
                3rd argument will be the height attribute
                4th argument will be the x attribute
                5th argument will be the y attribute
        '''
        if args and len(args) != 0:
            if len(args) != 0:
                arg_count = len(args)

                if arg_count >= 1:
                    if args[0] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[0]
                if arg_count >= 2:
                    self.width = args[1]
                if arg_count >= 3:
                    self.height = args[2]
                if arg_count >= 4:
                    self.x = args[3]
                if arg_count >= 5:
                    self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
