#!/usr/bin/python3
import math
""" MagicClass!"""


class MagicClass:
    """ Magic Class! """
    def __init(self, radius=0):
        """ init """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ return area """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ return circumfrence """
        return ((2 * math.pi) * self.__radius)
