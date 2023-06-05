#!/usr/bin/python3

''' Unittest for max_integer([..])
'''

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    ''' Defines unittest for the function 'max_integer' '''

    def Test_ordered_list(self):
        ''' Tests max_integer when list is arranged in order of magnitude.'''
        ordered_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer(ordered_list), 10)

    def Test_unordered_list(self):
        ''' Tests max_integer when list is unsorted.'''
        result = max_integer([2, 0, 3, 1, 88, 23, 9, 9])
        self.assertEqual(result, 88)

    def Test_float_list(self):
        ''' Tests max_integer when list contains floats '''
        _max = max_integer([0.0, 2.3, 20.1, 99.99, 99.98, 20])
        self.assertEqual(_max, 99.99)

    def Test_empty_list(self):
        ''' Tests max_integer when list is empty.'''
        _max = max_integer([])
        _max_1 = max_integer()
        self.assertEqual(_max, None)
        self.assertEqual(_max_1, None)

    def Test_negative_list(self):
        ''' Tests max_integer when list contains negative numbers.'''
        _max = max_integer([-1.05, -2, -101, -1.1, -419])
        self.assertEqual(_max, -1.05)

    def Test_exponential(self):
        ''' Tests max_integer when list contains exponentials. '''
        _max = max_integer([10e1, 1e1, 1e2, 10e10])
        self.assertAlmostEqual(_max, 100000000000.0)

    def Test_characters(self):
        ''' Tests max_integer when list contains single letters.'''
        _max = max_integer(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(_max, 'e')

    def Test_word(self):
        ''' Tests max_integer when the argument is a string.'''
        _max = max_integer("James")
        self.assertEqual(_max, 's')

    def Test_words(self):
        ''' Tests max_integer when list contains different strings.'''
        _max = max_integer(['James', 'Bond', 'Raph', 'King'])
        self.assertEqual(_max, 'Raph')

    def Test_boolean(self):
        ''' Tests max_integer when argument is a boolean.'''
        _max = max_integer(True)
        self.assertRaise(TypeError, _max)


if __name__ == '__main__':
    unittest.main()
