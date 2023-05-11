#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = (len(sys.argv) - 1)
    if ac == 0:
        print(ac, "arguments.")
    else:
        print(ac, "arguments:")
        for i in range(1, ac + 1):
            print("{}: {}".format(i, sys.argv[i]))
