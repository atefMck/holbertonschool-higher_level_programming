#!/usr/bin/python3
"""
This module add a new class
"""


class BaseGeometry:
	"""
	BaseGeometry class
	"""
    def area(self):
    	"""
		Method that checks if class has area implemented
		"""
        if hasattr(self, 'area'):
            raise Exception("area() is not implemented")
