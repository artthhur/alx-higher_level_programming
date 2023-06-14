#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_element = element ** 2
            squared_row.append(squared_element)
        squared_matrix.append(squared_row)
    return squared_matrix
