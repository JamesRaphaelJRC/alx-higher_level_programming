#!/usr/bin/python3
def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        ''' Adds all the unique numbers in a list "my_list"'''
        res = 0
        set_list = set(my_list)
        for num in set_list:
           res += num
        return(res)
