#!/usr/bin/python3

"""
A script that lists all State objects, and
corresponding City objects, contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_city import City
from sqlalchemy.engine import Engine
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


def createSession(args: list) -> Session:
    """Create a MySQL database session
    Args:
        args (list): List of arguments passed to the script
    """
    engine: Engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(args[0], args[1], args[2]),
        pool_pre_ping=True
    )
    Session: Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: Session = createSession(argv[1:])
    for state in session.query(State).order_by(State.id):
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')
    session.close()
