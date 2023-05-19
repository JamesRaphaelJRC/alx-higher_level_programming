#!/usr/bin/python3
''' roman_to_int - Converts roman numerals to integers '''
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    map_numerals_to_ints = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result, prev_value = 0, 0
    for char in reversed(roman_string):
        int_value = map_numerals_to_ints.get(char, 0)

        if int_value < prev_value:
            result -= int_value
        else:
            result += int_value

        prev_value = int_value
    return (result)
