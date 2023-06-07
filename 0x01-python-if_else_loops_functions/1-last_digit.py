#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    r = number % 10
else:
    r = number % (-10)
if r > 5:
    print(f"Last digit of {number:d} is {r:d} and is greater than 5")
elif r == 0:
    print(f"Last digit of {number:d} is {r:d} and is 0")
else:
    print(f"Last digit of {number:d} is {r:d} and is less than 6 and not 0")
