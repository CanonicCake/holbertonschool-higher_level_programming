#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """ print infinite additions """

    av = sys.argv
    lowav = len(av)
    sum = 0

    if lowav > 1:
        for i in range(1, lowav):
            sum += int(av[i] + 1)
    print(sum)
