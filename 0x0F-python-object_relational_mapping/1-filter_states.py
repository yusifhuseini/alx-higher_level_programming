#!/usr/bin/python3

"""
A script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from MySQLdb.cursors import Cursor


def filterStates(params: list) -> None:
    """Filter states that start with 'N' and prints them in ascending order
    Args:
        params (list): List of arguments given to script
    """
    query: str = """
    SELECT * FROM `states`
    WHERE BINARY `name` LIKE 'N%' ORDER BY `id` ASC"""
    try:
        conn: MySQLdb.Connection = MySQLdb.connect(
            host="localhost", port=3306, user=params[0],
            passwd=params[1], db=params[2], charset="utf8"
        )
        cursor: Cursor = conn.cursor()
        cursor.execute(query)
        records: list[tuple] = cursor.fetchall()
        for row in records:
            if row[1][0] == 'N':
                print(row)
        cursor.close()
        conn.close()
    except MySQLdb.Error:
        pass


if __name__ == '__main__':
    from sys import argv
    [host, user, db] = argv[1:]
    filterStates([host, user, db])
