#!/usr/bin/python3
''' Defines a class 'Base'.'''
import json


class Base:
    ''' Represents a class 'Base'.'''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Initializes objects of class Base.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation of 'list_dictionaries'

            Where:
                list_dictionaries = a list of dictionaries
            Condition:
                If list_dictionaries is None or empty, "[]" is returned.
                Otherwise, the JSON string representation of list_dictionaries
                is retuned.
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON string representation of list_objs to a file.

            Where:
                list_objs is a list of instances who inherits of Base (i.e.
                    a list of Rectangle or list of Square instances.
            Conditions:
                filename must be <Class name>.json e.g. Rectangle.json
                File must be overwritten if it already exists.
        '''
        with open(cls.__name__ + ".json", 'w', encoding="UTF-8") as jsonFile:
            json_list_of_objs = []
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                json_list_of_objs.append(obj_dict)
            json_str = Base.to_json_string(json_list_of_objs)
            jsonFile.write(json_str)
