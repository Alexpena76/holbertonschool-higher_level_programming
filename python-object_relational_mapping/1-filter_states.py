#!/usr/bin/python3
"""
Lists all states starting with 'N' from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cur = db.cursor()

    # Select states that start with 'N' sorted by id
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print each row
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
