# This program will allow the user to create new students and view students.
# Referring to week05, student.py & week06, studentmanagement.py (also _2.py and _3.py)
# Author: Jonathon Grealish

# We will write in the function doAdd(students):
# Read in the student's name. Read in the module names and grades.
# Test this function, it creates a student dict.
# We should add the student dict to list.
# Test this.

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit): ").strip()
    return modules