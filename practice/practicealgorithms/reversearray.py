def reverseArray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
reverseArray(arr, 0, 9)
print("The reversed array is: ")
print(arr)