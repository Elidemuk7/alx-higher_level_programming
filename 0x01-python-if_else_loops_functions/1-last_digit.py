#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdigit = abs(number) % 10
if lstdigit > 5:
    print(f"Last digit of {number} is {lstdigit} and is greater than 5")
elif lstdigit == 0:
    print(f"Last digit of {number} is {lstdigit} and is 0")
else:
    print(f"Last digit of {number} is {lstdigit} and is less than 6 and not 0")