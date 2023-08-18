#!/usr/bin/python3
# File: base_model.py
# Auhtors: Oluwatobiloba Light &&
"""
Defines a base model class BaseModel
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiate an instance of BaseModel
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict.update({'__class__':
                         (str(type(self)).split('.')[-1]).split('\'')[0]})
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns the string representation of the object"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
