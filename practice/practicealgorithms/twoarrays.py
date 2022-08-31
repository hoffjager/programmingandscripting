def findMissing(arr, arr2):
  
    for i in range(n):
        for j in range(m):
            if (arr[i] == arr2[j]):
                break
  
        if (j == m - 1):
            print(arr[i], end = " ")

if __name__ == "__main__":
      
    arr = [42, 12, 21, 30]
    arr2 = [12, 30, 45]
    n = len(arr)
    m = len(arr2)
    findMissing(arr, arr2)
