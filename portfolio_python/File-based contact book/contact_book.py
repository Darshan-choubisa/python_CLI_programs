FILE_NAME = "contacts.txt"


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully.\n")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
        
        if not contacts:
            print("No contacts found.\n")
            return
        
        print("\n--- contact list ---")
        for contact in contacts:
            name, phone, email = contact.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
        print()
    except FileNotFoundError:
        print("No contacts file found.\n")



def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    found = False

    with open(FILE_NAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if search_name == name.lower():
                print(f"\nFound: {name}, {phone}, {email}\n")
                found = True
                break
    if not found:
        print("Contact not found.\n")



def update_contacts():
    search_name = input("Enter name to update: ").strip().lower()
    updated_contacts = []
    found = False

    with open(FILE_NAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if name.lower() == search_name:
                print("Enter new details: ")
                phone = input("New phone: ").strip()
                email = input("New email: ").strip()
                updated_contacts.append(f"{name},{phone},{email}\n")
                found = True
            else:
                updated_contacts.append(contact)
    
    with open(FILE_NAME, "w") as file:
        file.writelines(updated_contacts)

    if found:
        print("contacts updated successfully.\n")
    else:
        print("contacts not found.\n")




def delete_contacts():
    search_name = input("Enter name to delete: ").strip().lower()
    updated_contacts = []
    found = False

    with open(FILE_NAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if name.lower() != search_name:
                updated_contacts.append(contact)
            else:
                found = True
    
    with open(FILE_NAME, "w") as file:
        file.writelines(updated_contacts)

    if found:
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")
    


def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Updated Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contacts()
        elif choice == "5":
            delete_contacts()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.\n")



if __name__ == "__main__":
    main()
