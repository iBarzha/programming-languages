# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, 
    QLabel, QLineEdit, QPushButton)
from PyQt6.QtCore import Qt

class MainWindow(QWidget): 

    def __init__(self): 
        super().__init__() 
        self.initializeUI() 

    def initializeUI(self):
        self.setMaximumSize(310, 180)
        self.setWindowTitle("Приклад QLineEdit")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        QLabel("Введіть текст у полі нижче.",
               self).move(70, 10)
        num1_label = QLabel("Число 1:", self)
        num1_label.move(20, 50)
        self.num1_edit = QLineEdit(self)
        self.num1_edit.resize(210, 20)
        self.num1_edit.move(70, 50)

        # Label та поле для вводу другого числа
        num2_label = QLabel("Число 2:", self)
        num2_label.move(20, 80)
        self.num2_edit = QLineEdit(self)
        self.num2_edit.resize(210, 20)
        self.num2_edit.move(70, 80)

        # Label для виведення суми
        sum_label = QLabel("", self)
        sum_label.move(20, 140)

        # Кнопки очищення та відправлення
        clear_button = QPushButton("Очистити", self)
        clear_button.move(140, 110)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton("OK", self)
        accept_button.move(210, 110)
        accept_button.clicked.connect(lambda: self.showSum(self.findChild(QLabel, "")))

    def clearText(self):
        self.num1_edit.clear()
        self.num2_edit.clear()

    def showSum(self, sum_label):
        """Calculate and show the sum of the inputted numbers."""
        try:
            num1 = float(self.num1_edit.text())
            num2 = float(self.num2_edit.text())
            total = num1 + num2
            sum_label.setText(f"Сума: {total:.2f}")
        except ValueError:
            sum_label.setText("Введені дані не є числами!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())