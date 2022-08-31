# hello2.py
# This program allows the user to enter his/her name.
# The program will then greet the user with a nice message.
# Author: Jonathon Grealish

name = input("Enter your name: ")
# establishing a variable called name.
# The user will be prompted to enter their name (the value to be stored in the variable)

print ('Hello {}, \nIt is nice to meet you.'.format(name))
# {} will contain the user's input, in this case, format option = .format(name)
# \n creates a line break in the sentence.