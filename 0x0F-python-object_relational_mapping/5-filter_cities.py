#!/usr/bin/python3

"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

from typing import Any
import MySQLdb


def getCitiesByStates(params: list) -> None:
    """
    Filter cities by states from by user input
    Args:
        params (list): List of arguments given to script
    """
    query: str = """
    SELECT cities.name FROM `cities`
    LEFT JOIN `states` ON cities.state_id = states.id
    WHERE states.name = %s"""
    try:
        conn: MySQLdb.Connection = MySQLdb.connect(
            host="localhost", port=3306, user=params[0],
            passwd=params[1], db=params[2], charset="utf8"
        )
        cursor: Any = conn.cursor()
        cursor.execute(query, (params[3],))
        records: list[tuple] = cursor.fetchall()
        for row in records:
            if row == records[-1]:
                return (print(row[0]))
            print(row[0], end=", ")
        else:
            print("")
        cursor.close()
        conn.close()
    except MySQLdb.Error:
        pass


if __name__ == '__main__':
    from sys import argv
    [host, user, db, state] = argv[1:]
    getCitiesByStates([host, user, db, state])
