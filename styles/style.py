from abc import ABC, abstractmethod

from widgets import Button, ProgressBar


class Style(ABC):
    @abstractmethod
    def create_button(self, parent=None) -> Button:
        ...

    @abstractmethod
    def create_progress_bar(self, parent=None) -> ProgressBar:
        ...
