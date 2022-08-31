def bubble_sort(arr):
    n = len(arr) # Traverse through all elements in the array.
    for outer in range (n-1, 0, -1):
        for inner in range (0, outer, 1):
            if arr[inner] > arr[inner+1]: # Swap if the element found is greater than the next element.
                temp = arr[inner] # Temporary variable in place to swap values.
                arr[inner] = arr[inner+1]
                arr[inner+1] = temp
        print(arr)

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)