# 🔐 Password Generator

A simple and interactive command-line password generator written in Python. Customize your password by choosing its length and whether to include letters, digits, and special characters.

---

## 📋 Features

- Generate secure, random passwords
- Choose password length
- Optional inclusion of:
  - Letters (A-Z, a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&*, etc.)
- Easy-to-use command-line interface
- Built using Python’s `secrets` module for cryptographically secure passwords

---

## 🛠️ Requirements

- Python 3.x (Recommended: 3.6 or later)

No third-party libraries are needed—only built-in modules are used.

---

## ▶️ How to Use

1. **Clone or download** this repository.
2. **Run the script**:

```bash
python password_generator.py
```

3. **Follow the prompts**:
   - Enter your desired password length.
   - Choose whether to include:
     - Letters
     - Digits
     - Special characters
   - View your generated password!

---

## 💡 Example Output

```
  Welcome to Password Generator!
----------------------------------------
Enter Password Length: 12
Include Letters? (y/n): y
Include Digits? (y/n): y
Include Symbols? (y/n): y
========================================
Generated Password: 8@wZfP1&dL$g
========================================

  Would you like to try again?(y/n): n

  Thank you for using this program!
----------------------------------------
```

---

## 🧠 How It Works

- Uses `secrets.choice()` for secure random character selection.
- Builds a character pool based on user preferences.
- Generates a password by randomly selecting characters from the pool.

---

## 📄 License

This project is open source and free to use.
