#!/usr/bin/env python3

"""
File: hangman.py
Name:

A python implementation of hangman
Concepts covered: Strings, if/else, while, functions
"""

import random
import sys

def main():
    # Code here
    tries = 5
    print("the answer is a 5 letter word")        
   
    word = ["y","a","s",'a','s']

    while(tries>0):
        guess = input('Guess a letter: ')
        if guess in word: 
            tries = tries -1
            print("correct, you have " + str(tries) + ' guesses remaining')
            var= word.index(guess)
            print(var)
            
               
               
               
               
               
               
               
               
            
    
            
    
    

        
def checkWin(guessed_letters, selected_word):
    # Code here
    print()
    



if __name__ == "__main__":
    main()
