# This program asks the user to input a positive integer.
# It then outputs successive values of a calculation within a function.
# At each step, the next value is calculated by taking the user's input value.
# If it is even, it is divided by two.
# Else if it is odd, it is multiplied by three, and one added.
# The program ends if the current value equals one.
# Author: Jonathon Grealish
# Reference:
# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# https://www.educative.io/edpresso/how-to-generate-the-collatz-sequence-in-python

# Defining a function named collatz to outline the calculations.
# The if and elif statements within the function
# check if the user inputs a number that is even or odd.
 
def collatz (number):
    if number % 2 == 0: # if even (using modulo % 2, with no remainder);
        print (number // 2) # program outputs the number divided by 2.
        return number // 2 # return will loop that result to the beginning of the function.

    elif number % 2 == 1: # if odd (using modulo % 2, with a remainder);
        result = 3 * number + 1 # program outputs the number tripled (and plus 1).
        print (result) # program outputs the calculation set above in the result variable.
        return result # return will loop that result to the beginning of the function.

n = input ("Please enter a positive integer: ")

while n != 1: # The program continues to loop, and ends when a result of 1 is calculated.
    n = collatz (int(n)) # This passes 'n' to the function, until a result of 1 is calculated.