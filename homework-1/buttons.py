
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("Приклад QPushButton")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.times_pressed = 0

        self.name_label = QLabel("Не тисни на кнопку.", self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60, 30) 
            
        self.button = QPushButton("-_-", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """Handle when the button is clicked. 
        Demonstrates how to change text for widgets,
        update their sizes and locations, and how to
        close the window due to events."""
        self.times_pressed += 1

        if self.times_pressed == 1:
            self.name_label.setText("Не треба")
            self.button.move(10, 90)
        if self.times_pressed == 2:
            self.name_label.setText("не роби цього ")
            self.button.setText("-_-")
            self.button.adjustSize()
            self.button.move(160, 50)
        if self.times_pressed == 3:
            print("Я ж казав...")
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())