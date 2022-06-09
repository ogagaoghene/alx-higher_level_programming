#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for index in a_dictionary:
        new_d[index] = a_dictionary[index] * 2
    return new_d
