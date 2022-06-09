#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for integer_tuples in my_list:
        average += integer_tuples[0] * integer_tuples[1]
        div += integer_tuples[1]
    return float(average / div)
