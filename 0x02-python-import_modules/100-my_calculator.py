#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    from calculator_1 import add, sub, mul, div

    sys.argv[1], sys.argv[2], sys.argv[3] = int(a), ops, int(b)
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if ops is not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = 0
    if ops == '+':
        result = add(a, b)
    elif ops == '-':
        result = sub(a, b)
    elif ops == '*':
        result = mul(a, b)
    elif ops == '/':
        result = div(a, b)
    
    print("{} {} {} = {}".format(a, ops, b, result))
