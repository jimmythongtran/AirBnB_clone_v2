#!/usr/bin/python3
from os import getenv
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base


class State(BaseModel, Base):

    if getenv('HBNB_TYPE_STORAGE', "fs") != "db":
        name = ""

    else:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE', "fs") != "db":
        @property
        def cities(self):
            cities = storage.all("City").values()
            myList = []
            for i in cities:
                if self.id == i.state_id:
                    myList.append(i)
            return myList

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
