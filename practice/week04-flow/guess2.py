# This program asks the user to guess a number
# The program will inform the user if their guess
# was above or below the correct answer
# The program will continue to prompt the user to
# guess until the user guesses correctly
# Author: Jonathon Grealish

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high") # if false, then guess > numberToGuess
    guess = int(input("Please guess again: "))
print ("Well done! Yes, the number was", numberToGuess)