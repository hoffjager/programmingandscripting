# This program counts how many times it was run.
# Author: Jonathon Grealish

filename = "count.txt" # txt file created with number 0

# This function reads in a number from the existing file.
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

num = readNumber()
print(num)