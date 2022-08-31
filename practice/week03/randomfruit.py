# This program prints out a random fruit.
# Author: Jonathon Grealish

import random
# importing the random module gives the program a random number generator.

# The variable fruits contains an array [] of random fruits.
fruits = ["Apple", "Orange", "Pear", "Banana", "Strawberry", "Raspberry", "Blueberry", "Pineapple", "Kiwi"]

# We want a random number between 0 and the length - 1.
# random.randint will return a random number within the range.
index = random.randint(0,len(fruits)-1)

# The fruit variable takes a random fruit from the array in the index variable above.
fruit = fruits[index]

print("Here is a random fruit: {}".format(fruit))