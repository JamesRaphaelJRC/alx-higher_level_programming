#!/usr/bin/python3
''' Adds all arguments to a python list and save them to a file
    'add_item.json'
'''
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

try:
    my_object = load_from_json_file("add_item.json")
except Exception:
    my_object = []
my_object.extend(arguments)
save_to_json_file(my_object, "add_item.json")
