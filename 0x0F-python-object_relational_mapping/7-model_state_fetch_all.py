#!/usr/bin/python3

"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from typing import Any
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createEngine(args: list) -> Any:
    """Create a database engine
    Return:
        Session (class)
    """
    engine: Any = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(args[0], args[1], args[2]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session: sessionmaker = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: Any = createEngine(argv[1:])
    query: list = session.query(State).order_by(State.id)
    for state in query:
        print(f'{state.id}: {state.name}')
