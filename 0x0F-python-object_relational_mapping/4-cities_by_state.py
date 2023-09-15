#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """Get the arguments from the command line"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    """Connect to the MySQL server"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8")
    """Create a cursor object"""
    cursor = db.cursor()
    """Execute the SQL query"""
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   ORDER BY cities.id ASC;""")
    """Fetch all the rows from the result set"""
    rows = cursor.fetchall()
    """Loop through each row and print it"""
    for row in rows:
        print(row)
    """Close the cursor and the database connection"""
    cursor.close()
    db.close()
