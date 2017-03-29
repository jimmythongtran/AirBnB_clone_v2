#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
