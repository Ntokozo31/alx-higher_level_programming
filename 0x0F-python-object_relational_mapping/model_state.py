#!/usr/bin/python3
"""
Module model_state
Defines the State class and Base instance for SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
