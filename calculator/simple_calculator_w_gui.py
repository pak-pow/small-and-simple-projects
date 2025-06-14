import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()

        uic.loadUi("simple_calculator_w_gui.ui",self)

        self.show()

app = QApplication(sys.argv)
UIWindow = Calculator()
app.exec()