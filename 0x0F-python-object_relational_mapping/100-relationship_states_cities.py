#!/usr/bin/python3

"""
A script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


def create_state_city():
    """
    Creates the State “California” with the City “San Francisco” in the database hbtn_0e_100_usa
    """
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()

    session.close()


if __name__ == "__main__":
    create_state_city()
