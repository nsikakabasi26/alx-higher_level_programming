#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lst = abs(number) % 10
if number < 0:
    lst = -lst
l = "Last digit of {} is {} and is {}"
if lst > 5:
    print(l.format(number, lst, "greater than 5"))
elif lst == 0:
    print(l.format(number, lst, "0"))
elif lst < 6 and lst != 0:
    print(l.format(number, lst, "less than 6 and not 0"))
