#!/usr/bin/python3
'''
    Implementation of the State class
'''
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""

        @property
        def cities(self):
            '''
                getter attribute cities that returns the list of City
                instances with state_id equals to the current State.id
            '''
            cities = models.storage.all(City).values()
            cities_by_state = []

            for city in cities:
                if city.state_id == self.id:
                    cities_by_state.append(city)

            return cities_by_state
    else:
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
