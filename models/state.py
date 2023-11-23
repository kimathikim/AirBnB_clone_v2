#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "state"
        name = Column(String(128), nullable=False)
        cities = relationship("city", backref="state")
    else:

        @property
        def cities(self):
            """hat returns the list of City instances with state_id
            equals to the current State.id"""
            city_dict = models.storage.all(City)
            st = []
            for city in city_dict.values():
                if city.state_id == self.id:
                    st.append(city)
            return st
