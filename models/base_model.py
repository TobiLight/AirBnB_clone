#!/usr/bin/python3
# File: base_model.py
# Auhtors: Oluwatobiloba Light &&
"""
Defines a base model class BaseModel
"""
import uuid
import datetime
import models


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiate an instance of BaseModel
        """
        if len(kwargs) < 1:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.datetime.\
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns the string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
