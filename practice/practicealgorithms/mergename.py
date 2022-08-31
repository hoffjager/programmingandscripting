def merge(string, string2):
    result = "" 
    i = 0
    while (i < len(string)) or (i < len(string2)):
        if (i < len(string)):
            result += string[i] 
        if (i < len(string2)):
            result += string2[i]  
        i += 1 
    return result

string = "jnto"
string2 = "oahn"
 
print(merge(string, string2))