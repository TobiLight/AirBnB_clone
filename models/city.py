#!/usr/bin/python3
# File: city.py
# Auhtors: Oluwatobiloba Light &
"""
Defines a class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines a City Model

    Attr:
        state_id (str): State's ID. This will be State.id
        name: Name of the City
    """
    state_id = ""
    name = ""
