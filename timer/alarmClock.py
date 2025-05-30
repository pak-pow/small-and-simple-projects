from playsound3 import playsound
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import sys


class Clock(QMainWindow):

    def __init__(self):
        super(Clock, self).__init__()

        uic.loadUi("timer.ui", self)

        self.btn_10_sec = self.findChild(QPushButton, "ten_sec_button")
        self.btn_30_sec = self.findChild(QPushButton, "thirty_sec_button")
        self.btn_1_min = self.findChild(QPushButton, "oneMinute_button")
        self.btn_2_min = self.findChild(QPushButton, "twoMinute_button")

        self.counter = self.findChild(QLabel, "label")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.btn_10_sec.clicked.connect(lambda: self.start_timer(10))
        self.btn_30_sec.clicked.connect(lambda: self.start_timer(30))
        self.btn_1_min.clicked.connect(lambda: self.start_timer(60))
        self.btn_2_min.clicked.connect(lambda: self.start_timer(120))

        self.show()

    def start_timer(self, seconds):

        self.time_left = seconds
        self.update_label()
        self.timer.start(1000)

    def update_timer(self):

        if self.time_left > 0:
            self.time_left -= 1
            self.update_label()

        else:
            self.timer.stop()
            playsound("alarm_wake_up.mp3")

    def update_label(self):

        mins = self.time_left // 60
        secs = self.time_left % 60

        self.counter.setText(f"{mins:02d}:{secs:02d}")

app = QApplication(sys.argv)
UIWindow = Clock()
app.exec_()

