
# 🧮 Simple Calculator (CLI + GUI with PyQt5)

A lightweight calculator application featuring two interfaces:
- A command-line version using `lambda` expressions
- A GUI version built with **PyQt5** and a `.ui` file for interface design

---

## 📁 Project Structure

```
├── simple_calculator.py            # CLI version using lambda functions
├── simple_calculator_w_gui.py      # PyQt5 GUI logic
└── simple_calculator_w_gui.ui      # UI file created with Qt Designer
```

---

## 🖥️ CLI Version

### ➤ File: `simple_calculator.py`

- Prompts the user to enter a simple equation (e.g., `5 + 4`)
- Supports:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*` or `x`)
  - Division (`/`)
- Uses `lambda` functions in a dictionary for elegant operation mapping

### 🧪 Example:

```
Enter Equation: 7 / 2
3.50
```

---

## 🧰 GUI Version

### ➤ File: `simple_calculator_w_gui.py` + `simple_calculator_w_gui.ui`

- GUI powered by **PyQt5**
- `.ui` file is built using **Qt Designer**
- `simple_calculator_w_gui.py` loads the UI dynamically and displays the main window

### 🚀 How to Run

1. Make sure you have **PyQt5** installed:
   ```
   pip install PyQt5
   ```

2. Run the GUI script:
   ```
   python simple_calculator_w_gui.py
   ```

> ⚠️ The `.ui` file must be in the same directory as the `.py` file.

---

## 💡 Notes

- GUI functionality is still in development — logic buttons and calculation features will be added.
- CLI version is fully functional and handles basic math operations safely (e.g., division by zero).

---

## 📜 License

Free to use and extend. Ideal for beginners learning Python, PyQt, or UI design with Qt Designer.
