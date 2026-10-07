#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: Create Some Complex Functions.
# Usage: ./lab4b.py

# TO DO 1: Add the docstring
# @Function definition: Returns a new list of the even numbers from a list
# @param: A list of integers
# @return: List of even numbers if present in the original list
# TO DO 2: Create the function.
# TO DO 3: Call the function.
def even_number(numbers):
    """ Return a new list containing only the even numbers. """
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

mylist = [34,45,56,67,88,-90,12,-49]
result = even_number(mylist)
print(result)