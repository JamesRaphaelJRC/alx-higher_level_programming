#!/usr/bin/python3
''' Defines a class, Square that inherits from another class Rectangle.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Represents class Square.'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initialize an instance of class Sqaure.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Returns the str() representation of Sqaure.'''
        string = "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                               str(self.id), str(self.x),
                                               str(self.y), str(self.width))
        return string

    @property
    def size(self):
        ''' Gets/sets the current value for the size of the square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' Updates the class Square by re-arranging the order of the arguments
            
            Re-arrangement style:
                1st argument will be the id attribute
                2nd argument will be the size attribute
                3rd argument will be the x attribute
                4th argument will be the y attribute

            Condition:
                **kwargs must be skipped if *args exists and is not empty
        '''
        if args and len(args) != 0:
            arg_size = len(args)

            if arg_size >= 1:
                if args[0] is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = args[0]
            if arg_size >= 2:
                self.size = args[1]
            if arg_size >= 3:
                self.x = args[2]
            if arg_size >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        ''' Returns a dictionary reppresentation of  Sqaure.'''
        dict_rep = dict([('id', self.id), ('x', self.x), ('size', self.size),
                         ('y', self.y)])
        return dict_rep
