#!/usr/bin/python3
'''
    delete_at - deletes an item at a specific position (idx) in a list
'''


def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        if idx < 0 or idx >= len(my_list):
            return(my_list)

        del my_list[idx]
        return(my_list)
