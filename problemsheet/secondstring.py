# This program asks the user to input a string.
# The string then outputs every second letter in reverse order.
# Author: Jonathon Grealish
# References:
# https://realpython.com/python-strings/
# https://codegolf.stackexchange.com/questions/128496/hello-world-every-other-character

s = input ("Please enter a sentence: ")
# used to input a string, eg, "The quick brown fox jumps over the lazy dog".

reverse = s [::-1]
# reverses the string and slices from the end to the start of the input (with ::-1).

alternate = reverse [::2]
# removing every second character from the reversed string (with ::2).

print (alternate)
# prints the reversed string, with every second character removed.