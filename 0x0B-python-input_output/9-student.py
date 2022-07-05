#!/usr/bin/python3
""" Student to JSON. """


class Student:
    """ Define a student """
    def __init__(self, first_name, last_name, age):
        """ Instation with first_name, last_name, age. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Dictionary representation of a Student. """
        return self.__dict__
