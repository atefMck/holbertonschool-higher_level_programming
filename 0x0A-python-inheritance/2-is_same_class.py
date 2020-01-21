#!/usr/bin/python3
"""
This module adds a new function
"""


def is_same_class(obj, a_class):
	"""
	This function returs a boolean indicating the similarity between two classes
	"""
    return (type(obj) is a_class)
