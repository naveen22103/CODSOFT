import sqlite3
from termcolor import colored
import re
import csv

# Database Setup
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT UNIQUE,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

# Add a Contact
def add_contact():
    name = input(colored("Enter Name: ", "cyan"))
    phone = input(colored("Enter Phone: ", "cyan"))
    email = input(colored("Enter Email: ", "cyan"))
    address = input(colored("Enter Address: ", "cyan"))

    if not validate_phone(phone):
        print(colored("Invalid phone number format. Please try again.", "red"))
        return

    if not validate_email(email):
        print(colored("Invalid email format. Please try again.", "red"))
        return

    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                       (name, phone, email, address))
        conn.commit()
        print(colored("Contact added successfully!", "green"))
    except sqlite3.IntegrityError:
        print(colored("Contact with this phone or email already exists.", "red"))
    finally:
        conn.close()

# View All Contacts
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, email FROM contacts")
    rows = cursor.fetchall()
    conn.close()

    print(colored("\nContact List:", "yellow"))
    for row in rows:
        print(colored(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}", "cyan"))

# Search Contact
def search_contact():
    query = input(colored("Enter name or phone to search: ", "cyan"))
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, email FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                   (f"%{query}%", f"%{query}%"))
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print(colored("\nSearch Results:", "yellow"))
        for row in rows:
            print(colored(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Email: {row[3]}", "cyan"))
    else:
        print(colored("No contacts found.", "red"))

# Update Contact
def update_contact():
    contact_id = input(colored("Enter the ID of the contact to update: ", "cyan"))
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    contact = cursor.fetchone()

    if not contact:
        print(colored("Contact not found.", "red"))
        conn.close()
        return

    name = input(colored("Enter new name (leave blank to keep current): ", "cyan")) or contact[1]
    phone = input(colored("Enter new phone (leave blank to keep current): ", "cyan")) or contact[2]
    email = input(colored("Enter new email (leave blank to keep current): ", "cyan")) or contact[3]
    address = input(colored("Enter new address (leave blank to keep current): ", "cyan")) or contact[4]

    cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                   (name, phone, email, address, contact_id))
    conn.commit()
    conn.close()
    print(colored("Contact updated successfully!", "green"))

# Delete Contact
def delete_contact():
    contact_id = input(colored("Enter the ID of the contact to delete: ", "cyan"))
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
    print(colored("Contact deleted successfully!", "green"))

# Export to CSV
def export_to_csv():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()

    with open("contacts_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Phone", "Email", "Address"])
        writer.writerows(rows)

    print(colored("Contacts exported to 'contacts_export.csv'!", "green"))

# Validate Phone Number
def validate_phone(phone):
    return bool(re.match(r"^\d{10}$", phone))

# Validate Email
def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

# Main Menu
def main_menu():
    while True:
        print(colored("\n=== Contact Management System ===", "yellow"))
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input(colored("Enter your choice (1-7): ", "cyan"))
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            print(colored("Goodbye!", "cyan"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

# Initialize Database and Run Program
if __name__ == "__main__":
    init_db()
    main_menu()
