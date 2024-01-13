#!/usr/bin/python3

"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.engine import Engine

from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createEngine(args: list) -> Session:
    """Create a database engine
    Return:
        Session (class)
    """
    engine: Engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(args[0], args[1], args[2]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session: sessionmaker = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: Session = createEngine(argv[1:])
    query: State = session.query(State).first()
    if query:
        print(f'{query.id}: {query.name}')
    else:
        print('Nothing')
