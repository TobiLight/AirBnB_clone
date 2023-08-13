#!/usr/bin/python3
# File: file_storage.py
# Author: Oluwatobiloba Light
"""
Defines a class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        return self.__objects
       
    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj
          
    def save(self):
        """
        Serializes __objects to the JSON file
        """
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        
        json_str = json.dumps(data)
        
        with open(self.__file_path, 'w', encoding="utf-8") as JSON_File:
            JSON_File.write(json_str)
            
    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as JSON_File:
                json_file = json.load(JSON_File)
                for obj in json_file.values():
                    self.new(eval("{}({})".format(obj['__class__'], '**obj')))
        except FileNotFoundError:
            pass
        