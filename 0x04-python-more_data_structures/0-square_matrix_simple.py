#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        new_matrix = []
        new_matrix = [[x * x for x in mat] for mat in matrix]
        return(new_matrix)
