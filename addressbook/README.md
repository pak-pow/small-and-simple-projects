# 📖 Address Book Management System (Console App)

A console-based Address Book system written in Python. It stores entries in a CSV file and allows users to create, list, and update contact information with a user-friendly flow and partial-name search support.

---

## 🧰 Features

- ✅ Add new address entries
- 📋 List all saved contacts in a formatted table
- ✏️ Update contact details by name (supports partial match)
- 🧹 CSV-backed persistent storage (`addressbook.csv`)
- 🧪 Input validation and error handling
- 🚧 Search and delete functions are scaffolded for future implementation

---

## 🧱 CSV Structure

Stored in a file called `addressbook.csv` with the following fields:

```
Name, Gender, Age, City, Street, Phone Number
```

---

## 🧪 Sample Run

```
1.) Create Address
2.) Read / List All Address
3.) Update Address By Name
4.) Delete Address By Name
5.) Search Address By Location
6.) Exit

Enter choice: 1
Enter Name: Juan Dela Cruz
Enter Gender: Male
Enter Age: 27
Enter City: Manila
Enter Street: Rizal Ave
Enter Phone Number: 09171234567

Would you like to try again? (Y/N): y
```

---

## 📦 How It Works

- The system initializes `addressbook.csv` on first run if it doesn't exist.
- When updating, the user can input **partial names** and select from a list of matches.
- Records are saved and modified directly in the CSV file.

---

## 🔜 In Development

- GUI or web-based interface (future enhancement)

---

## 🐍 How to Run

Make sure Python is installed, then run:

```
python adressbook.py
```

> Note: Ensure you’re in the correct directory containing `adressbook.py`.

---

## 📜 License

Open-source and free to use for learning, small projects, or extensions.
