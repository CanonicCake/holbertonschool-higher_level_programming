#!/usr/bin/python3
if __name__ == "__main__":
    """ prints the numbers on an argument list
    will grab from the given line and print back
    under an argument"""

import sys

aug = sys.argv
count = len(aug) - 1

if count == 0:
    print('0 arguments:')
else:
    print("{} arguments:".format(count))
for i in range(count):
    print("{}: {}".format(i + 1, aug[i + 1]))
