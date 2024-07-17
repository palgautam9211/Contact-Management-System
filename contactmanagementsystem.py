class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Contact '{name}' added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for name, phone_number in self.contacts.items():
                print(f"{name}: {phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact details for {name}: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManagementSystem()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            contact_manager.add_contact(name, phone_number)
        elif choice == "2":
            contact_manager.display_contacts()
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_manager.search_contact(name)
        elif choice == "4":
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
