import sys
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit, QApplication

from lab8.lab_8 import result_trap, result_rect


class GreetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label_rect = None
        self.label_trapezoid = None
        self.name_input = None
        self.more_info_button = None
        self.exit_button = None
        self.new_window = None  # Добавляем новое окно как атрибут
        self.init_ui()

    def init_ui(self):
        self.label_rect = QLabel(f"Результат интегрирования методом прямоугольников: {result_rect[0]:.4f}")
        self.label_trapezoid = QLabel(f"Результат интегрирования методом трапеций: {result_trap[0]:.4f}")
        self.more_info_button = QPushButton("Результат для каждого этапа")
        self.exit_button = QPushButton("Выход")

        layout = QVBoxLayout()
        layout.addWidget(self.label_rect)
        layout.addWidget(self.label_trapezoid)
        layout.addWidget(self.more_info_button)
        layout.addWidget(self.exit_button)

        self.more_info_button.clicked.connect(self.show_more_info)
        self.exit_button.clicked.connect(self.close)

        # Макет для главного окна
        self.setLayout(layout)

        # Параметры окна
        self.setWindowTitle("Вычисление интеграла")
        self.setGeometry(100, 100, 400, 200)

    def show_more_info(self):
        if self.new_window is None:
            self.new_window = QWidget()

            self.new_window.setWindowTitle("Результат для каждого этапа")
            self.new_window.setGeometry(100, 100, 400, 600)

            self.new_window.layout = QVBoxLayout()
            text_edit = QTextEdit()

            formatted_result = ""
            for pair in result_rect[1:]:
                formatted_result += f"Метод прямоугольников:\n {pair}\n"

            for pair in result_trap[1:]:
                formatted_result += f"Метод трапеций:\n {pair}\n"

            text_edit.setPlainText(formatted_result)

            self.new_window.layout.addWidget(text_edit)
            self.new_window.setLayout(self.new_window.layout)

            self.new_window.show()
            self.new_window.activateWindow()
        else:
            self.new_window.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GreetApp()
    ex.show()
    sys.exit(app.exec())
