# This program will ask the user
# to enter in a number
# The program will then tell the user
# if the number is even or odd.
# Author: Jonathon Grealish

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))