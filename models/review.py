#!/usr/bin/python3
from os import getenv
from models import *
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):

    if getenv('HBNB_TYPE_STORAGE', "fs") != "db":
        place_id = ""
        user_id = ""
        text = ""

    else:
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
