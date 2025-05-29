# ❌⭕ PyQt5 Tic Tac Toe

A simple GUI-based Tic Tac Toe game made with PyQt5. This project was designed to help understand GUI development in Python using `.ui` files and widget interaction.

---

## 🕹️ Features

- Clean interface using Qt Designer (`.ui` file)
- X and O turn-based system with dynamic label updates
- Reset button to clear the board and restart the game

---

## 🔧 Requirements

- Python 3.x
- PyQt5

To install PyQt5:

```bash
pip install PyQt5
```

---

## ▶️ How to Run

1. Make sure you have a file named `tic_tac_toe.ui` with the correct UI layout.
2. Save the script as `main.py`.
3. Run it using:

```bash
python main.py
```

---

## 📚 How It Works

- Buttons `pushButton_1` to `pushButton_9` represent the Tic Tac Toe grid.
- When clicked, the button marks either an "X" or "O" depending on the turn and disables itself.
- The label displays whose turn it is.
- Reset button re-enables all buttons and clears the board.

---

## 🔜 Coming Soon

Planned features to enhance the game:

- ✅ Scoreboard for Player 1 and Player 2
- ✅ Player name input and tracking
- ✅ Win detection logic and highlight
- ✅ Game menu with options like restart, quit, etc.
- ✅ Sound effects for clicks and wins
- ✅ Draw detection and proper endgame display

---

## 📄 License

This project is open-source. Feel free to modify or expand on it for learning or fun!
