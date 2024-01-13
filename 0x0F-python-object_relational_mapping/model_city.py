#!/usr/bin/python3

"""
A script that defines model City via SQLAlchemy ORM
"""

from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """
    Defines a city model
    """
    __tablename__: str = 'cities'
    id: Column = Column(Integer, primary_key=True, nullable=False)
    name: Column = Column(String(128), nullable=False)
    state_id: Column = Column(Integer, ForeignKey('states.id'), nullable=False)
