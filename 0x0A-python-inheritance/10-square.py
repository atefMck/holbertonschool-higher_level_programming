#!/usr/bin/python3
"""
This module add a new square class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
	"""
	This a subclass from rectangle object
	"""
    def __init__(self, size):
    	"""
		This is the initialisation method for the square class
		"""
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
    	"""
		This method returns the area of a square
		"""
        return (self.__size ** 2)

    def __str__(self):
    	"""
		This method returns a formatted string when the class gets printed
		"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
