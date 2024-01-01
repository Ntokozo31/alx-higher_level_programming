#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_new_matrix = []
    for raw in matrix:
        squared_raw = list(map(lambda x: x ** 2, raw))
        my_new_matrix.append(squared_raw)
    return my_new_matrix
