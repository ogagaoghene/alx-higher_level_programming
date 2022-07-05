#!/usr/bin/python3
""" Student to JSON with filter. """


class Student:
    """ Define a student """
    def __init__(self, first_name, last_name, age):
        """ Instation with first_name, last_name, age. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation of a Student.
        Return:
            a dictionary representation of a Student instance
            with specified attributes
        """
        if attrs is None:
            return self.__dict__

        dictt = {}
        for i in attrs:
            if i in self.__dict__:
                dictt[i] = self.__dict__[i]
        return dictt
