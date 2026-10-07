#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py

# TO DO 1: Add the docstring
# @Function definition: It checks whether a number in the list is even 
# @param: A list of numbers
# @return: True if any number in the list is even, False if it is not even
# TO DO 2: define the function with name `is_even`.
# TO DO 3: Call the function `is_even`.
def is_even(numbers):
    """ Return True if any number in the list is even, False if it is not even """
    result = False
    for n in numbers:
        if n % 2 == 0:
            result = True
            break
    return result

mylist = [45,-67,78,89,-12,34]
even = is_even(mylist)
print(even)