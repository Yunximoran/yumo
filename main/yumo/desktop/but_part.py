from PyQt6.QtWidgets import QVBoxLayout, QStatusBar, QSpacerItem

from PyQt6.QtCore import QEvent


# from PyQt6.QtGui import QColorSpace

class ButPart(QVBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_widgets()
        self.load_config()
        # self.addStretch(0)

    def load_widgets(self):
        self.statusBar = StatusBar(self.parent())
        self.addWidget(self.statusBar)

    def load_config(self):
        pass


class StatusBar(QStatusBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_config()

    def load_config(self):
        self.showMessage("YuMoStatus")
        self.setStyleSheet("""
            color: #333;
            border: 3px solid black;

            padding: 0;
            margin: 0;
        """)
        # border-radius: 36px;
