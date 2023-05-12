#!/usr/bin/python3
"""
    element_at - Retrieves an element from a list at a given index
    my_list: The list containing the element to be retrieved.
    idx: The index whose element is to be retrieved.

    Return: None if idx is negative or out of range
            The element at idx otherwise
"""


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return("None")
    return(my_list[idx])
