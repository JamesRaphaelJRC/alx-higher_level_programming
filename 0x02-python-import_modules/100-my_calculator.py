#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    ac = len(sys.argv) - 1
    av = sys.argv[1:]

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(av[0])
    b = int(av[2])

    if av[1] == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif av[1] == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif av[1] == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif av[1] == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
