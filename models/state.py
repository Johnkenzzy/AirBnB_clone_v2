#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class definition """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref='state', cascade='all, delete-orphan')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Return a list of city objects linked to the current state"""
            from models import storage, City
            cities_in_state = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
