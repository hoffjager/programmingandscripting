# This program will ask the user to enter in a number.
# The program will then tell the user if the number is even or odd.
# Author: Jonathon Grealish

number = int(input("Enter an integer: "))

# The if statement will calculate whether the input has a remainder.
# If there is no remainder, the output will state the number is even.
# Else, if there is a remainder, the output will state the number is odd.
if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))