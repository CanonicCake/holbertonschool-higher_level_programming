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
