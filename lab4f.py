#!/usr/bin/env python3
# Author: Mehtaash Kaur
# Date: 2026-10-7
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py

# Follow the instructions from readme.md.
def get_initials(*args):
    initials = []
    for letter in args:
        initials.append(letter[0])
    return initials

def main():
    result = get_initials("Alice", "Bob", "Charlie", "David")
    print(result)

if __name__ == "__main__":
    main()