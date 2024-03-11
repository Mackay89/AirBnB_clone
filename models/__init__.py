#!/usr/bin/python3
"""
This module initializes the file storage system for models.

This module contains the initializatiom logic for the file storage system used by models in the application.
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
