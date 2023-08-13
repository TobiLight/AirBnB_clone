#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from uuid import uuid4
import datetime
import inspect    


class TestBaseModel(unittest.TestCase):
    def test_has_atrributes(self):
        # Test attributes after instantiation
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"), True)
        self.assertTrue(hasattr(instance, "created_at"), True)
        self.assertTrue(hasattr(instance, "updated_at"), True)
        
    def test_id_is_a_string(self):
        # Test if ID is a string
        instance = BaseModel()
        self.assertTrue(type(instance.id) == str, True)
        self.assertEqual(type(instance.id) == int, False)
        self.assertEqual(type(instance.id), str)
        
    def test_id_is_unique(self):
        # Test if ID is unique
        instance =  BaseModel()
        self.assertEqual(instance.id == uuid4(), False)
        
    def test_unique_id(self):
        # Test two instances don't have the same ID
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
    
    def test_created_is_datetime(self):
        # Test created_at attribute is an instance of datetime
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime.datetime)
    
    def test_created_is_datetime(self):
        # Test updated_at attribute is an instance of datetime
        instance = BaseModel()
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        
    def test_to_dict_method(self):
        # Test to_dict() method returns a dict
        instance = BaseModel()
        base_dict = instance.to_dict()
        self.assertIsInstance(base_dict, dict)
        
    def test_save_method(self):
        # Test save() method updates updated_at
        instance = BaseModel()
        initial_val = instance.updated_at
        instance.save()
        updated_val = instance.updated_at
        self.assertNotEqual(initial_val, updated_val)
        
    def test_str_method(self):
        # Test __str__ method
        instance = BaseModel()
        expected_format = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(instance.__str__(), expected_format)
        
    def test_model_from_dict(self):
        # Test creation of BaseModel from a dictionary
        instance = BaseModel()
        new_instance = instance.to_dict()
        instance2 = BaseModel(**new_instance)
        self.assertEqual(instance.id, instance2.id)
        self.assertEqual(instance.created_at, instance2.created_at)
        self.assertEqual(instance.updated_at, instance2.updated_at)
        self.assertNotEqual(instance, instance2)
        
    def test_has_args(self):
        # Test if instance has args
        def has_args(cls):
            return "args" in inspect.signature(cls.__init__).parameters
        self.assertTrue(has_args(BaseModel))
    
    def test_has_kwargs(self):
        # Test if instance has kwargs
        def has_kwargs(cls):
            return "kwargs" in inspect.signature(cls.__init__).parameters
        self.assertTrue(has_kwargs(BaseModel))

if __name__ == '__main__':
    unittest.main()