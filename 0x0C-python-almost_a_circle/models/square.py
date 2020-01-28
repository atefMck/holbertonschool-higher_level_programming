#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New Square class, inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method for Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method formatting string Square output"""
        string0 = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        string1 = "{}/{} ".format(self.x, self.y)
        string2 = "- {}".format(self.width)
        return(string0 + string1 + string2)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size
