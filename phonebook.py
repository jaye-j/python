import pickle
import os.path

import time
import sys

if os.path.isfile('contacts.pickle'):
    with open('contacts.pickle', 'rb') as fh:
        contacts = pickle.load(fh)

else:

    contacts = {
    "Jaye": "281-222-2222", 
    "Austin": "281-333-3333",
    "Daniel": "281-444-4444"
    }



print("""\nElectronic Phone Book
=====================
Enter 1 to look up an entry.\n
Enter 2 to set an entry.\n
Enter 3 to delete an entry.\n
Enter 4 to list all entries.\n
Enter 5 to quit.
=====================""")
while True:
    
    userAction = int(input("What would you like to do? (1-5) "))

    if userAction == 1:
        lookup = input("Which entry would you like to view? ")
        print(contacts[lookup])

    elif userAction == 2:
        name = input("What is the name? ")
        number = input("What is the number?")

        contacts[name] = number
        print(contacts)

    elif userAction == 3:
        name = input("Who would you want to delete? ")
        del contacts[name]
        print("Contact Deleted.")
        print(contacts)

    elif userAction == 4:
        items = contacts.items()
        for key, value in contacts.items():
            print(f"{key}: {value}")
        
    elif userAction == 5:
        print("Shutting down Electronic Phonebook...")
        time.sleep(.5)
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.2)
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.2)
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.2)
        print("Goodbye")
        time.sleep(.3)

        with open('contacts.pickle', 'wb') as fh:
            pickle.dump(contacts, fh)

        exit()

    else:
        print("INVALID ENTRY!")

