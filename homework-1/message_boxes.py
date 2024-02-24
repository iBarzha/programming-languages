# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
    QMessageBox, QLineEdit, QPushButton)
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setGeometry(100, 100, 340, 140)
        self.setWindowTitle("Приклад QMessageBox")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        catalogue_label = QLabel("Каталог авторів", self)
        catalogue_label.move(100, 10)
        catalogue_label.setFont(QFont("Arial", 18))

        search_label = QLabel("Пошук автора у каталозі:", self)
        search_label.move(20, 40)

        # Create name QLabel and QLineEdit widgets
        author_label = QLabel("Ім'я та прізвище:", self)
        author_label.move(20, 74)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(130, 70)
        self.author_edit.resize(180, 24)
        self.author_edit.setPlaceholderText(
            "Введіть ім'я та прізвище")

        # Create search QPushButton
        search_button = QPushButton("Шукати", self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthors)

    def searchAuthors(self):
        """Search through catalogue of names.
        If name is found, display Author Found dialog.
        Otherwise, display Author Not Found dialog."""
        file = "files/authors.txt"

        try:
            with open(file, "r") as f:
                authors = [line.rstrip("\n") for line in f]

            # Check for name in authors list
            search_name = self.author_edit.text().lower()
            results = [author for author in authors if search_name in author.lower()]

            if results:
                QMessageBox.information(self, "Авторів знайдено",
                                        f"Ура! Знайдено {len(results)} авторів:\n\n{', '.join(results)}",
                                        QMessageBox.StandardButton.Ok)
            else:
                answer = QMessageBox.question(self, "Відсутні автори!",
                                              """<p>Авторів не знайдено у каталозі.</p>
                                              <p>Будете продовжувати?</p>""",
                                              QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                              QMessageBox.StandardButton.Yes)

                if answer == QMessageBox.StandardButton.No:
                    print("Closing application.")
                    self.close()
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Помилка!",
                                f"""<p><b>File not found.</b></p> 
                <p>Error: {error}</p>
                <p><i>Closing application</i>.""",
                                QMessageBox.StandardButton.Cancel)
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())