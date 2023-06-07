#!/usr/bin/python3
''' Unittest for max_integer([..])
'''

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' Defines unittest for the function 'max_integer' '''

    def test_ordered_list(self):
        ''' tests max_integer when list is arranged in order of magnitude.'''
        ordered_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer(ordered_list), 10)

    def test_unordered_list(self):
        ''' tests max_integer when list is unsorted.'''
        result = max_integer([2, 0, 3, 1, 88, 23, 9, 9])
        self.assertEqual(result, 88)

    def test_float_list(self):
        ''' tests max_integer when list contains floats '''
        _max = max_integer([0.0, 2.3, 20.1, 99.99, 99.98, 20])
        self.assertEqual(_max, 99.99)

    def test_one_element_list(self):
        ''' Tests max_integer when list contains only one element.'''
        _max = max_integer([8])
        self.assertEqual(_max, 8)

    def test_empty_list(self):
        ''' tests max_integer when list is empty.'''
        _max = max_integer([])
        _max_1 = max_integer()
        self.assertEqual(_max, None)
        self.assertEqual(_max_1, None)

    def test_negative_list(self):
        ''' tests max_integer when list contains negative numbers.'''
        _max = max_integer([-1.05, -2, -101, -1.1, -419])
        self.assertEqual(_max, -1.05)

    def test_exponential(self):
        ''' tests max_integer when list contains exponentials. '''
        _max = max_integer([10e1, 1e1, 1e2, 10e10])
        self.assertAlmostEqual(_max, 100000000000.0)

    def test_characters(self):
        ''' tests max_integer when list contains single letters.'''
        _max = max_integer(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(_max, 'e')

    def test_word(self):
        ''' tests max_integer when the argument is a string.'''
        _max = max_integer("James")
        self.assertEqual(_max, 's')

    def test_words(self):
        ''' tests max_integer when list contains different strings.'''
        _max = max_integer(['James', 'Bond', 'Raph', 'King'])
        self.assertEqual(_max, 'Raph')

    def test_boolean(self):
        ''' tests max_integer when argument is a boolean.'''
        self.assertRaises(TypeError, max_integer, True)


if __name__ == '__main__':
    unittest.main()
