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
            for i, num in enumerate(row):
                print("{:d}".format(num), end="")
                if i != len(row) - 1:
                    print(" ", end="")
            print()
