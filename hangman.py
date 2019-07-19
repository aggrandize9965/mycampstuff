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
    var = ["_",'_','_',"_",'_']
    while(tries>0):
        i = 0
        guess = input('Guess a letter: ')
        while i <len(word):
            if word[i] == guess: 
                tries = tries -1
                print("correct, you have " + str(tries) + ' guesses remaining')
                
               
               
               
               
               
               
               
               
            
                i +=1
    
            
    
    

        
def checkWin(guessed_letters, selected_word):
    # Code here
    print()
    



if __name__ == "__main__":
    main()
