#!/usr/bin/python3
from datetime import datetime
import uuid
import models
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

if getenv('HBNB_TYPE_STORAGE', "fs") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The base class for all storage objects in this project"""
    if getenv('HBNB_TYPE_STORAGE', "fs") == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(timezone=True), default=datetime.now(),
                            nullable=False)
        updated_at = Column(DateTime(timezone=True), default=datetime.now(),
                            nullable=False,
                            onupdate=datetime.now)

    def __init__(self, *args, **kwargs):
        """initialize class object"""
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe
