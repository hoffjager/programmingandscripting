# This programs rounds a number to the nearest even number.
# Author: Jonathon Grealish

# First step is to create two variables.
# numberToRound prompts the user to input a float number (containing decimals)
numberToRound = float(input("Enter a float number: "))

# After input, roundedNumber will round that number to the nearest even number. 
roundedNumber = round(numberToRound)

print("{} rounded is {}".format(numberToRound, roundedNumber))
# The program will output the string above, with variables in order.