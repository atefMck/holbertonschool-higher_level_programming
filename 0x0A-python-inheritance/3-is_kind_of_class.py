#!/usr/bin/python3
"""
This module adds a new function
"""


def is_kind_of_class(obj, a_class):
    """ This function returs a boolean indicating the
    similarity between two classes or them being a
    subclass of each other """
    return (type(obj) is a_class or issubclass(type(obj), a_class))
