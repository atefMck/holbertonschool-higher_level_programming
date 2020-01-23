#!/usr/bin/python3
"""
This module add a new list class
"""


class MyList(list):
    """
    A subclass from list object
    """
    def print_sorted(self):
        """ This method prints the list sorted """
        print(sorted(self))

    def __str__(self):
        """ returns the list """
        return (str(list(self)))
