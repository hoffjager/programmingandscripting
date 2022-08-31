# This program generates 10 random numbers.
# It prints them out, then it prints the Top 3.
# Author: Jonathon Grealish

# I will use a list to store and manipulate the numbers

import random
# importing the random module gives the program a random number generator.

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range (0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
    # random.randint will return a random number within the established range.
print("{} random numbers\t {}".format(howMany,numbers))

topOnes = numbers.copy() # This will copy the random array of the numbers variable.
topOnes.sort(reverse = True) # This returns the top 3 numbers in descending order.
print("The top {} are \t\t {}".format(topHowMany, topOnes[0:topHowMany]))
# The program will output the string above, with variables in order.