#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0")
    elif argc == 1:
        print("{}".format(int(argv[0])))
    else:
        total = 0
        for i in range(argc):
            total += int(argv[i])
        print(total)
