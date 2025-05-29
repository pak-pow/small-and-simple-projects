from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel 
from PyQt5 import uic
import sys

class TicTacToe(QMainWindow):

    def __init__(self):
        super(TicTacToe, self).__init__()

        # load ui
        uic.loadUi("tic_tac_toe.ui", self)

        # define counter to see who's turn is it
        self.counter = 0

        # define button
        self.button =[]

        for i in range(1, 10):
            btn = self.findChild(QPushButton, f"pushButton_{i}")
            btn.clicked.connect(lambda _, b = btn: self.clicker(b))
            self.button.append(btn)

        self.reset_button = self.findChild(QPushButton, "reset_button")
        self.label = self.findChild(QLabel, "label")
        self.reset_button.clicked.connect(self.reset)

        self.show()

    def clicker(self, b: QPushButton) -> None:

        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")

        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False)

        self.counter += 1

    def reset(self):

        for b in self.button:
            b.setText("")
            b.setEnabled(True)

        self.label.setText("X Goes First")
        self.counter = 0

app = QApplication(sys.argv)
UIWindow = TicTacToe()
app.exec_()