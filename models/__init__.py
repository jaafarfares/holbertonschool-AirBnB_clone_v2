#!/usr/bin/python3
'''
    Package initializer
'''
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place, place_amenity
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
