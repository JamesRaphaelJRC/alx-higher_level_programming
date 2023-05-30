#!/usr/bin/python3

  """safe_print_list - Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """

def safe_print_list(my_list=[], x=0):
    if isinstance(my_list, list) and isinstance(x, int):
        num = 0
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
                num += 1
            except IndexError:
                break
        print("")
        return (num)
