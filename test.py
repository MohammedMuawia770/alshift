import json
import os

# Define file path for storing contacts
file_path = "contacts.json"

# Check if the file exists; if not, create an empty file
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump({}, f)  # Initialize with an empty dictionary

# Load existing contacts from the file
with open(file_path, "r") as f:
    the_numbers = json.load(f)

# Function to add a new contact
def add_contact(name, phone):
    the_numbers[name] = phone  # Add to dictionary
    with open(file_path, "w") as f:
        json.dump(the_numbers, f)  # Save updated contacts to file
    print(f"Contact '{name}' added successfully!")

# Main Loop
while True:
    try:
        print("\nSaved Contacts:", the_numbers)
        name = input("Enter the name of the person you want to add: ")
        phone = int(input("Enter their phone number: "))
        add_contact(name, phone)  # Add and save contact
        
        continue_adding = input("Do you want to add another? (yes/no): ").strip().lower()
        if continue_adding != 'yes':
            break
    except ValueError:
        print("Please enter a valid number.")
