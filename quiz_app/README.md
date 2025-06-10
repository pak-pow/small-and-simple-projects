
# 🧠 Python Quiz Application

A simple terminal-based multiple-choice quiz game built in Python. Questions are stored and loaded from a CSV file, and the quiz randomizes both the questions and the options for a dynamic experience every time.

---

## 📁 Features

- ✅ Loads quiz questions from a CSV file (`questions.csv`)
- 📝 Automatically creates the CSV file if it doesn't exist
- 🔀 Randomizes question and answer order
- 🧠 Tracks and displays the final score
- 🚫 Handles invalid user inputs gracefully

---

## 📄 CSV Format

The quiz reads questions from a file called `questions.csv` with the following headers:

```
Question, Option A, Option B, Option C, Option D, Answer
```

### Example:
```csv
What is the capital of France?,Paris,Lyon,Marseille,Nice,Paris
```

---

## 🚀 How to Run

1. **Make sure you have Python installed** (Python 3.6+ recommended).
2. Open a terminal and run:

```bash
python quiz.py
```

- If the `questions.csv` file doesn't exist, it will be created.
- You'll then be quizzed on the questions in the file.

---

## 🧪 Sample Interaction

```
Q1: What is the capital of France?

    1. Marseille
    2. Paris
    3. Lyon
    4. Nice

Your Answer (1-4): 2
✅ Correct!
```

---

## 📌 Notes

- Add your questions to `questions.csv` using a spreadsheet editor or any CSV editor.
- The correct answer must match one of the provided options exactly.
- The app will automatically shuffle both questions and options each time.

---

## 📂 File Structure

```
quiz.py             # Main Python script
questions.csv       # Data source for quiz questions (auto-created if missing)
```

---

## 💡 Future Improvements (Optional Ideas)

- GUI using Tkinter or Kivy
- Category filters for questions
- Timed quiz feature
- Score saving and leaderboard

---

## 📜 License

This project is open-source and free to use.
