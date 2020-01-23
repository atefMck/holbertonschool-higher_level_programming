#!/usr/bin/python3
"""
This module adds a new function related to classes
"""

def inherits_from(obj, a_class):
	"""
	This functions returns if an object is a subclass from a class
	"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
