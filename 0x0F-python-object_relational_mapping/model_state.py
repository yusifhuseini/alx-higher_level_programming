#!/usr/bin/python3

"""
A script that defines model via SQLAlchemy ORM
"""

from typing import Any, Union
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base: Any = declarative_base()


class State(Base):
    """
    Defines a state model
    """
    __tablename__: str = 'states'
    id: Column = Column(Integer, primary_key=True, nullable=False)
    name: Union[Column, str] = Column(String(128), nullable=False)
