#!/usr/bin/python3
"""
Script that takes arguments and displays all values in the states table
where name matches the argument — safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # sys.argv[1] = MySQL username
    # sys.argv[2] = MySQL password
    # sys.argv[3] = database name
    # sys.argv[4] = state name to search (safe)
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cur = db.cursor()

    # SAFE query — using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
