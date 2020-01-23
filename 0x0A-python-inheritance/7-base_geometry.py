#!/usr/bin/python3
"""
Module adding a new class
"""

class BaseGeometry:
    def area(self):
        """
                Method that checks if class has area implemented
                """
        if hasattr(self, 'area'):
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
                Method checking if value is an integer and > 0
                """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
