import asyncio
import os
import sys

import aiofiles
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
        self.time_step_input = QLineEdit()
        self.directory_path_input.setPlaceholderText("Укажите путь")
        self.time_step_input.setPlaceholderText("Введите шаг сортировки (день, неделя, месяц")
        layout.addWidget(self.action_label)
        layout.addWidget(self.directory_path_input)
        layout.addWidget(self.time_step_input)

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
        self.sort_photos_button.clicked.connect(self.start_sort_photos_by_date)
        self.open_log_button.clicked.connect(self.open_log)

    async def find_and_remove_duplicates(self, directory_to_scan, log_file_path):
        result = await find_and_remove_duplicates(directory_to_scan, log_file_path)
        return result

    def start_find_and_remove_duplicates(self):
        directory_to_scan = self.directory_path_input.text()  # Получить путь из текстового поля

        if directory_to_scan:
            log_directory = os.path.join(directory_to_scan, "logs")  # Путь к директории для журнала
            os.makedirs(log_directory, exist_ok=True)  # Создание директории для журнала, если она не существует
            log_file_path = os.path.join(log_directory, "duplicate_log.txt")  # Формирование пути к файлу журнала

            # Запуск асинхронной функции find_and_remove_duplicates
            result = asyncio.run(self.find_and_remove_duplicates(directory_to_scan, log_file_path))

            if result:
                self.action_label.setText("Дубликаты найдены и удалены")
            else:
                self.action_label.setText("Дубликатов не найдено")
        else:
            self.action_label.setText("Укажите путь к папке")

    async def sort_photos_by_date(self, directory_to_sort, time_step, log_file_path):
        return sort_photos_by_date(directory_to_sort, time_step, log_file_path)

    def start_sort_photos_by_date(self):
        directory_to_sort = self.directory_path_input.text()
        time_step = self.time_step_input.text()
        log_directory = os.path.join(directory_to_sort, "logs")
        os.makedirs(log_directory, exist_ok=True)
        log_file_path = os.path.join(log_directory, "sort_log.txt")
        asyncio.run(self.sort_photos_by_date(directory_to_sort, time_step, log_file_path))

    def open_log(self):
        loop = asyncio.ProactorEventLoop()  # Задается цикл событий
        asyncio.set_event_loop(loop)  # Установка в качестве текущего
        loop.run_until_complete(self.open_log_async())

    async def open_log_async(self):
        directory = self.directory_path_input.text()
        dialog = QFileDialog()
        options = dialog.options()
        # Можно выбрать только txt файлы, _ здесь и в других местах - флаг успешного/отмененного действия
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
