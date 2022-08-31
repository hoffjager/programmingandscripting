# This program asks the user to guess a randomly generated number.
# The program will inform the user if their guess was above or below the correct answer.
# The program will continue to prompt the user to guess until the user guesses correctly.
# Author: Jonathon Grealish

import random
# importing the random module gives the program a random number generator.

numberToGuess = random.randint(0,101)
# random.randint will return a random number within the range (index 0 to index 101 = 0-100)

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        print("Too high") # if false, then guess > numberToGuess
    guess = int(input("Please guess again: "))
print ("Well done! Yes, the number was", numberToGuess)
# The while loop checks to see if the user's guess is not equal to the randomly assigned number.
# Adding an if statement within helps to see whether input is below or above the random answer.
# If the guess is below the random answer, the output will say too low, and Please guess again:.
# Else, then the guess is above the correct answer, the output will say too high, and Please guess again:.
# The while loop will repeat and continue to prompt the user until guessed correctly.
# Once the input is equal, the user will receive a successful output. 