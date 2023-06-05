#!/usr/bin/python3

''' Defines a class 'Rectangle'.'''


class Rectangle:
    ''' Represents a rectangle.'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        ''' Initializes a new object of class Rectangle.
            Increases the number_of_instances by 1 at each instantiation.
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        ''' Return the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Returns the bigget ractangle base on the area.'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        ''' Return the printable representation of the Rectangle.
            The rectangle is represented with the content of 'print_symbol'.
        '''

        if self.__width == 0 or self.__height == 0:
            return ("")

        form = []

        for i in range(self.__height):
            form.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                form.append('\n')
        return ("".join(form))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)

    def __del__(self):
        ''' Prints a message anything a Rectangle is deleted.
            Reduces number_of_instances by 1 whenever an instance is deleted
        '''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
