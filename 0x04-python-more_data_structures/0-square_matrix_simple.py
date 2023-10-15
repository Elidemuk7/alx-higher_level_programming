#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square of integers in a matrix"""

    new_mat = []

    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_mat.append(new_row)

    return new_mat
