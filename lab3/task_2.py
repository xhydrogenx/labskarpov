import math
import random
import sys

from PyQt6.QtCore import Qt, QRect, QSize, QPoint, QPointF
from PyQt6.QtGui import QAction, QImage, QPainter, QColor, QPen, QCursor, QBrush, QPolygon
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QWidget, QGroupBox, QSlider, \
    QComboBox, QHBoxLayout, QColorDialog


class GraphicsEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.drawing_area = None
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
        brush_size_slider.setGeometry(540, 35, 200, 45)
        brush_size_slider.valueChanged.connect(self.set_brush_size)

        # Компоновщик для кнопок выбора типа кисти
        brush_layout = QHBoxLayout()

        # Выпадающий список для выбора типа кисти
        brush_type_combo = QComboBox(self)
        brush_type_combo.addItem("Квадратная")
        brush_type_combo.addItem("Прямоугольная")
        brush_type_combo.addItem("Круглая")
        brush_type_combo.addItem("Треугольная")
        brush_type_combo.addItem("Звезда")
        brush_type_combo.addItem("Кардиоида")
        brush_type_combo.addItem("Ластик")

        brush_type_combo.currentIndexChanged.connect(self.set_brush_type)

        # Кнопка для очистки
        clear_button = QPushButton("Очистить", self)
        clear_button.clicked.connect(self.clear_drawing_area)

        color_button = QPushButton("Выбрать цвет", self)
        color_button.clicked.connect(self.open_color_dialog)

        # Добавление выпадающего список и кнопку в компоновщик
        brush_layout.addWidget(brush_type_combo)
        brush_layout.addWidget(clear_button)
        brush_layout.addWidget(brush_type_combo)
        brush_layout.addWidget(color_button)  # Добавляем кнопку выбора цвета
        brush_layout.addWidget(clear_button)

        # Геометрия компоновки
        brush_group.setLayout(brush_layout)
        brush_group.setGeometry(100, 100, 300, 100)

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

        # Ограничение области рисования
        drawing_width = 800
        drawing_height = 480
        x = (self.width() - drawing_width) // 2  # Центрирование по горизонтали
        y = self.height() - drawing_height  # Размещение снизу
        drawing_area = QRect(x, y, drawing_width, drawing_height)
        self.drawing_area = drawing_area

    def setCursorPos(self, pos):
        QCursor.setPos(pos)

    def set_brush_size(self, size):
        self.brush_size = size

    def set_brush_type(self, index):
        brush_types = ["Square", "Rectangle", "Circle", "Triangle", "Star", "Cardioid", "Eraser"]
        self.brush_type = brush_types[index]

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
            if self.drawing_area.contains(event.pos()):
                painter = QPainter(self.image)
                brush = QBrush()

                if self.brush_type == "Eraser":
                    pen = QPen()
                    pen.setColor(self.background_color)
                    eraser_rect = QRect(self.last_point, event.pos())
                    eraser_rect &= self.drawing_area
                    eraser_rect.setSize(QSize(self.brush_size, self.brush_size))
                    brush.setColor(self.background_color)
                    brush.setStyle(Qt.BrushStyle.SolidPattern)
                    painter.setPen(pen)
                    painter.setBrush(brush)
                    painter.drawRect(eraser_rect)

                else:
                    pen = QPen()
                    pen.setColor(self.brush_color)
                    brush.setColor(self.brush_color)
                    brush.setStyle(Qt.BrushStyle.SolidPattern)
                    painter.setPen(pen)
                    painter.setBrush(brush)

                if self.brush_type == "Square":
                    square_rect = QRect(self.last_point, event.pos())
                    square_rect &= self.drawing_area
                    square_rect.setSize(QSize(self.brush_size, self.brush_size))
                    painter.drawRect(square_rect)
                elif self.brush_type == "Rectangle":
                    rect_rect = QRect(self.last_point, event.pos())
                    rect_rect &= self.drawing_area
                    rect_rect.setSize(QSize((self.brush_size * 2), self.brush_size))
                    painter.drawRect(rect_rect)
                elif self.brush_type == "Circle":
                    circle_rect = QRect(self.last_point, event.pos())
                    circle_rect.setSize(QSize(self.brush_size, self.brush_size))
                    circle_rect &= self.drawing_area
                    painter.drawEllipse(circle_rect)
                elif self.brush_type == "Triangle":
                    triangle_points = [
                        QPoint(self.last_point),
                        QPoint(int(event.pos().x() - self.brush_size / 2), int(event.pos().y() + self.brush_size)),
                        QPoint(int(event.pos().x() + self.brush_size / 2), int(event.pos().y() + self.brush_size)),
                    ]
                    triangle_polygon = QPolygon(triangle_points)
                    drawing_polygon = QPolygon([
                        self.drawing_area.topLeft(),
                        self.drawing_area.topRight(),
                        self.drawing_area.bottomRight(),
                        self.drawing_area.bottomLeft()
                    ])

                    triangle_polygon = triangle_polygon.intersected(drawing_polygon)
                    painter.drawPolygon(triangle_polygon)
                elif self.brush_type == "Star":
                    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                    brush = QBrush(self.brush_color)

                    x, y = event.pos().x(), event.pos().y()
                    size = self.brush_size

                    outer_points = []
                    inner_points = []

                    for i in range(5):
                        outer_x = x + size * math.cos(i * 2 * math.pi / 5)
                        outer_y = y + size * math.sin(i * 2 * math.pi / 5)
                        outer_points.append(QPointF(outer_x, outer_y))

                        inner_x = x + size / 2 * math.cos((i * 2 + 1) * math.pi / 5)
                        inner_y = y + size / 2 * math.sin((i * 2 + 1) * math.pi / 5)
                        inner_points.append(QPointF(inner_x, inner_y))

                    for i in range(5):
                        painter.drawLine(outer_points[i], inner_points[i])
                        painter.drawLine(inner_points[i], outer_points[(i + 1) % 5])
                    painter.drawLine(outer_points[0], inner_points[0])
                    painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)

                elif self.brush_type == "Cardioid":

                    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
                    brush = QBrush(self.brush_color)
                    x, y = event.pos().x(), event.pos().y()
                    size = self.brush_size
                    cardioid_points = []
                    num_points = 100

                    for i in range(num_points):
                        t = 2 * math.pi * i / num_points

                        r = size * (1 - math.cos(t))

                        x_point = x + r * math.cos(t)

                        y_point = y + r * math.sin(t)

                        cardioid_points.append(QPointF(x_point, y_point))

                    for i in range(num_points):
                        painter.drawLine(cardioid_points[i], cardioid_points[(i + 1) % num_points])

                    painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)

                self.last_point = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def open_color_dialog(self):
        color = QColorDialog.getColor(self.brush_color, self)
        if color.isValid():
            self.brush_color = color


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = GraphicsEditor()
    editor.show()
    sys.exit(app.exec())
