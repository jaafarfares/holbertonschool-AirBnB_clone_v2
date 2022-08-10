#!/usr/bin/python3
"""
    Update FileStorage with delete and all functions
"""

import json
import models
from models.state import State
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    the class file storage
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        returns the list of objects of one type of class. Example below
        with State """

        if cls is None:
            return self.__objects
        else:
            classes = {}
            for key, val in self.__objects.items():
                if isinstance(val, cls):
                    classes[key] = val

            return classes

    def delete(self, obj=None):
        """
        Delete a given object from __objects, if it exists.
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def new(self, obj):
        """
        ...
        """

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        ...............
        """

        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        ...............
        """

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def close(self):
        """
        ...............
        """
        self.reload()
