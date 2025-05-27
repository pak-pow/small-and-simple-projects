# ✊🧻✂️ Rock, Paper, Scissors Game

A simple and fun terminal-based **Rock, Paper, Scissors** game written in Python. Test your luck and skill against the computer!

---

## 🎮 Game Features

- Classic Rock, Paper, Scissors gameplay
- 3 lives per game session
- Tracks and displays your score
- Automatically ends the game when you run out of lives
- Option to play again after game over

---

## 🛠️ Requirements

- Python 3.x

No external libraries are required—just built-in Python modules.

---

## ▶️ How to Play

1. Save the script as `rock_paper_scissors.py`
2. Run the game in your terminal:

```bash
python rock_paper_scissors.py
```

3. Follow the prompts:
   - Enter one of the following choices: `rock`, `paper`, or `scissors`
   - The game compares your choice to the computer's random choice
   - You either win, lose, or draw
   - You start with 3 lives—each loss reduces a life, and each win increases your score

---

## 💡 Sample Output

```
    Welcome to Rock, Paper, Scissors Game!
================================================
            |ROCK|PAPER|SCISSORS|

------------------------------------------------
Remaining Life: 3 | Score: 0
Please enter your choice: rock
------------------------------------------------
Result: YOU WON! your choice: rock, computer choice: scissors
------------------------------------------------
Remaining Life: 3 | Score: 1
Please enter your choice: paper
------------------------------------------------
Result: YOU LOSE! your choice: paper, computer choice: scissors
================================================

Game Over! You've run out of lives | SCORE: 3

================================================
Would you like to try again?(y/n):
```

---

## 📚 How It Works

- Uses `random.choice()` to simulate the computer's choice
- Implements basic game logic in `game_function()` to determine the outcome
- Main game loop tracks lives and score, and restarts based on user input

---

## 📄 License

This project is open source and free to use.
