#!/usr/bin/python3
def weight_average(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return (0)
        numerator, denominator = 0, 0
        i, j = 0, 1
        for num_set in my_list:
            numerator += num_set[i] * num_set[j]
            denominator += num_set[j]
        return (numerator / denominator)
