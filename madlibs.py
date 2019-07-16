#!/usr/bin/env python3

"""
File: madlibs.py
Name:

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""
import random
def main():
    # Code here
    print("This is a madlibs please enter the following information to complete a story.")
    name = input("please enter your name: ")
   
    place = input("please enter a place: ")
   
    vehicle = input("please enter a name of a vehicle: ")
    verb = input("please enter a name of a verb: ")
    adjective = input("please enter a name of an adjective: ")
    
    print(name + " went to visit his best friend at "+ place + ". While he was there, he saw a " + adjective +' ' +  vehicle + ' ' +  verb  + " down the road! While unsure of what was going on at first, " + name +" soon found out that it was a streetrace!")
        
if __name__ == "__main__":
    main()
