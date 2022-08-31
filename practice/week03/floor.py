# This program floors a number (rounding it down to a whole integer).
# Author: Jonathon Grealish

import math
# importing the math module allows the use of numerous methods and constants.

numberToFloor = float(input("Enter a float number: "))

# importing math allows the use of math.floor, this rounds down the integer.
flooredNumber = math.floor(numberToFloor)

print("{} floored is {}".format(numberToFloor, flooredNumber))
# The program will output the string above, with variables in order.