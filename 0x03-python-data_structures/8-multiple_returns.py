#!/usr/bin/python3

def multiple_returns(sentence):
    """returns lenth of sentence and first character"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
