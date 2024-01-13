#!/usr/bin/python3

"""
A script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from typing import List
from sqlalchemy.engine import Engine
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


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
    Session: Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: Session = createEngine(argv[1:])
    query: List[State] = session.query(State)\
                                .filter(State.name.like('%a%'))\
                                .order_by(State.id).all()
    for state in query:
        print(f'{state.id}: {state.name}')
