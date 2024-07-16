class Contact:
    def _init_(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class ContactBook:
    def _init_(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")
    
    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add a new contact")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            contact = Contact(name, phone_number)
            contact_book.add_contact(contact)
        
        elif choice == '2':
            name = input("Enter contact name to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print(f"Contact found - Name: {contact.name}, Phone Number: {contact.phone_number}")
            else:
                print(f"Contact {name} not found.")
        
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '4':
            contact_book.display_contacts()
        
        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()