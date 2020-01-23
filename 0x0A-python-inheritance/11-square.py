#!/usr/bin/python3
"""
This module adds a Squre subclass of Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is the new Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        This is the Squre class init method
        """
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        """
        This method returns the area of a Square object
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        This method returns a better fromatted string when printing the object
        """
        return ("[Square] {}/{}".format(self.__width, self.__height))
