#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for x in list_keys:
        if value == a_dictionary.get(x):
            del a_dictionary[x]

    return (a_dictionary)
