#!/usr/bin/python3
"""This module contains the Base class"""
import json


class Base:
    """This is a Base class handling ids"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method converting python list of dic to jsop string"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return ('[]')
        else:
            return (json.dumps(list_dictionaries))
