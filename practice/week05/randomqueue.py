# This program puts 10 random numbers into a queue.
# The program will then output all values in the queue.
# Then it will take one number at a time from the queue.
# The program will print that number, along with the current numbers.
# Author: Jonathon Grealish

import random
# importing the random module gives the program a random number generator.

queue = [] # establishing the array within the queue variable.
numberOfNumbers = 10
rangeTo = 100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo)) # random numbers will be stored in the queue array.
    # random.randint will return a random number within the range.

print ("Queue is {}".format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0) # pop takes the first element from the list.
    print ("Current number is {} and the queue is {}".format(currentNumber, queue))
# The while loop checks if the length of the queue is not equal to 0.
# If it is != 0, the first number in the queue is removed from the list, and output is displayed.
# The loop repeats until every number is removed

print ("The queue is now empty")