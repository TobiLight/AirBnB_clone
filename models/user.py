#!/usr/bin/python3
# File: user.py
# Auhtors: Oluwatobiloba Light &
"""
Defines a class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a User Model

    Attr:
        email (str): User email
        password (str): User password
        first_name (str): User first name
        last_name (str): User last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
