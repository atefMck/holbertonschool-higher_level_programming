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

    def update(self, *args, **kwargs):
        """method updating rectangle"""
        atrs = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        elif kwargs:
            for key, value in kwargs.items():
                for atr in atrs:
                    if key == atr:
                        setattr(self, key, value)

    def to_dictionary(self):
        """method returning dict form of rectangle"""
        square = dict()
        square["id"] = self.id
        square["width"] = self.width
        square["height"] = self.height
        square["x"] = self.x
        square["y"] = self.y
        return(square)
