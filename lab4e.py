#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py
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
    print("Your result:",compute(num1=n1, num2=n2, operation=opp))

    print(compute(num1=13, num2=45, operation='*'))
    print(compute(operation='/', num2=45, num1=13))
    print(compute(num1=13, operation='-', num2=45))
    print(compute(num1=13, num2=45, operation='+'))
    print(compute(num1=13, num2=45))

if __name__ == "__main__":
    main()