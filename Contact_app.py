import sqlite3
import re
import csv
import os

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Connect to SQLite DB
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create contacts table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT PRIMARY KEY,
    age INTEGER,
    email TEXT,
    mobile TEXT
)
''')
conn.commit()

# Main program loop
while True:
    print("\n===== Contact Book APP =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Backup to CSV")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        if cursor.fetchone():
            print(f"{name} already exists.")
        else:
            age = int(input("Enter age: "))
            while True:
                email = input("Enter email: ")
                if is_valid_email(email):
                    break
                print("Invalid email. Try again.")
            mobile = input("Enter mobile: ")
            cursor.execute("INSERT INTO contacts (name, age, email, mobile) VALUES (?, ?, ?, ?)",
                           (name, age, email, mobile))
            conn.commit()
            print(f"{name} added successfully.")

    elif choice == "2":
        name = input("Enter name to view: ")
        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        contact = cursor.fetchone()
        if contact:
            print(f"\nName: {contact[0]}\nAge: {contact[1]}\nEmail: {contact[2]}\nMobile: {contact[3]}")
        else:
            print("Contact not found.")


    elif choice == "3":

        name = input("Enter name to update: ")

        cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))

        result = cursor.fetchone()

        if result:

            print(f"\nCurrent details for {name}:")

            print(f"Age: {result[1]}")

            print(f"Email: {result[2]}")

            print(f"Mobile: {result[3]}")

            # Prompt user to enter new values or press Enter to keep old

            new_age = input("Enter new age (leave blank to keep current): ")

            new_email = input("Enter new email (leave blank to keep current): ")

            new_mobile = input("Enter new mobile (leave blank to keep current): ")

            # Use old values if new values are empty

            age = int(new_age) if new_age.strip() else result[1]

            email = result[2]

            if new_email.strip():

                while not is_valid_email(new_email):
                    print("Invalid email format. Try again.")

                    new_email = input("Enter new email: ")

                email = new_email

            mobile = new_mobile.strip() if new_mobile.strip() else result[3]

            # Update in DB

            cursor.execute("UPDATE contacts SET age = ?, email = ?, mobile = ? WHERE name = ?",

                           (age, email, mobile, name))

            conn.commit()

            print(f"{name}'s contact updated successfully.")


        else:

            print("Contact not found.")


    elif choice == "4":
        name = input("Enter name to delete: ")
        cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        if cursor.rowcount:
            conn.commit()
            print(f"{name} deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("\nSearch by:")
        print("1. Name")
        print("2. Email")
        print("3. Mobile")
        print("4. Age")
        option = input("Choose option: ")
        value = input("Enter search value: ").strip().lower()

        if option == "1":
            cursor.execute("SELECT * FROM contacts WHERE LOWER(name) LIKE ?", (f"%{value}%",))
        elif option == "2":
            cursor.execute("SELECT * FROM contacts WHERE LOWER(email) LIKE ?", (f"%{value}%",))
        elif option == "3":
            cursor.execute("SELECT * FROM contacts WHERE mobile LIKE ?", (f"%{value}%",))
        elif option == "4":
            cursor.execute("SELECT * FROM contacts WHERE age = ?", (value,))
        else:
            print("Invalid option.")
            continue

        results = cursor.fetchall()
        if results:
            for c in results:
                print(f"\nName: {c[0]}\nAge: {c[1]}\nEmail: {c[2]}\nMobile: {c[3]}")
        else:
            print("No matching contacts found.")

    elif choice == "6":
        cursor.execute("SELECT COUNT(*) FROM contacts")
        total = cursor.fetchone()[0]
        print(f"\nTotal contacts: {total}")

    elif choice == "7":
        filename = "contacts_backup.csv"
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()

        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Email", "Mobile"])
            writer.writerows(contacts)

        print(f"\nContacts backed up to '{filename}'.")

    elif choice == "8":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from the menu.")

# Close the database connection
conn.close()
