#!/usr/bin/python3

"""
A script that lists all states from the database hbtn_0e_0_usa
"""

from typing import Any
import MySQLdb


def getStates(params: list) -> None:
    """
    Gets all states from a database and prints them in ascending order

    Args:
        params (list): List of arguments given to script
    """
    query: str = "SELECT * FROM states ORDER BY states.id ASC"
    try:
        conn: MySQLdb.Connection = MySQLdb.connect(
            host="localhost", port=3306, user=params[0],
            passwd=params[1], db=params[2], charset="utf8"
        )
        cursor: Any = conn.cursor()
        cursor.execute(query)
        records: list[tuple] = cursor.fetchall()
        for row in records:
            print(row)
        cursor.close()
        conn.close()
    except MySQLdb.Error:
        pass


if __name__ == '__main__':
    from sys import argv
    [host, user, db] = argv[1:]
    getStates([host, user, db])
