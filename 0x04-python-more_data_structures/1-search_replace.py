#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """a search and replace function"""

    latest_list = []

    for items in my_list:
        if items == search:
            latest_list.append(replace)
        else:
            latest_list.append(items)

    return (latest_list)
