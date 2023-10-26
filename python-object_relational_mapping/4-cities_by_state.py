#!/usr/bin/python3
"""Module documentation: Lists all cities from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """List all states from database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute('''SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN state ON cities.state_id = state.id
                   ORDER BY cities.id ASC;
                   ''')
    cities = cursor.fetchall()
    for city in cities:
        print(city)
