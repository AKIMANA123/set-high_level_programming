#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Case-sensitive comparison using BINARY
    cursor.execute(
        "SELECT * FROM states WHERE BINARY LEFT(name, 1) = 'N' "
        "ORDER BY id ASC"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
