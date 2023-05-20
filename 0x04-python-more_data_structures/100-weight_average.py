#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    numerator = sum(x * y for x, y in my_list)
    denominator = sum(y for _, y in my_list)

    return (numerator / denominator)
