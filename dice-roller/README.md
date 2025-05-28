# 🎲 Dice Roller

A simple terminal-based dice roller simulator written in Python. This program allows users to roll various types of dice like D4, D6, D10, D12, and D20—perfect for tabletop games or just having fun!

---

## 🎮 Features

- Supports 5 common dice types: D4, D6, D10, D12, D20
- Simulates a real-time rolling experience with delay
- Includes user input validation and play-again option

---

## 🛠️ Requirements

- Python 3.x

No additional libraries needed—just the built-in `random` and `time` modules.

---

## ▶️ How to Use

1. Save the script as `dice_roller.py`
2. Run it in your terminal:

```bash
python dice_roller.py
```

3. Choose a die by typing `D4`, `D6`, `D10`, `D12`, or `D20` when prompted.
4. The program will simulate rolling the selected die and display the result.

---

## 💡 Sample Output

```
==============================

    Welcome to Dice Roller!

==============================

            |DICES|
      |D4|D6|D10|D12|D20|

Dice: D6
You picked D6 with sides [1, 2, 3, 4, 5, 6]
Rolling...
You got... 4
--------------------------------------------
Would you like to try again (y/n)?: n
--------------------------------------------
Thanks for playing! Come Again!
```

---

## 📚 How It Works

- The `get_dice()` function returns a list of integers representing possible roll outcomes for each dice type.
- The program uses `random.choice()` to simulate rolling the dice.
- User input is validated to make sure only valid dice types are accepted.

---

## 📄 License

This project is free and open-source. Use it however you like!
