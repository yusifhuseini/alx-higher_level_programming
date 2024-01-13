#!/usr/bin/python3

"""
A script that defines model via SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base: declarative_base = declarative_base()


class State(Base):
    """Defines a state model
    Attributes:
        id (Integer): Primary key
        name (String): Name of state
        cities (City): List of City instances associated with this state
    """
    __tablename__: str = 'states'
    id: Column = Column(Integer, primary_key=True, nullable=False)
    name: Column = Column(String(128), nullable=False)

    cities: relationship = relationship(
        "City", backref="state", cascade="all, delete"
    )
