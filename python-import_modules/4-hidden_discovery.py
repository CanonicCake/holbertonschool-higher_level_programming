#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """ Print all the names under hidden_4"""

names = dir(hidden_4)

for single_name in names:
    if single_name[:2] != "__":
        print(single_name)
