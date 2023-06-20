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
            return []
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
            list_of_obj_dicts = []
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                list_of_obj_dicts.append(obj_dict)

            json_str = Base.to_json_string(list_of_obj_dicts)
            jsonFile.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of thhe JSON string representation of json_string.

            Where:
                json_string is a string representing a list of dictionaries

            Condition:
                If json_string is None or empty, an empty list is returned
                otherwise a list represented by json_string.
        '''
        if json_string is None and len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes already set.

            Where:
                **dictionary can be thought as a double pointer to a dictionary

            Condition:
                To use the update method to assign all attributes, a 'dummy'
                instance is first created. i.e. a Rectangle or Square instance
                with dummy mandatory attributes (width, height, size, etc)
                then the update is called to this dummy instance to apply the
                real values.

                **dictionary must be used as **kwards of the method - update
        '''
        if dictionary and dictionary is not {}:
            if cls.__name__ == 'Rectangle':  # Checks the child class calling
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances.

            condition:
                If file does not exist, an empty list is returned
                Otherwise a list of instances.
        '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="UTF-8") as jsonFile:
                list_of_contents = Base.from_json_string(jsonFile.read())
            return [cls.create(**content) for content in list_of_contents]
        except FileNotFoundError:
            return []
