#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes at a specific index"""
    if idx >= 0 and idx < len(mylist):
        del my_list[idx]
    return (my_list)
