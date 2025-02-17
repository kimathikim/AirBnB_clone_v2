#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects

        return {
            key: value
            for key, value in FileStorage.__objects.items()
            if cls is None or isinstance(value, cls)
        }

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.to_dict()["__class__"] + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        tmp = {}
        with open(FileStorage.__file_path, "w") as f:
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                if not temp:
                    print("File is empty")
                    return
            for key, val in temp.items():
                self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            print(f"Error: File '{FileStorage.__file_path}' not found.")

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside - if obj is equal to None,
        the method should not do anything"""
        if obj:
            key = obj.to_dict()["__class__"] + "." + obj.id
            del FileStorage.__objects[key]

    def close(self):
        """function to reload"""
        self.reload()
