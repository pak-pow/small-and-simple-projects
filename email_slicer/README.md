
# ✉️ Email Slicer (Python)

A simple command-line tool to split an email address into its username and domain components using basic Python string operations.

---

## 📁 Project Structure

```
├── email_slicer.py         # Main script
├── requirements.txt        # (Optional) Dependencies
└── samples/                # (Optional) Sample inputs/outputs directory
    └── sample_emails.txt
```

---

## 🚀 Features

- ✅ Prompts the user to enter an email address.
- 🔍 Validates that the input contains an `@` symbol.
- ✂️ Uses string slicing to separate the username (before `@`) and domain (after `@`).
- 🚫 Handles invalid inputs gracefully with an error message.
- 📝 Easy to read and extend.

---

## 💻 How to Run

1. **Clone the repository** (or download the script):

```bash
git clone https://github.com/pak-pow/small-and-simple-projects.git
cd small-and-simple-projects/email_slicer
```

2. **Ensure you have Python 3 installed**.

3. **Run the script**:

```bash
python email_slicer.py
```

---

## 🧪 Sample Interaction

```
Enter your email address:   alice.smith@example.com
Your username is: alice.smith
Your domain is: example.com
```

If the input does not contain `@`, the script will display:

```
Invalid email address. Please include an '@' symbol.
```

---

## 🛠️ How It Works

1. The script reads the email input and strips whitespace.
2. It checks if an `@` symbol is present.
3. It finds the index of `@` and slices the string:
   - `username = email[:email.index("@")]`
   - `domain = email[email.index("@") + 1:]`
4. Displays the results to the user.

---

## 🚧 Future Enhancements

- 📜 Add unit tests for edge cases.
- 🏷️ Batch processing: read multiple emails from a file.
- 🖼️ Build a GUI version (e.g., with Tkinter or PyQt).
- 🛡️ Validate domain format (e.g., via regular expressions).

---

## 📜 License

Open-source and free to use for learning, small projects, or extensions.
