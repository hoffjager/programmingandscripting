# This program allows the user to input a float number.
# consisting of US $ and cents, it converts the float number to cents.
# Author: Jonathon Grealish

# float allows the user to input $ and c.
cent = float(input("Please enter an amount: "))

# abs will ensure the user's input is an absolute number.
final = abs(cent)

print("That amount in cent is {}".format(final*100))
# The program will output the string above, with the variable * 100
# * 100 will convert $ into c.