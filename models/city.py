#!/usr/bin/python3
from models import *
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    state_id = ""
    name = ""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
