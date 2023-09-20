#!/usr/bin/python3
from sys import argv as aug

if __name__ == "__main__":
    if len(aug) - 1 == 0:
        print('0 arguments.')
    else:
        if len(aug) - 1 == 1:
            print("{} argument:".format(len(aug) - 1))
        else:
            print("{} arguments:".format(len(aug) - 1))
        for i in range(1, len(aug)):
            print("{}: {}".format(i, aug[i]))
