# This program reads in numbers
# until the user enters 0
# It will then print back out again
# and their average
# Author: Jonathon Grealish

numbers = []

number = int(input("Enter number (0 to quit): "))
# Enter first number then we check if it's 0 in the While loop

while number != 0:
    numbers.append(number) # read the next number and check if it's 0
    number = int(input("Enter another (0 to quit): "))

for value in numbers:
    print (value)

# Average to be a float to accommodate answers with decimals
average = float(sum(numbers)) / len(numbers)
print ("The average is {}".format(average))