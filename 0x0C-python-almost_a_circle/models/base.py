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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """method writes string repr of list of objs in a file"""
        name = cls.__name__ + ".json"
        file = open(name, "w")
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        file.write(cls.to_json_string(list))
        file.close()

    def from_json_string(json_string):
        """method parses json string to python list of objects"""
        return(json.loads(json_string))
