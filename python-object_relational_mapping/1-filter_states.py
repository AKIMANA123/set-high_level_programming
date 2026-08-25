#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    # Using LIKE with wildcard % for pattern matching
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
