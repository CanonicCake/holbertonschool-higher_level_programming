#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        print(len(sentence), sentence[0])
