from PySide6 import QtCore
from PySide6.QtCore import QTimerEvent
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

from styles import Red, Green, Blue, Style
from widgets import Button


class App(QMainWindow):
    # Настройки окна
    __x = 50
    __y = 75
    __width = 480
    __height = 640
    __name = 'Abstract Fabric Example'
    __layout = QHBoxLayout()

    def __init__(self) -> None:
        super().__init__()
        self._main = QWidget()
        self._style_control = QWidget(self)
        self._change_to_red = Button()
        self._change_to_green = Button()
        self._change_to_blue = Button()
        self._blocks = list()
        self._init_ui()
        self.show()

    # Главная функция настройки интерфейса
    def _init_ui(self) -> None:
        self.setGeometry(self.__x, self.__y, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)
        self.setWindowTitle(self.__name)
        self._set_style_control()
        self._set_main_layout()
        self.setCentralWidget(self._main)

    # Настройка панели контроля стиля
    def _set_style_control(self) -> None:
        self._change_to_red.setText("Add RED")
        self._change_to_red.clicked.connect(lambda: self._add_styled_widgets(Red()))
        self._change_to_green.setText("Add GREEN")
        self._change_to_green.clicked.connect(lambda: self._add_styled_widgets(Green()))
        self._change_to_blue.setText("Add BLUE")
        self._change_to_blue.clicked.connect(lambda: self._add_styled_widgets(Blue()))
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
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(self._style_control)
        self._main.setLayout(self.__layout)

    # # Используется для добавления виджетов одного стиля
    def _add_styled_widgets(self, style: Style) -> None:
        timer = QtCore.QBasicTimer()
        button = style.create_button()
        progressbar = style.create_progress_bar()
        block = {
            'button': button,
            'progressbar': progressbar,
            'timer': timer,
            'steps': 0,
            'is_active': False
        }
        self._blocks.append(block)
        button.clicked.connect(lambda: self._start_progress_bar(block))
        self.__layout.insertWidget(self.__layout.count() - 1, button, alignment=QtCore.Qt.AlignCenter)
        self.__layout.insertWidget(self.__layout.count() - 1, progressbar)

    def _start_progress_bar(self, block: dict) -> None:
        block['timer'].start(100, self)
        block['is_active'] = True

    def timerEvent(self, e: QTimerEvent):
        for block in self._blocks:
            if block['is_active']:
                if block['steps'] >= 100:
                    block['timer'].stop()
                    block['is_active'] = False
                    block['steps'] = 0
                    block['progressbar'].setValue(0)
                else:
                    block['steps'] += 5
                    block['progressbar'].setValue(block['steps'])
