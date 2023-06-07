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
    skip_next_char = False

    for char in text:
        if skip_next_char:
            skip_next_char = False
            continue

        result += char
        if char in characters:
            result += '\n\n'
            skip_next_char = True

    print(result.strip())
