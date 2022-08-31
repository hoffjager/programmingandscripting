# This program asks the user to guess a number
# The program will continue to prompt the user to
# guess until the user guesses correctly
# Author: Jonathon Grealish

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again: "))
print ("Well done! Yes, the number was", numberToGuess)