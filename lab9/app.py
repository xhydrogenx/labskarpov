import sys
import asyncio
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from module_1 import find_and_remove_duplicates
from module_2 import sort_photos_by_date

class PhotoOrganizerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.find_duplicates_button = QPushButton("Найти дубликаты")
        self.sort_photos_button = QPushButton("Сортировать фотографии")

        layout.addWidget(self.find_duplicates_button)
        layout.addWidget(self.sort_photos_button)

        self.setWindowTitle("Сортировщик фотографий")
        self.setGeometry(100, 100, 400, 200)

        self.find_duplicates_button.clicked.connect(self.start_find_and_remove_duplicates)
        self.sort_photos_button.clicked.connect(self.sort_photos_by_date)

    async def find_and_remove_duplicates(self):

        directory_to_scan = "C:/Users/hydrogen/PycharmProjects/labskarpov/test"
        await find_and_remove_duplicates(directory_to_scan)

    def start_find_and_remove_duplicates(self):
        asyncio.run(self.find_and_remove_duplicates())

    def sort_photos_by_date(self):
        directory_to_sort = "C:/Users/hydrogen/PycharmProjects/labskarpov/test"
        sort_photos_by_date(directory_to_sort)

if __name__ == '__main__':
    app = QApplication([])
    window = PhotoOrganizerApp()
    window.show()

    sys.exit(app.exec())
