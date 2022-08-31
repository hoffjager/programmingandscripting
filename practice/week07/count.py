# This program counts how many times it was run.
# We will have to store data outside of memory.
# That is accessible each time the program is run (persistent data).
# Author: Jonathon Grealish

filename = "count.txt" # txt file created with number 0

# This function reads in a number from the existing file.
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

# This function reads in a number from the existing file, and overwrites it.
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

num = readNumber()
num += 1
print("We have run this program {} times.".format(num))
writeNumber(num)