#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    lst = abs(number) % 10
    print("{:d}".format(lst), end="")
    return (lst)
