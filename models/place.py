#!/usr/bin/python3
# File: place.py
# Auhtors: Oluwatobiloba Light &
"""
Defines a class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines a Place Model

    Attr:
        city_id (str): ID of the City
        user_id (str): ID of the User
        name (str): Name of the Place
        description (str): Description of the Place
        number_rooms (int): Number of rooms the Place has
        number_bathrooms (int): Number of bathrooms the Place has
        max_guests (int): Number of guests allowed in the Place
        price_by_night (int): Price of this Place for a night
        latitude (float): Latitude of this Place
        longitude (float): Longitude of this Place
        amenity_ids ([str]): List of amenity IDs of the Place        
    """
    city_id = ""
    user_id=""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
