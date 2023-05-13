#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if isinstance(matrix, list):
        transposed = []
        for row in matrix:
            transpose_row = []
            for i in range(len(row)):
                transpose_row.append(row[i])
            transposed.append(transpose_row)

        for row in transposed:
            for i in row:
                print("{:d}".format(i), end=" ")
            print()
