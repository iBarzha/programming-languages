"""Listing 2-3 to Listing 2-7
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(50, 50, 250, 430)
        self.setWindowTitle("Профіль користувача")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create the labels to be displayed in the window."""
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Барджеєв Антон")
        user_label.setFont(QFont("Calibri", 20))
        user_label.move(30, 140)

        bio_title_label = QLabel(self)
        bio_title_label.setText("Навчання")
        bio_title_label.setFont(QFont("Calibri", 17))
        bio_title_label.move(15, 170)

        bio_text_label = QLabel(self)
        bio_text_label.setText("2 курс")

        bio_text_label.setWordWrap(True)
        bio_text_label.move(17, 175)
        bio_text_label.resize(280,60)

        bio_text_label = QLabel(self)
        bio_text_label.setText("ІСТ")

        bio_text_label.setWordWrap(True)
        bio_text_label.move(17, 190)
        bio_text_label.resize(280, 60)


        skills_label = QLabel(self)
        skills_label.setText("Основні Дисципліни")
        skills_label.setFont(QFont('Arial', 17))
        skills_label.move(15, 230)

        languages_label = QLabel(self)
        languages_label.setText(" Мови Програмування ")
        languages_label.move(15, 260)

        languages_label = QLabel(self)
        languages_label.setText("Алгоритми ")
        languages_label.move(20, 275)

        languages_label = QLabel(self)
        languages_label.setText(" Теорія Ймовірностей ")
        languages_label.move(15, 290)

        experience_label = QLabel(self)
        experience_label.setText("Майбутня професія")
        experience_label.setFont(QFont("Comic Sans MS", 17))
        experience_label.move(15, 310)

        developer_label = QLabel(self)
        developer_label.setText("Back-end developer")
        developer_label.setFont(QFont("Comic Sans MS", 10))
        developer_label.move(15, 340)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Знання декількох мов програмування")
        dev_dates_label.setFont(QFont("	Impact", 10))
        dev_dates_label.move(15, 360)

        driver_label = QLabel(self)
        driver_label.setText("Python | Ruby | C#")
        driver_label.setFont(QFont("Impact", 10))
        driver_label.move(15, 380)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Комунікабельність та гарні навички")
        driver_dates_label.setFont(QFont("	Impact", 10))
        driver_dates_label.move(15, 400)

    def createImageLabels(self):
        """Open image files and create image labels."""
        images = ["images/skyblue.png", 
                  "images/erro.png"]

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/erro.png":
                        label.move(100, 40)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")            

# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())