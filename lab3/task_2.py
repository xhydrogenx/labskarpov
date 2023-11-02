import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QWidget
from PyQt6.QtGui import QAction


class GraphicsEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание меню
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        help_menu = menubar.addMenu("Справка")

        # Пункты меню
        new_action = QAction("Создать", self)
        save_action = QAction("Сохранить", self)
        open_action = QAction("Открыть", self)
        exit_action = QAction("Выход", self)

        file_menu.addAction(new_action)
        file_menu.addAction(save_action)
        file_menu.addAction(open_action)
        file_menu.addAction(exit_action)

        about_action = QAction("О программе", self)
        help_menu.addAction(about_action)

        # Создание панелей
        tools_panel = QToolBar("Панель инструментов")
        draw_panel = QWidget()

        # Свойства панелей
        tools_panel.setObjectName("toolsPanel")
        draw_panel.setObjectName("drawPanel")

        tools_panel.setMovable(False)

        self.addToolBar(tools_panel)
        self.setCentralWidget(draw_panel)

        # Добавление кнопок на панель инструментов
        brush_button = QPushButton("Кисть")
        color_button = QPushButton("Цвет")
        tools_panel.addWidget(brush_button)
        tools_panel.addWidget(color_button)

        # Функция-обработчик действий
        exit_action.triggered.connect(self.close)

        # Параметры окна
        self.setWindowTitle("Графический редактор")
        self.setGeometry(100, 100, 800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = GraphicsEditor()
    editor.show()
    sys.exit(app.exec())
