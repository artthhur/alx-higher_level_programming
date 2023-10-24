#!/usr/bin/python3
"""
Module that contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    State class definition.

    Represents a state in the states table.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
            )

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"
