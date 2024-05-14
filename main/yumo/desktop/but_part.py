from PyQt6.QtWidgets import QVBoxLayout, QStatusBar


class ButPart(QVBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)

    def init(self):
        self.load_widgets()
        self.load_config()

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
        self.setWindowTitle("window")
