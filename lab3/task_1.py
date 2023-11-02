import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class GreetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.name_input = None
        self.greet_button = None
        self.exit_button = None
        self.init_ui()

    def init_ui(self):
        # Создаем виджеты
        self.label = QLabel("Введите свое имя:")
        self.name_input = QLineEdit()
        self.greet_button = QPushButton("Hello")
        self.exit_button = QPushButton("Выход")

        # Добавление виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.greet_button)
        layout.addWidget(self.exit_button)

        # Функции-обработчики событий
        self.greet_button.clicked.connect(self.greet_user)
        self.exit_button.clicked.connect(self.close)

        # Макет для главного окна
        self.setLayout(layout)

        # Параметры окна
        self.setWindowTitle("Приветствие пользователя")
        self.setGeometry(100, 100, 400, 200)

    def greet_user(self):
        name = self.name_input.text()
        if name:
            greeting = f"Привет, {name}!"
        else:
            greeting = "Привет, аноним!"
        self.label.setText(greeting)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GreetApp()
    ex.show()
    sys.exit(app.exec())
