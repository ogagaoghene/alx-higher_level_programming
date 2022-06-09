#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    returned_value = list(a_dictionary.keys())[0]
    biggest_number = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > biggest_number:
            biggest_number = v
            returned_value = k
    return (returned_value)
