#!/usr/bin/python3

"""
A script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.engine import Engine

from sqlalchemy.orm.session import Session
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
    Session: Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session: Session = createEngine(argv[1:])
    newState: State = State(name='Louisiana')
    session.add(newState)
    session.commit()
    print(newState.id)
