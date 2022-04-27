from widgets import Button, ProgressBar, GreenButton, GreenProgressBar
from .style import Style


class Green(Style):
    def create_button(self, parent=None) -> Button:
        return GreenButton(parent)

    def create_progress_bar(self, parent=None) -> ProgressBar:
        return GreenProgressBar(parent)
