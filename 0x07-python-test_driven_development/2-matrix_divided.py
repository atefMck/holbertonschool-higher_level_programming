#!/usr/bin/python3
"""
File containing the add integer method.
a is the first integer
b is the second integer
"""

def matrix_divided(matrix, div):
    """ 'add_integer(a, b)' function that adds two integers/floats
        a is the first integer
        b is the second integer """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    error3 = "div must be a number"
    error4 = "division by zero"
    newMat = eval(repr(matrix))
    if type(matrix) is not list:
        raise TypeError(error1)
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(error1)
        if i != len(matrix) -1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError(error2)
        for elem in matrix[i]:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(error1)
    if type(div) is not int and type(div) is not float:
        raise TypeError(error3)
    if div == 0:
        raise ZeroDivisionError(error4)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMat[i][j] = round(matrix[i][j] / div, 2)
    return(newMat)
