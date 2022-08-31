# This program will allow the user to create new students and view students.
# Referring to week05, student.py & week06, studentmanagement.py (also _2.py)
# Author: Jonathon Grealish

# We will write in the function doAdd(students):
# Read in the student's name. Read in the module names and grades.
# Test this function, it creates a student dict.
# We should add the student dict to list.

students = []
def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent)

doAdd(students)
doAdd(students)

print(students)