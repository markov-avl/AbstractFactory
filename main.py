import sys

from PySide6.QtWidgets import QApplication

from windows import App


if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = App()
    sys.exit(app.exec())
