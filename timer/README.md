# ⏰ PyQt5 Alarm Countdown Timer

A simple desktop alarm countdown timer built using **Python** and **PyQt5**. Set a short timer (10 seconds, 30 seconds, 1 minute, or 2 minutes), and the app will count down and play an alarm sound when time is up.

---

## 📸 Preview

> GUI consists of:
- A digital label showing the time remaining
- Four preset timer buttons
- Alarm plays when timer reaches zero

---

## 🛠 Features

- Graphical interface made with **Qt Designer** (`.ui` file)
- Preset timers: 10s, 30s, 1 min, 2 min
- Countdown updates in real-time
- Audio alarm plays when finished
- Simple and easy to use

---

## 📁 Project Structure

```
📦 timer/
├── alarmClock.py         # Main Python application
├── timer.ui              # PyQt5 UI file (created in Qt Designer)
├── alarm_wake_up.mp3     # Alarm sound played when time ends
└── README.md             # Project documentation (this file)
```

---

## 🚀 How to Run


### 1. Install Dependencies
Make sure you have Python 3 installed.

```

pip install PyQt5, playsound3

```

### 2. Run the App
```

python alarmClock.py

```

---

## 📦 Dependencies

- [PyQt5](https://pypi.org/project/PyQt5/)
- [playsound3](https://pypi.org/project/playsound3/)

You can install them with:

```

pip install PyQt5, playsound3

```
---

## 🎵 Customizing the Alarm Sound

To use your own alarm:
1. Replace `alarm_wake_up.mp3` with your own `.mp3` file
2. Make sure the filename and extension match in `alarmClock.py`

---

## 🧠 How It Works

- When a button is clicked, a countdown timer is set.
- A `QTimer` triggers every second to update the label.
- When the countdown ends, an MP3 file is played using `playsound`.

---

## 🧑‍💻 Author

Created by **Vee**

---

## 📜 License

This project is open-source and free to use. 
