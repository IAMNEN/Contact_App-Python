# 📇 Contact App (Python)

A simple command-line contact management application written in Python.  
It allows users to create, read, update, and delete (CRUD) contact entries stored in a local file (e.g. JSON or CSV).

---

## 🔹 Features

- **Add new contacts**: Save full name, phone number, email, and notes.
- **List all contacts**: Display all saved contacts in a neat tabular format.
- **Search contacts**: Find contacts by name, phone, or email.
- **Update contacts**: Edit existing contact information.
- **Delete contacts**: Remove unwanted contacts.
- **Persistent storage**: Saves contacts in a file for persistence between runs.

---

## 💻 Technologies Used

- **Python 3.x**
- Built-in libraries: `argparse`, `json` (or `csv`), `os`, `sys`
- Optional: `tabulate` for formatted table display

---

## 🧭 Installation & Setup

1. **Clone the repository**  
git clone https://github.com/IAMNEN/Contact_App-Python.git
cd Contact_App-Python


2. *(Optional)* Create a virtual environment:  
python3 -m venv venv
source venv/bin/activate


3. **Install dependencies** (if any, e.g. `tabulate`):  
pip install -r requirements.txt

---

## 🚀 Usage

Run the main script with one of the supported commands:

```
python contact_app.py add        # Add a new contact
python contact_app.py list       # List all contacts
python contact_app.py search     # Search for specific contacts
python contact_app.py update     # Update an existing contact
python contact_app.py delete     # Remove a contact

Example – Adding a Contact
```
python contact_app.py add \
  --name "Jane Doe" \
  --phone "1234567890" \
  --email "jane.doe@example.com" \
  --notes "Friend from yoga class"
```
Example – Listing Contacts
python contact_app.py list
```

SQL

+----+----------+------------+----------------------+---------------------+
| ID | Name     | Phone      | Email                | Notes               |
+----+----------+------------+----------------------+---------------------+
| 1  | Jane Doe | 1234567890 | jane.doe@example.com | Friend from yoga...|
+----+----------+------------+----------------------+---------------------+

