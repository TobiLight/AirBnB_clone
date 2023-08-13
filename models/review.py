#!/usr/bin/python3
# File: review.py
# Auhtors: Oluwatobiloba Light &
"""
Defines a class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines a Review Model

    Attr:
        place_id (str): Place's ID
        user_id (str): User's ID
        text (str): Review of the Place
    """
    place_id = ""
    user_id = ""
    text = ""
