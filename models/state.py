#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    name = ""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
