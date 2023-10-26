#!/usr/bin/python3
"""Module documentation: take in argument through query and displays all
arguments from database injections"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """List all states from database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states"
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
