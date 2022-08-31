def arraySearch(arr, n, myNum):
    myNum = input("Please enter a number: ")
    if arr[n-1] == myNum:
        return("Yes, {} is in the array.".format(myNum))
    return("No, {} is not in the array.".format(myNum))

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
n = len(arr)
myNum = input("Please enter a number: ")

print(arraySearch(arr, n, myNum))
