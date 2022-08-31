# This program stores a student's name, along with a list of her courses and grades in a dict.
# The program will then print out her data.
# Author: Jonathon Grealish

# student dictionary will contain variables, name, modules, and module info within.
# 
student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade": 99
        }
    ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
# The program will output the value in name stored in the dictionary.
# The program will output the values from within modules, namely courseName and grade.