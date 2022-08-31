# This program will allow the user to create new students and view students.
# Referring to week05, student.py & week06, studentmanagement.py
# Author: Jonathon Grealish

# We will use the function created in studentmanagement.py, this prints out a menu of commands.

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice
def doAdd():
    # we fill this in later
    print ("in adding")
def doView():
    # we fill this in later
    print ("in viewing")

# main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lambda functions.
    # I am keeping this basic for the moment.
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nplease select either a,v or q")
    choice = displayMenu()