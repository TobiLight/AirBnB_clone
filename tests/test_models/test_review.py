#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import re
import time
from models.review import Review
from models.engine.file_storage import FileStorage
import os
import json
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()