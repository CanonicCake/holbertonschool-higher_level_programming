#!/usr/bin/python3
if __name__ == "__main__":
    """ prints the numbers on an argument list
    will grab from the given line and print back
    under an argument"""

import sys
aug = sys.argv
count = len(aug) - 1

if count > 1:
    print(count, 'arguments:')
    for i in range(1, count + 1):
        print('{:d}: {}'.format(i + 1, aug[i + 1]))
elif count == 1:
    print(count, 'arguments:')
    for i in range(1, count + 1):
        print("{:d}: {}".format(i, aug[i]))
elif count == 0:
    print('0 arguments.')
