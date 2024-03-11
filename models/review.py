#!/usr/bin/python3
"""
This module defines the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represent class managing review object.
    Attributes:
        place_id (str): The place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """


    place_id = ""
    user_id = ""
    text = ""
