#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """deletes at a specific index"""

    for idx in len(my_list):
        if idx >= 0:
            del my_list[idx]
        return (my_list)
