#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models import BaseModel, Base, Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class definition """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
            'Place', secondary=Place.place_amenity, back_populates='amenities')
