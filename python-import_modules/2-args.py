#!/usr/bin/python3
if __name__ == "__main__":
    """ prints the numbers on an argument list
    will grab from the given line and print back
    under an argument"""

import sys
av = sys.argv
lowav = len(av) - 1

if lowav > 1:
    print(lowav, 'arguments:')
    for i in range(1, lowav + 1):
        print('{:d}: {}'.format(i, av[i]))
elif lowav == 1:
    print(lowav, 'arguments:')
    for i in range(1, lowav + 1):
        print("{:d}: {}".format(i, av[i]))
elif lowav == 0:
    print(lowav, 'arguments.')
