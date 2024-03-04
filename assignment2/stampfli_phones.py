"""
PROGRAM: phones.py
AUTHOR: David Stampfli  
DATA: 2/12/2024
This program lookups phone numbers in a data file given a user-provided last name, or a first and last name. 
INPUT: Last name, last name and first name, or nothing are supplied by the user.  The lookup data is provided 
by a file called phones.txt which should be in the same directory as the Python file.  
OUTPUT: The phone number or nothing
"""

# Used to get the path of file to open
from pathlib import Path

# Open the file and read in
file_path = Path(__file__).with_name("phones.txt")
with open(file_path, "r") as file:
    phones = file.readlines()

while True:
    name = input("Enter last name OR first name and last name of the phone number you are looking for: ")
    name = name.strip().lower()

    # Check if the user provided a name
    if (len(name)) == 0:
        print("No name provided, exiting the program!")
        break
    else:
        # Split the name string into an array so I can get the first name and last name from user's input
        names = name.split()

        if len(names) == 2:
            first_name = names[0]
            last_name = names[1]
        else:
            first_name = ""
            last_name=names[0]

        # Find the phone number using the last name
        found = False
        for phone in phones:
            phone_info = phone.split()
            
            # Filter on last name
            if last_name == phone_info[1].lower():
                found = True

                # If there's no first name, just use the last name 
                if len(first_name) == 0:
                    print(f"{phone_info[0]} {phone_info[1]}, {phone_info[2]}")
                # Since there is a first name, 
                else:
                    if first_name == phone_info[0].lower():
                        found = True
                        print(f"{phone_info[0]} {phone_info[1]}, {phone_info[2]}")
                    #else:
                    #    found = False
                
        if found == False:
            print(f"User {name} not found")




            
        




