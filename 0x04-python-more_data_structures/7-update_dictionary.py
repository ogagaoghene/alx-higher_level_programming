#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for index in a_dictionary:
            if index == key:
                a_dictionary[index] = value
    return a_dictionary
