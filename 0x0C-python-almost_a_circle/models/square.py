#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New Square class, inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method for Square class"""
        Rectangle.__init__(self, size, size, x, y, id)
