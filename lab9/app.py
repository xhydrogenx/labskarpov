import os
import sys
import asyncio

import aiofiles
from PyQt6.QtCore import QEventLoop
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog
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

        self.action_label = QLabel("Введите путь до папки")
        self.directory_path_input = QLineEdit()
        layout.addWidget(self.action_label)
        layout.addWidget(self.directory_path_input)

        # self.input_label = Q

        self.find_duplicates_button = QPushButton("Найти дубликаты")
        self.sort_photos_button = QPushButton("Сортировать фотографии")
        self.open_log_button = QPushButton("Открыть лог")

        layout.addWidget(self.find_duplicates_button)
        layout.addWidget(self.sort_photos_button)
        layout.addWidget(self.open_log_button)

        self.setWindowTitle("Сортировщик фотографий")
        self.setGeometry(100, 100, 400, 200)

        self.find_duplicates_button.clicked.connect(self.start_find_and_remove_duplicates)
        self.sort_photos_button.clicked.connect(self.sort_photos_by_date)
        self.open_log_button.clicked.connect(self.open_log)

    async def find_and_remove_duplicates(self, directory_to_scan, log_file_path):
        result = await find_and_remove_duplicates(directory_to_scan, log_file_path)
        return result

    def start_find_and_remove_duplicates(self):
        directory_to_scan = self.directory_path_input.text()  # Получить путь из текстового поля
        if directory_to_scan:
            log_directory = os.path.join(directory_to_scan, "logs")
            os.makedirs(log_directory, exist_ok=True)
            log_file_path = os.path.join(log_directory, "duplicate_log.txt")
            result = asyncio.run(self.find_and_remove_duplicates(directory_to_scan, log_file_path))
            if result:
                self.action_label.setText("Дубликаты найдены и удалены")
            else:
                self.action_label.setText("Дубликатов не найдено")
        else:
            self.action_label.setText("Укажите путь к папке")

    def sort_photos_by_date(self):
        directory_to_sort = "C:/Users/hydrogen/PycharmProjects/labskarpov/test"
        sort_photos_by_date(directory_to_sort)

    def open_log(self):
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.open_log_async())

    async def open_log_async(self):
        directory = self.directory_path_input.text()  # Получить путь из текстового поля
        dialog = QFileDialog()
        options = dialog.options()
        fileName, _ = dialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", directory,
                                             "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            async with aiofiles.open(fileName, mode='r') as f:
                contents = await f.read()
            print(contents)


if __name__ == '__main__':
    app = QApplication([])
    window = PhotoOrganizerApp()
    window.show()

    sys.exit(app.exec())
