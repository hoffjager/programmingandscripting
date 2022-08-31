# This program reads in numbers until the user enters 0.
# It will then print back out again and their average.
# Author: Jonathon Grealish

numbers = []
# [] array can store numerous inputs from the user.

number = int(input("Enter number (0 to quit): "))
# Enter first number, then we check if it is 0 in the while loop.

while number != 0:
    numbers.append(number) # the input will be stored in the numbers array, if it is != 0.
    number = int(input("Enter another (0 to quit): ")) # while loop continues to prompt until 0 is entered.

for value in numbers:
    print (value) # outputs all the number inputs.

# Average will be equal to float of the sum, divided by the length(number) of inputs. 
average = float(sum(numbers)) / len(numbers)

print ("The average is {}".format(average))
# The program will output the string above, with the established variable.