#!/usr/bin/python3
"""
File containing the print my name method.
first_name is the first name
last_name is the last name
"""

def say_my_name(first_name, last_name=""):
    """ 'say_my_name(first_name, last_name="")' print name method
        first_name is the first name
        last_name is the last name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
