# This program reads in a string and strips any leading or trailing spaces.
# It converts all letters to lower case.
# It also outputs the length of the original string and the normalised one.
# Author: Jonathon Grealish

# The user is prompted to enter a string, rawString.
# normalisedString will return the input stripped of spaces and letters in lower case.
rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

# len calculates the length of both strings.
lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That string normalised is : {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalised))
# The program will output the strings above, with established variables in order.