import random
import IPython
from random import randint
from IPython.display import clear_output
guessed=False
number=randint(0,100)
guesses=0
while not guessed:
    ans=input("Please enter a number:")
    guesses+=1
    clear_output()
    if int(ans)==number:
        print("Your guess is right, it took {} attemt for guessing".format(guesses))
        break
    elif int(ans)<number:
        print("Your guess is less than correct number, correct number is {}".format(number))
    elif int(ans)>number:
        print("Your guess is greater than correct number, correct number is {}".format(number))
