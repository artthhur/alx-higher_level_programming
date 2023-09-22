#!/usr/bin/python3
"""
Module that contains the class definition of a City and links to the table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class definition.

    Represents a city in the cities table.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        return ("<City(id={}, name='{}', state_id={})>"
                .format(self.id, self.name, self.state_id))
