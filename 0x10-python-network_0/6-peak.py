#!/usr/bin/python3
''' Defines an algorithm for peak finding.'''


def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    listSize = len(list_of_integers)

    if listSize == 1:
        return list_of_integers[0]
    elif listSize == 2:
        return max(list_of_integers)

    mid = int(listSize / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
