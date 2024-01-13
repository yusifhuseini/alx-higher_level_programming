#!/usr/bin/python3

"""
A script that defines model via SQLAlchemy ORM
"""
from typing import Any, Union
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base: Any = declarative_base()

class State(Base):
    """Defines a state model
    Attributes:
        id (Integer): Primary key
        name (String): Name of state
        cities (City): List of City instances associated with this state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
