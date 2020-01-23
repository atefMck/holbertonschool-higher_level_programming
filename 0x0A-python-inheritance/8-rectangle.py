#!/usr/bin/python3
"""
Module adding a subclass Rectangle of BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The new Rectangle Class
    """
    def __init__(self, width, height):
        """
        The init method of Rectangle class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
