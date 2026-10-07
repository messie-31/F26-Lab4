#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py

# Follow the instructions from readme.md.
def compute(num1, num2, operation='+'):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Cannot be divided by zero!"
        return num1 / num2
    else:
        return "Invalid operation"

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    opp = input("Choose an operation (+, -, *, /): ")
    print(f"Your result: {compute(n1, n2, opp)}\n")

    print(compute(13, 45, '*'))
    print(compute(13, 45, '/'))
    print(compute(13, 45, '-'))
    print(compute(13, 45, '+'))
    print(compute(13, 45))

if __name__ == "__main__":
    main()