#!/usr/bin/python3

"""
A script that lists all City objects from the database hbtn_0e_101_usa
"""

from sys import argv
from typing import List
from sqlalchemy.engine import Engine
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createSession(args: List[str]):
    """Create a MySQL database session
    Args:
        args (list): List of arguments passed to the script
    """
    engine: Engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(args[0], args[1], args[2]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session = createSession(argv[1:])
    for city in session.query(City).order_by(City.id):
        print(f'{city.id}: {city.name} -> {city.state.name}')
    session.close()
