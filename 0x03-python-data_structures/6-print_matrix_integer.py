#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if j == len(matrix) - 1:
                    print("{:d}".format(matrix[i][j]), end = "")
                else:
                    print("{:d} ".format(matrix[i][j]), end = "")
            print()
    else:
        print()
