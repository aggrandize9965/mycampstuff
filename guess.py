
import random
def main():
        while(True): 
                randum = random.randint(1,20)
                tries = 3
              
                
                while (tries>0):
                
                        guess= int(input("please guess a number from 1 to 20: "))
                        if (guess == randum):
                                print("you got it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                                break
                                
                        elif (guess >randum): 
                                tries= tries - 1
                                print("answer too large, you have " + str(tries) + " left")
                        elif (guess <randum):
                                tries = tries -1 
                                print('answer too small, you have ' + str(tries) +" left")
                                
                name = input("press p to play again or press enter to quit.")
                if (name != "p"):
                        print('exiting game')
                        break
        
main()