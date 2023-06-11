#!/usr/bin/python3

''' Demonstration of python inheritance.
    class MyList inherits list.
'''


class MyList(list):
    ''' Prints the list in sorted ascending order.
    '''
    def print_sorted(self):
        print(sorted(self))
