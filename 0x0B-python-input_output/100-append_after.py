#!/usr/bin/python3
''' Defines a function append_after'''


def append_after(filename="", search_string="", new_string=""):
    ''' Inserts new_string after search_string in the file "filename"'''
    wholefile = []
    with open(filename, 'r+', encoding="UTF-8") as myFile:
        wholefile = myFile.readlines()
        print(wholefile)
        for line, line_contents in enumerate(wholefile):
            if search_string in line_contents:
                wholefile.insert(line + 1, new_string)
                break
        myFile.seek(0)
        myFile.writelines(wholefile)
