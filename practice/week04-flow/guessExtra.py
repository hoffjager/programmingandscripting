# This program asks the user to guess a randomly generated number
# The program will inform the user if their guess
# was above or below the correct answer
# The program will continue to prompt the user to
# guess until the user guesses correctly
# Author: Jonathon Grealish

import random

numberToGuess = random.randint(0,101)

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high") # if false, then guess > numberToGuess
    guess = int(input("Please guess again: "))
print ("Well done! Yes, the number was", numberToGuess)