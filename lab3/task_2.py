import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QVBoxLayout, QWidget, QGroupBox, QSlider, \
    QGridLayout
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class GraphicsEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем меню
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

        # Добавление GroupBox'а "Выбор кисти" на панель инструментов
        brush_group = QGroupBox("Выбор кисти", self)
        brush_group.setCheckable(True)
        brush_group.setChecked(True)
        tools_panel.addWidget(brush_group)

        # Создание компонента QSlider для размера кисти
        brush_size_slider = QSlider(Qt.Orientation.Horizontal, self)
        brush_size_slider.setValue(10)
        brush_size_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        brush_size_slider.setTickInterval(5)
        brush_size_slider.setObjectName("brushSizeSlider")

        # Создание кнопок для выбора типа кисти
        brush1_button = QPushButton("Кисть 1", self)
        brush2_button = QPushButton("Кисть 2", self)
        brush3_button = QPushButton("Кисть 3", self)
        brush4_button = QPushButton("Кисть 4", self)

        # Создание компоновщика для кнопок выбора кисти
        brush_layout = QVBoxLayout()
        brush_layout.addWidget(brush1_button)
        brush_layout.addWidget(brush2_button)
        brush_layout.addWidget(brush3_button)
        brush_layout.addWidget(brush4_button)

        # Компоновщик для всей группы выбора кисти
        group_layout = QGridLayout()
        group_layout.addWidget(brush_size_slider, 0, 0, 1, 2)
        group_layout.addLayout(brush_layout, 1, 0, 1, 2)
        brush_group.setLayout(group_layout)

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
