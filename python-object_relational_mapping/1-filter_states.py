#!/usr/bin/python3
"""Module documentation: Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """List all states from database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
