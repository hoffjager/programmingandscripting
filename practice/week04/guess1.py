# This program asks the user to guess a number
# The program will continue to prompt the user
# to guess until the user guesses correctly.
# Author: Jonathon Grealish

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again: "))
print ("Well done! Yes, the number was", numberToGuess)
# The while loop checks to see if the user's guess is not equal to the correct number.
# If it is not equal, the output will say Wrong, and Please guess again:.
# The while loop will repeat and continue to prompt the user until guessed correctly.
# Once the input is equal, the user will receive a successful output.  