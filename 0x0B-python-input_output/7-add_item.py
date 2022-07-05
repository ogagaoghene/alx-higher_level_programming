#!/usr/bin/python3
""" Script that adds arguments to a Python list and save them to a file. """


from sys import argv
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file


filename = "add_item.json"

try:
    listt = load_from_json_file(filename)
except:
    listt = []

for arg in argv[1:]:
    listt.append(arg)

save_to_json_file(listt, filename)
