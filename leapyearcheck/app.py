import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)

        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

#     checked - состояние кнопки когда она зажата


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# def year_check():
#     # берем строку по ключу и преобразуем в число
#     year =
#     leap = 'Високосный'
#     regular = 'Обычный'
#
#     # 2 условия
#     if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
#         print(leap)
#     else:
#         print(regular)
