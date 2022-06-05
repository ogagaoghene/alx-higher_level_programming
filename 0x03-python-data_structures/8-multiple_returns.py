#!/usr/bin/python3

def multiple_returns(sentence):
    length_of_sentence = len(sentence)
    if length_of_sentence == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return ((length_of_sentence, f_char))
