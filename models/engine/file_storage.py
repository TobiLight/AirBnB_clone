#!/usr/bin/python3
# File: file_storage.py
# Author: Oluwatobiloba Light
"""
Defines a class FileStorage
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as JSON_File:
            data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(data, JSON_File)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.all(self)[key] = classes[val['__class__']]\
                        (**val)
        except FileNotFoundError:
            pass
