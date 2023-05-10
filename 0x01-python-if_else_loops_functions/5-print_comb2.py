#!/usr/bin/python3
for i in range(0, 100):
    if i >= 0 and i < 99:
        first = i // 10
        last = i % 10
        print("{}{}, ".format(first, last), end='')
    else:
        print(i)
