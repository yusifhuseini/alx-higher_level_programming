#!/usr/bin/python3

"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from MySQLdb.cursors import Cursor


def filterStatesByUserInput(params: list) -> None:
    """
    Filter states by user input
    Args:
        params (list): List of arguments given to script
    """
    query: str = """
    SELECT * FROM `states`
    WHERE BINARY `name` = '{}' ORDER BY `id` ASC""".format(params[3])
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
    except MySQLdb.Error:
        pass


if __name__ == '__main__':
    from sys import argv
    [host, user, db, name] = argv[1:]
    filterStatesByUserInput([host, user, db, name])
