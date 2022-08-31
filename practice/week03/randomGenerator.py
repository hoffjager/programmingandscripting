# Program that prints out a random number
# between 1 and 10
# Author: Jonathon Grealish

import random
# importing the random module gives the program a random number generator.

# random.randint will return a random number within the range.
number = random.randint(1,10)

print("Here is a random number: {}".format(number))
# The program will output the string above, with variables in order.