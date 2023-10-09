#!/usr/bin/python3
"""The base class in models"""
import json


class Base:
    """Defines a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilize id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def to_json_string(list_dictionaries):
        """JSON string by serialization"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Wrties json string to file"""
        filename = cls.__name__ + ".json"
        json_data = []
        if list_objs is not None:
            for obj in list_objs:
                json_data.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_data))
