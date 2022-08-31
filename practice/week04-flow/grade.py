# This program reads in a student's
# percentage and prints out
# the corresponding grade
# Author: Jonathon Grealish

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # greater than 0 & up to 39
    print ("Fail")
elif percentage < 50: # between 40 & 49
    print ("Pass")
elif percentage < 60: # between 50 & 59
    print ("Merit 2")
elif percentage < 70: # between 60 & 69
    print ("Merit 1")
else:
    print ("Distinction") # this is the only remaining option