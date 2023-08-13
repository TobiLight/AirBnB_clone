#!/usr/bin/python3
# File: __init__.py
# Author: Oluwatobiloba Light
"""Package Initialization"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
