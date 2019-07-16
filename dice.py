#!/usr/bin/env python3

"""
File: dice.py
Name:

Rolls a dice and outputs the result
Concepts covered: Random, printing
"""

import random

def main():
    # Code here
    answer = "c"
    while (answer == "c"):
        answer = input("Type c to roll the dice")
        randum = random.randint(1,6)
        print("you rolled a " +str(randum)+"!")
      
    




















if __name__ == "__main__":
    main()
