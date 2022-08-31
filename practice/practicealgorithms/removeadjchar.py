def removeDuplicates(s):
    chars = list(s)
    prev = None
    k = 0
 
    for c in s:
        if prev != c:
            chars[k] = c
            prev = c
            k = k + 1
 
    return ''.join(chars[:k])
 
 
if __name__ == '__main__':
 
    s = "AAABBBBCCCDDDD"
 
    s = removeDuplicates(s)
    print(s)