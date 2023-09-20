#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for length in matrix:
        new_l = []
        for collum in length:
            new_l.append(collum ** 2)
        new_matrix.append(new_l)
    return new_matrix
