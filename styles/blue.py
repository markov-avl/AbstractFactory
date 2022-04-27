from widgets import Button, ProgressBar, BlueButton, BlueProgressBar
from .style import Style


class Blue(Style):
    def create_button(self, parent=None) -> Button:
        return BlueButton(parent)

    def create_progress_bar(self, parent=None) -> ProgressBar:
        return BlueProgressBar(parent)
