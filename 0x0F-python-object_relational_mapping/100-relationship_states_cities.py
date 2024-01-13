#!/usr/bin/python3

"""
A script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy.engine import Engine
from relationship_city import City
from relationship_state import Base, State
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
    Base.metadata.create_all(engine)
    Session: Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: Session = createSession(argv[1:])
    session.add(City(name='San Francisco', state=State(name='California')))
    session.commit()
    session.close()
