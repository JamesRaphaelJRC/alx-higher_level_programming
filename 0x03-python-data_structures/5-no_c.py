#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
            new_str = ""
            for word in my_string:
                if word != 'c' and word != 'C':
                    new_str += word
            return(new_str)
