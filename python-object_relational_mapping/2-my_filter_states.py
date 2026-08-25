#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Use BINARY for case-sensitive comparison
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s "
        "ORDER BY id ASC",
        (state_name,)
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
