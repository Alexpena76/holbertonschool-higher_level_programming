#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
(SQL injection safe)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cur = db.cursor()

    # Using placeholders to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    # Extract only the city names and print them comma-separated
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()
