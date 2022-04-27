from abc import abstractmethod

from PySide6.QtWidgets import QPushButton


class Button(QPushButton):
    width = 150
    height = 50

    @abstractmethod
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(self.width, self.height)


class RedButton(Button):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: red;")


class GreenButton(Button):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: green;")


class BlueButton(Button):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: blue;")
