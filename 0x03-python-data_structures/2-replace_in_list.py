#!/usr/bin/python3
"""
    replace_in_list - Replaces an element of a list at a specific position.
    my_list: A list containing elements
    idx: The index/position to be replaced by the new element
    element: The new element

    return: The newly edited list on sucess
            The original list when idx < 0 or idx > number of elements
            in the list
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
