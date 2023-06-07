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
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    conditional_chars = [':', '.', '?']
    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in conditional_chars:
            if text[c] in conditional_chars:
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
