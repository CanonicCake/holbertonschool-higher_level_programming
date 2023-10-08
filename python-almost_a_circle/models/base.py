#!/usr/bin/python3
"""The base class in models"""
import json


class Base:
    """Defines a Base class"""

    def __init__(self, id=None):
        """Initilize id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
