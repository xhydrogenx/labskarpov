from PyQt6.QtWidgets import QApplication, QWidget

import sys

# Разрешает аргументы командной строки для приложения
app = QApplication(sys.argv)

# Создание виджета
window = QWidget()
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
