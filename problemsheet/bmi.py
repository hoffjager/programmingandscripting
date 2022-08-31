# bmi.py
# This program will calculate the user's Body Mass Index
# Author: Jonathon Grealish
# References:
# https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx
# https://dev.to/mindninjax/how-to-build-a-bmi-calculator-in-python-4g2g

# The variable height will store the user's height input as a float with decimals.
# The variable weight will store the user's weight input as a float with decimals. 

height = float (input ("Enter your height (in m): "))
weight = float (input ("Enter your weight (in kg): "))

# The formula to calculate BMI is as follows:
# BMI = Weight/Height^2; **2 will calculate height to the power of 2.
# Round will round the result to two decimal places, indicated by the second 2 in the formula.
# If and Elif and Else statements can declare the health of the user based on their BMI result.

bmi = round (weight / height ** 2, 2)

if bmi <= 18.4:
    print ("Your calculated BMI is {}, you are underweight.".format(bmi))
elif bmi <= 24.9:
    print ("Your calculated BMI is {}, you are healthy.".format(bmi))
elif bmi <= 29.9:
    print ("Your calculated BMI is {}, you are overweight.".format(bmi))
elif bmi <= 34.9:
    print ("Your calculated BMI is {}, you are Class 1 obese.".format(bmi))
elif bmi <= 39.9:
    print ("Your calculated BMI is {}, you are Class 2 obese.".format(bmi))
else:
    print ("Your calculated BMI is {}, you are Class 3 obese.".format(bmi))