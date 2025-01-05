#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class definition """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state')

    @property
    def cities(self):
        """Return the list of City instances as state_id equal State's id."""
        from models import storage
        from models.city import City

        all_cities = storage.all(City).values()  # Fetch all City objects
        return [city for city in all_cities if city.state_id == self.id]
