#!/usr/bin/python3
"""
Defines the City class and its relationship with the State class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """
    City class that links to the 'cities' table in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
