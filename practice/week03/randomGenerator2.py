# Program that prints out a random number between a user's inputted range.
# Author: Jonathon Grealish

import random
# importing the random module gives the program a random number generator.

x = int(input("Enter first number in the range: "))
y = int(input("Enter last number in the range: "))

# random.randint will return a random number within the inputted range.
number = random.randint(x,y)

print("Here is a random number: {}".format(number))
# The program will output the string above, with variables in order.