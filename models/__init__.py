#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ
from models.engine.db_storage import DBStorage

glb_storage = environ.get('HBNB_TYPE_STORAGE')

if glb_storage == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
