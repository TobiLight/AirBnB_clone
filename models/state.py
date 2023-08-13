#!/usr/bin/python3
# File: state.py
# Auhtors: Oluwatobiloba Light &
"""
Defines a class State that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Defines a State Model

    Attr:
        name (str): Name of the state
    """
    name = ""
