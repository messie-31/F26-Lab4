#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py

# Follow the instructions from readme.md.
def sum(a, b):
    return a + b

def main():
    """Get two numbers from the user and print their sum."""
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    total = sum(n1, n2)
    print(f"The sum is: {total}")

if __name__ == "__main__":
    main()