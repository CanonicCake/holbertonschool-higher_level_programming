#!/usr/bin/python3
"""Module documentation: Lists all cities from the database hbtn_0e_0_usa
by the table from safe injections"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """List all states from database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = '''SELECT *
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC;
               '''
    cursor.execute(query)
    cities = cursor.fetchall()
    cities = [item[2] for item in cities if item[4] == argv[4]]
    print(', '.join(cities))
