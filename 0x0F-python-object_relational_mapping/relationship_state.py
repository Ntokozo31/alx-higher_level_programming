#!/usr/bin/python3
"""
This script defines a State class and a Base instance to be used with
SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete-orphan'
    )
