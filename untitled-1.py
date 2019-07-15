
import random

def main():
    #put code here
  randum = random.randint(1,10)
  tries = 3
  while(tries>0):
    guess = int(input("Guess a number between 1 and 10:"))
    if (guess == randum):
      print("nice one")
      break
    else: 
      tries = tries - 1
      print("you have " + str(tries) + " left")
      if (tries >0):
        print("not a nice one, go again")
  if (tries == 0):
      print("not a nice one, dont go again")
     




if __name__ == "__main__":main()
    