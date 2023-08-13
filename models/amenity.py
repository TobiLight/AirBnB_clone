#!/usr/bin/python3
# File: amenity.py
# Auhtors: Oluwatobiloba Light &
"""
Defines a class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines an Amenity Model

    Attr:
        name: Name of the amenity
    """
    name = ""
