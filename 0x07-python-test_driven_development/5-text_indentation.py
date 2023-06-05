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
    for letter in text:
        if letter == '.' or letter == '?' or letter == ':':
            print(letter, end='')
            print()
            print()
        else:
            print(letter, end='')
