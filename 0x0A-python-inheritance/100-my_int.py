#!/usr/bin/python3
"""
This module add a new int subclass
"""


class MyInt(int):
	"""
	This is the int subclass
	"""
    def __init__(self, value):
    	"""
		This is the MyInt init method
		"""
        self.value = value

    def __eq__(self, obj):
    	"""
		This method overrides the equal int method
		"""
        return (obj != self.value)

    def __ne__(self, obj):
    	"""
		This method overrides the not equal int method
		"""
        return (obj == self.value)
