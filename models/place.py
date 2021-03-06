#!/usr/bin/python3
from os import getenv
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):

    if getenv('HBNB_TYPE_STORAGE', "fs") != "db":
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenities = [""]

    else:
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PlaceAmenity(Base):
    if getenv('HBNB_TYPE_STORAGE', "fs") == "db":
        __tablename__ = 'place_amenity'
        place_id = Column(String(60), ForeignKey("places.id"),
                          primary_key=True, nullable=False)
        amenity_id = Column(String(60), ForeignKey("amenities.id"),
                            primary_key=True, nullable=False)
