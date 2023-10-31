import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Проверка на високосный")
        self.setFixedSize(QSize(300, 150))

        # Создаем виджеты
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        label = QLabel("Введите год:", self)
        layout.addWidget(label)

        input_widget = QLineEdit(self)
        input_widget.setPlaceholderText('Введите год')
        layout.addWidget(input_widget)

        result_label = QLabel(self)
        layout.addWidget(result_label)

        button = QPushButton("Проверить", self)
        layout.addWidget(button)

        # Функция для проверки на високосный год и вывода результата
        def check_leap_year():
            year = input_widget.text()
            try:
                year = int(year)
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    result_label.setText(f"{year} - високосный год")
                else:
                    result_label.setText(f"{year} - не високосный год")
            except ValueError:
                result_label.setText("Некорректный ввод")

        button.clicked.connect(check_leap_year)

        central_widget.setLayout(layout)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
