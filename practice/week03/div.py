# This program reads two numbers and will output the integer answer.
# Also outputs the remainder, if applicable.
# Author: Jonathon Grealish

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x//y) # // gives the integer division.
remainder = x % y # % (modulus) gives the remainder.

print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))
# The program will output the string above, with established variables in order.