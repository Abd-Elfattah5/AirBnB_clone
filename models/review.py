#!/usr/bin/python3

"""Defines a review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review model.
    """

    place_id = ""
    user_id = ""
    text = ""