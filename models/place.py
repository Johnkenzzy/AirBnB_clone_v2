#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ Defines a place and its attributes """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship('User', back_populates='places')
    cities = relationship('City', back_populates='places')

    reviews = relationship(
            'Review', back_populates='place', cascade='all, delete-orphan')

    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'Place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False
                ),
            Column(
                'amenity_id', String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False
                )
            )

    amenities = relationship(
            'Amenity', secondary=place_amenity,
            back_populates='place_amenities', viewonly=False)
    # amenity_ids = []
