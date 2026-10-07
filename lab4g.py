#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: Practice map, filter and lambda expressions.
# Usage: ./lab4g.py

# Follow the instructions from readme.md.
numbers = list(range(2, 11))
numbers = list(map(lambda x: x ** 2, numbers))
print(numbers)
divisible_by_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(divisible_by_2)