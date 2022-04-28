from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

from styles import Red, Green, Blue, Style
from widgets import Button, ProgressBar


class App(QMainWindow):
    # Настройки окна
    __x = 50
    __y = 75
    __width = 480
    __height = 320
    __name = 'Abstract Fabric Example'

    def __init__(self) -> None:
        super().__init__()
        self._main = QWidget()
        self._style_control = QWidget(self)
        self._change_to_red = Button()
        self._change_to_green = Button()
        self._change_to_blue = Button()
        self._button: Button | None = None
        self._progress_bar: ProgressBar | None = None
        self._timer = QtCore.QBasicTimer()
        self._step = 0
        self._init_ui()
        self.show()

    # Главная функция настройки интерфейса
    def _init_ui(self) -> None:
        self.setGeometry(self.__x, self.__y, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)
        self.setWindowTitle(self.__name)
        self._set_style_control()
        self._set_style(Red())
        self._set_main_layout()
        self.setCentralWidget(self._main)

    # Настройка панели контроля стиля
    def _set_style_control(self) -> None:
        self._change_to_red.setText("Change to RED")
        self._change_to_red.clicked.connect(lambda: self._set_style(Red()))
        self._change_to_green.setText("Change to GREEN")
        self._change_to_green.clicked.connect(lambda: self._set_style(Green()))
        self._change_to_blue.setText("Change to BLUE")
        self._change_to_blue.clicked.connect(lambda: self._set_style(Blue()))
        layout = QHBoxLayout()
        layout.addWidget(self._change_to_red)
        layout.addWidget(self._change_to_green)
        layout.addWidget(self._change_to_blue)
        layout.setAlignment(QtCore.Qt.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        self._style_control.setFixedSize(self.__width, Button.height)
        self._style_control.setLayout(layout)

    # Настройка главного макета
    def _set_main_layout(self) -> None:
        layout = QVBoxLayout()
        layout.addWidget(self._button, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self._progress_bar)
        layout.addWidget(self._style_control)
        self._main.setLayout(layout)

    # Используется для изменения стиля
    def _set_style(self, style: Style) -> None:
        old_button = self._button
        old_progress_bar = self._progress_bar
        self._button = style.create_button(self)
        self._button.clicked.connect(self._start_progress_bar)
        self._progress_bar = style.create_progress_bar(self)
        self._progress_bar.setValue(0 if old_progress_bar is None else old_progress_bar.value())
        if old_button and old_progress_bar:
            self._main.layout().replaceWidget(old_button, self._button)
            self._main.layout().replaceWidget(old_progress_bar, self._progress_bar)

    def _start_progress_bar(self) -> None:
        if self._timer.isActive():
            self._timer.stop()
        else:
            self._timer.start(100, self)

    def timerEvent(self, e):
        if self._step >= 100:
            self._timer.stop()
            self._step = 0
            return
        self._step += 5
        self._progress_bar.setValue(self._step)