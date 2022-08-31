def reverse(string):
    if len(string) == 0:
        return string
    return reverse(string[1:]) + string[0]
    
string = str(input("Enter the string to be reversed: "))

print(reverse(string))