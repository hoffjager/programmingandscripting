# This program reads in a file and outputs the number of any letter requested.
# Author: Jonathon Grealish
# References:
# https://www.computerhope.com/issues/ch001721.htm
# https://www.sanfoundry.com/python-program-read-file-counts-number/

fileName = input("Enter file name: ")
l = input("Enter letter to be searched: ")
k = 0                            # This variable stores the occurrences of the letter to be searched for.
 
with open (fileName, 'rt') as f: # This opens the file to read through the entire file
    for line in f:               # for loop, for each line of text
        words = line.split()     # Each line is split into a list of words
        for i in words:          # for loop, for searching through each word in the line
            for letter in i:     # for loop, for searching through each letter in each word
                if(letter == l): # if the letter provided by user and letter found via iteration are equal
                    k = k + 1    # the letter count is incremented by 1 each time the letter is found
print("Occurrences of the letter", l, ":", k)