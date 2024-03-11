#!/usr/bin/python3
"""
This module defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The firstname of the user.
        last_name (str): The lat name of the user.
    """


    email = ""
    password = ""
    first_name = ""
    last_name = ""
