from abc import abstractmethod

from PySide6.QtWidgets import QProgressBar


class ProgressBar(QProgressBar):
    width = 460
    height = 50

    @abstractmethod
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(self.width, self.height)
        self.setTextVisible(False)


class RedProgressBar(ProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('QProgressBar::chunk { background-color: red; }')


class GreenProgressBar(ProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('QProgressBar::chunk { background-color: green; }')


class BlueProgressBar(ProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('QProgressBar::chunk { background-color: blue; }')
