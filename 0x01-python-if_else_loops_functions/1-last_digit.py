#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number
lastdig =  abs(digit) % 10
if digit < 0:
    lastdig = -lastdig
    if lastdig > 5:
        print(f"Last digit of {digit} is {lastdig} and is greater than 5")
    elif lastdig == 0:
        print(f"Last digit of {digit} is {lastdig} and is 0")
    else:
        print(f"Last digit of {digit} is {lastdig} and is less than 6 and not 0")
