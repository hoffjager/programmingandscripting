# This program that takes a positive floating-point number as input
# and outputs an approximation of its square root.
# Author: Jonathon Grealish
# References:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# https://surajregmi.medium.com/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64

# We take a reasonable guess (approximate root) for the square root.
# Add the approximate root with the original number, divided by the approximate root, and divide by 2.
# Continue until the difference in the approximate root, along the iterations is less than the desired value (or precision value).

# n = 16, x0 = 16, we determine the next approximation by the formula:
# x_n+1 = (x_i + n/x_i) / 2
# Continue the iterative process until the root is found to the desired accuracy.
# Iteration #1: x1 = (16 + 16/16) / 2 = 8.5
# Iteration #2: x2 = (8.5 + 16/8.5) / 2 = 5.19117647059
# Iteration #3: x3 = (5.19117647059 + 16/5.19117647059) / 2 = 4.13666472255 
# Iteration #4: x4 = (4.13666472255 + 16/4.13666472255) / 2 = 4.0022575248
# Iteration #5: x5 = (4.0022575248 + 16/4.0022575248) / 2 = 4.00000063669
# Iteration #6: x6 = (4.00000063669 + 16/4.00000063669) / 2 = 4 
 
def squareRoot(n, l):
    x = n # assuming the sqrt of n as n only
    count = 0 # to count the number of iterations 
  
    while(1):
        count += 1 # increment the count each time going through the loop 
        root = 0.5 * (x + (n / x)) # calculate more closed x
        if (abs(root - x) < l): # check for closeness
            break  
        x = root # update root
    return root 
  
# Driver code 
if __name__ == "__main__" : 
  
    n = int(input("Please enter a positive number: "))
    l = 0.00001 
  
    print("The square root of", n, "is approximately:", squareRoot(n, l))