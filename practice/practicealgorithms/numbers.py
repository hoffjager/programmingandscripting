def even_spaced (a,b,c):
    if(a > b):
        temp = a
        a = b
        b = temp

    if(b > c):
        temp = b
        b = c
        c = temp

    if(a > b):
        temp = a
        a = b
        b = temp

    return b - a == c - b

print(even_spaced(2,4,6))