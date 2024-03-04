"""
PROGRAM: lookup.py
AUTHOR: David Stampfli  
DATA: 2/25/2024
This program looks up the address for a person give their first and last name. 
INPUT:  Choose to lookup phone number ('1') or lookup address ('2) for a person. If the user does not provide a '1' or '2', the program will exit. 
The lookup data is provided by a file called address.txt which should be placed in the same directory as the Python file. 
OUTPUT:  The phone number or address for the user.
"""

# Used to get the path of file to open
from pathlib import Path
import json

def main() -> None:
    '''
    This function is the main function of the program.
    '''

    # Call the load_adresses function to load the addresses into the dictionary
    address_dict = load_adresses()

    # Pretty print the addresses loaded from the file
    #print(json.dumps(address_dict, indent=4))

    while True:
        choice = input('Lookuop (1) phone numbers or (2) addresses: ')
        choice = choice.strip().lower()

        if choice == '1':
            name = input('Enter space-separated first and last name: ')
            #pretty_print(name, choice)
        elif choice == '2':
            # Check if the name is in the dictionary
            # If it is, print the address
            name = input('Enter the name: ')
            #pretty_print(name, choice)
        else:
            print('Have a nice day!')
            break

        pretty_print(address_dict, name, choice)

def load_adresses() -> dict:
    '''
    This function loads the addresses from a file into a dictionary.
    '''

    # Create an empty dictionary to store the addresses
    address_dict = {}

    # Open the file and read in the addresses
    # IF the file is not, print the exception and return an empty dictionary
    try:
        file_path = Path(__file__).with_name("address.txt")
        with open(file_path, "r") as f:
            # Loop through each line in the file
            for line in f:
                # Clean the line and split it based on your desired delimiter (e.g., comma, space)
                address = line.strip().split(",")
                
                # Extract relevant information from the address parts
                name = address[0].strip().lower()   # Strip the name and convert to lowercase
                street = address[1].strip()
                city = address[2].strip()
                state = address[3].strip()
                zipcode = address[4].strip()
                phone = address[5].strip()
        
                # Add the address information to the dictionary with the name as the key
                address_dict[name] = {"street": street, "city": city, "state": state, "zipcode": zipcode, "phone": phone}
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)

    # Return the address dictionary
    return address_dict

def pretty_print(address_dict, name, choice = '1') -> None:
    '''
    This function prints the address or phone number for a given name.
    '''
    # Conver the name to lowercase for comparison
    name = name.lower()

    if choice == '1':
            # Check if the name is in the dictionary
            # If it is, print the phone
            if name in address_dict:
                print('Phone: ' + address_dict[name]['phone'])
            else:
                print('Name not found')
    elif choice == '2':
        # Check if the name is in the dictionary
        # If it is, print the address
        if name in address_dict:
            print('Street: ' + address_dict[name]['street'])
            print('City: ' + address_dict[name]['city'])
            print('State: ' +  address_dict[name]['state'])
            print('Zip Code: ' + address_dict[name]['zipcode'])
        else:
            print('Name not found')    

# Call the main function
if __name__== "__main__":
    main()