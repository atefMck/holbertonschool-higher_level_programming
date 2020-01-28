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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method converting python list of dic to jsop string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """method writes string repr of list of objs in a file"""
        name = cls.__name__ + ".json"
        list = []
        if list_objs is not None:
            for obj in list_objs:
                list.append(obj.to_dictionary())
        with open(name, "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """method parses json string to python list of objects"""
        if json_string is None:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(5)
        elif cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """method writes string repr of list of objs in a file"""
        name = cls.__name__ + ".json"
        file = open(name, "r")
        data = cls.from_json_string(file.read())
        list = []
        for obj in data:
            list.append(cls.create(**obj))
        file.close()
        return (list)
