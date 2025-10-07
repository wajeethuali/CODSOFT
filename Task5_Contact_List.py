# Contact List Program

# Dictionary to store contacts
contacts = {}

# Function to display the menu
def display_menu():
    print("\n*** Contact List Menu ***")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

# Function to add a contact
def add_contact():
    name = input("Enter the contact name: ").strip()
    if name in contacts:
        print(f"{name} already exists in the contact list.")
    else:
        phone = input("Enter the phone number: ").strip()
        contacts[name] = phone
        print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\n*** All Contacts ***")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Contact list is empty.")

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found in the contact list.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"{name} not found in the contact list.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
