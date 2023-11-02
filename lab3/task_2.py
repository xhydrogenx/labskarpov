import sys
from PyQt6.QtCore import Qt, QRect, QSize
from PyQt6.QtGui import QAction, QImage, QPainter, QColor, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QVBoxLayout, QWidget, QGroupBox, QSlider


class GraphicsEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.background_color = QColor(Qt.GlobalColor.white)
        self.brush_color = QColor(Qt.GlobalColor.red)
        self.brush_type = "Square"
        self.brush_size = 10

        self.drawing = False
        self.last_point = None
        self.image = None

        # Создаем меню
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        help_menu = menubar.addMenu("Справка")

        # Пункты меню
        new_action = QAction("Создать", self)
        new_action.triggered.connect(self.initialize_drawing_area)
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
        brush_size_slider.setRange(1, 100)
        brush_size_slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        brush_size_slider.setTickInterval(1)
        brush_size_slider.setObjectName("brushSizeSlider")
        brush_size_slider.valueChanged.connect(self.set_brush_size)

        # Кнопки для выбора типа кисти
        square_brush_button = QPushButton("Квадратная", self)
        square_brush_button.clicked.connect(lambda: self.set_brush_type("Square"))
        rectangular_brush_button = QPushButton("Прямоугольная", self)
        rectangular_brush_button.clicked.connect(lambda: self.set_brush_type("Rectangle"))
        circular_brush_button = QPushButton("Круглая", self)
        circular_brush_button.clicked.connect(lambda: self.set_brush_type("Circle"))

        # Кнопка для очистки
        clear_button = QPushButton("Очистить", self)
        clear_button.clicked.connect(self.clear_drawing_area)

        # Компоновщик для кнопок выбора кисти и кнопки очистки
        brush_layout = QVBoxLayout()
        brush_layout.addWidget(square_brush_button)
        brush_layout.addWidget(rectangular_brush_button)
        brush_layout.addWidget(circular_brush_button)
        brush_layout.addWidget(clear_button)

        # Компоновщик для всей группы выбора кисти
        group_layout = QVBoxLayout()
        group_layout.addWidget(brush_size_slider)
        group_layout.addLayout(brush_layout)
        brush_group.setLayout(group_layout)

        # Функция-обработчик действий
        exit_action.triggered.connect(self.close)

        # Параметры окна
        self.setWindowTitle("Графический редактор")
        self.setGeometry(100, 100, 800, 600)

        # Инициализация области рисования
        self.initialize_drawing_area()

    def initialize_drawing_area(self):
        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(self.background_color)
        self.drawing = False

    def set_brush_size(self, size):
        self.brush_size = size

    def set_brush_type(self, brush_type):
        self.brush_type = brush_type

    def clear_drawing_area(self):
        self.image.fill(self.background_color)
        self.update()

    def paintEvent(self, event):
        if self.image:
            painter = QPainter(self)
            painter.drawImage(event.rect(), self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_point = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.MouseButton.LeftButton and self.drawing:
            painter = QPainter(self.image)
            pen = QPen()
            pen.setColor(self.brush_color)
            pen.setWidth(self.brush_size)
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            painter.setPen(pen)

            if self.brush_type == "Square":
                square_rect = QRect(self.last_point, event.pos())
                painter.drawRect(square_rect)
            elif self.brush_type == "Rectangle":
                painter.drawLine(self.last_point, event.pos())
            elif self.brush_type == "Circle":
                circle_rect = QRect(self.last_point, event.pos())
                circle_rect.setSize(QSize(self.brush_size, self.brush_size))
                painter.drawEllipse(circle_rect)

            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = GraphicsEditor()
    editor.show()
    sys.exit(app.exec())
