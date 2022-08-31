def rreverse(s):
    if s == "":
        return s[::1]
    else:
        return rreverse(s[1:]) + s[0]

s = input("Please enter a string: ")
print(rreverse(s))