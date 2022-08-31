def sort(arr):
    n = len(arr)
    for outer in range(n-1, 0, -1):
        for inner in range(0,outer,1):
            print(f"inner is {inner} swapping {arr[inner]} and {arr[inner+1]}")

            if arr[inner] > arr[inner+1]:
                temp = arr[inner]
                arr[inner] = arr[inner+1]
                arr[inner+1] = temp
                
        print(f"outer is {outer}")
        print(arr)

arr = [64, 34, 25, 12, 22, 11, 90]