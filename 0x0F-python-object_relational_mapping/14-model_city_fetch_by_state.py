#!/usr/bin/python3

"""
A  that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from typing import Any
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createSession(args: list) -> sessionmaker:
    """Create a MySQL database session
    """
    engine: Any = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(args[0], args[1], args[2])
    )
    Base.metadata.create_all(engine)
    Session: sessionmaker = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: sessionmaker = createSession(argv[1:])
    query: City = session.query(City.name, City.id, State.name)\
        .join(State, City.state_id == State.id).order_by(City.id).all()
    for city in query:
        print(f'{city[2]}: ({city[1]}) {city[0]}')
    session.close()
