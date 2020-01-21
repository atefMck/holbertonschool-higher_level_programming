#!/usr/bin/python3


def add_attribute(obj, atr, value):
    if hasattr(obj, "__dict__"):
        setattr(obj, atr, value)
    else:
        raise TypeError("can't add new attribute")
