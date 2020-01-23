#!/usr/bin/python3
"""
This module add a new list class
"""

class MyList(list):
	"""
	A subclass from list object
	"""
    def print_sorted(self):
    	"""
		This method prints the list sorted
		"""
        newList = eval(repr(self))
        newList.sort()
        print(newList)
