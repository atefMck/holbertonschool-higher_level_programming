#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    new_matrix = [[0 for x in range(len(matrix))] for y in range(len(matrix[i]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return(new_matrix)
