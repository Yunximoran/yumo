from PyQt6.QtWidgets import QPushButton, QCheckBox
from PyQt6.QtGui import QPalette

__DISPLAY_CONFIG = """
    background-color: #333;
"""


class Button(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)

        self.init()

    def init(self):
        self.load_config()

    def load_config(self):
        pass


class CheckBox(QCheckBox):
    def __init__(self, *args):
        super().__init__(*args)
        self.init()

    def init(self):
        self.load_config()

    def load_config(self):
        pass


def load_hello():
    print("hello world")
