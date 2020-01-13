#!/usr/bin/python3
"""
File containing the print square method.
size is the size of the square
"""

def print_square(size):
    """ 'print_square(size)' print a square on #
        size is the size of the square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
