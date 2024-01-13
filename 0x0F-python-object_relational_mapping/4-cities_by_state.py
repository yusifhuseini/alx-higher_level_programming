#!/usr/bin/python3

"""
A script that execute a query and prevent sql injection
"""

import MySQLdb
from MySQLdb.cursors import Cursor


def getCitiesByStates(params: list) -> None:
    """
    Filter states by user input and prevent sql injection
    Args:
        params (list): List of arguments given to script
    """
    query: str = """
    SELECT cities.id, cities.name, states.name
    FROM cities LEFT JOIN states ON cities.state_id = states.id"""
    try:
        conn: MySQLdb.Connection = MySQLdb.connect(
            host="localhost", port=3306, user=params[0],
            passwd=params[1], db=params[2], charset="utf8"
        )
        cursor: Cursor = conn.cursor()
        cursor.execute(query)
        records: list[tuple] = cursor.fetchall()
        for row in records:
            print(row)
        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print(e)


if __name__ == '__main__':
    from sys import argv
    [host, user, db] = argv[1:]
    getCitiesByStates([host, user, db])
