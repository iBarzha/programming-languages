import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, 
    QLabel)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.checked_boxes = set()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle("QCheckBox Example")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        header_label = QLabel("У який час Вам краще працювати? \
                              (Відмітьте потрібні інтервали)", self)
        header_label.setWordWrap(True)
        header_label.move(20, 10)

        # Set up the checkboxes
        morning_cb = QCheckBox("Ранок [8:00-14:00]", self)
        morning_cb.move(40, 60)
        morning_cb.toggled.connect(self.update_checked_boxes)

        after_cb = QCheckBox("День [13:00-20:00]", self)
        after_cb.move(40, 80)
        after_cb.toggled.connect(self.update_checked_boxes)

        night_cb = QCheckBox("Ніч [19:00-03:00]", self)
        night_cb.move(40, 100)
        night_cb.toggled.connect(self.update_checked_boxes)

    def update_checked_boxes(self, checked):
        """Update the set of checked boxes."""
        sender = self.sender()
        if checked:
            self.checked_boxes.add(sender.text())
        else:
            self.checked_boxes.discard(sender.text())

    def closeEvent(self, event):
        """Handle the close event."""
        if len(self.checked_boxes) == 3:
            print("О, Ви - трудоголік!")
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())