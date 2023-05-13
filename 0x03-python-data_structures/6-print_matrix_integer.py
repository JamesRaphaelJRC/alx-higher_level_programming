#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        transposed = []
        for row in matrix:
            transpose_row = []
            for i in range(len(row)):
                transpose_row.append(str(row[i]))
            transposed.append(' '.join(transpose_row))
        print('\n'.join(transposed))
