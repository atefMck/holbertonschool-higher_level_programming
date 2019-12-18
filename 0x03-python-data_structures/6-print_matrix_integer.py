#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for j in range(len(list)):
            if j == len(list) - 1:
                print("{:d}".format(list[j]), end="")
            else:
                print("{:d} ".format(list[j]), end="")
        print()
