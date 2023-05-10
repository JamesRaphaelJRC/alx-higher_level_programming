#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for char in str:
        char = ord(char)

        if char > 96 and char < 123:
            newstr += chr(char - 32)
        else:
            newstr += chr(char)
    print("{}".format(newstr))
