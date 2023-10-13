#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] != '+' and sys.argv[2] != '-'\
            and sys.argv[2] != '*' and sys.argv[2] != '/':
                print("Unknown operator. Available operators: +, \
                        -, * and /")
                sys.exit(1)
    sys.argv[1], sys.argv[2], sys.argv[3] = int(a), ops, int(b)
    if len(sys.argv) - 1 == 3:
        result = a + b
        print("{} {} {} = {}".format(a, ops, b, result))
