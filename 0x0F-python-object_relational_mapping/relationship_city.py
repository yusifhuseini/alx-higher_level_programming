#!/usr/bin/python3

"""
A script that defines model City via SQLAlchemy ORM
"""
from relationship_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class City(Base):
    """Defines a city model
    Attributes:
        id (Integer): Primary key
        name (String): Name of City instance
        state_id (Integer): Foreign key to State model
        state (State): State object reference
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
