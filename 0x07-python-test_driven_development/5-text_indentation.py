#!/usr/bin/python3

''' Defines a text identation function '''


def text_indentation(text):
    ''' prints a text with 2 new lines after each of these characters:
        ., ? and :

        Argument:
                text - A string to be indented
        Raises:
                TypeError if text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [':', '.', '?']
    result = " "

    for char in text:
        result += char
        if char in characters:
            result += '\n\n'

    print(result.strip())
