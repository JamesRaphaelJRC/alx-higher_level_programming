#!/usr/bin/python3

''' Defines a matrix dividing function '''


def matrix_divided(matrix, div):
    ''' Returns a new matrix that contains the elements of the original matrix
        divided by 'div'

        Conditions:
                a. matrix must be a list of integers and/or floats
                b. Each row of the matrix must be of the same size
                c. div must be a number and must not be equal to 0
                d. All elements ofmatrix should be divided by div and
                        rounded to 2 decimal places
        Raises:
                TypeError if conditions a, b and c are not met
                ZeroDivisionError if div == 0
    '''
    for row in matrix:
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    i, j = 0, 1

    while i < len(matrix) - 1:
        if len(matrix[i]) != len(matrix[j]):
            raise TypeError("Each row of the matrix must have the same size")
        i += 1
        j += 1

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round((num / div), 2) for num in row] for row in matrix]
    return new
