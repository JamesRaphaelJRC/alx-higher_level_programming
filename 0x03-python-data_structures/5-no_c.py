#!/usr/bin/python3
def no_c(my_string):
    for word in my_string:
        new_str = ""
        for word in my_string:
            if word != 'c' and word != 'C':
                new_str += word
    return(new_str)
