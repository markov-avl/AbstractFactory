from widgets import Button, ProgressBar, RedButton, RedProgressBar
from .style import Style


class Red(Style):
    def create_button(self, parent=None) -> Button:
        return RedButton(parent)

    def create_progress_bar(self, parent=None) -> ProgressBar:
        return RedProgressBar(parent)
