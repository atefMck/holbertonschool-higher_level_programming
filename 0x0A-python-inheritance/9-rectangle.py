#!/usr/bin/python3
"""
Module adding an improved version of Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
	"""
	The new improved Rectangle class
	"""
    def __init__(self, width, height):
    	"""
		The init method of Rectangle class
		"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
    	"""
		Method that returns area of a Rectangle
		"""
        return (self.__height * self.__width)

    def __str__(self):
    	"""
		Method that returns a better formatted string when printing the class
		"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
