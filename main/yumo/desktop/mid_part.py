from PyQt6.QtWidgets import QGridLayout, QTextEdit, QPushButton


class MidPart(QGridLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_widgets()

    def load_widgets(self):
        self.textEdit = TextEdit(self.parent())
        self.addWidget(self.textEdit, *(0, 0))

        self.send = Button("send", self.parent())
        self.clear = Button("clear", self.parent())
        self.addWidget(self.send, *(0, 1))
        self.addWidget(self.clear, *(1, 1))

    def loadTextEdit(self):
        pass

    def loadButton(self):
        pass


class TextEdit(QTextEdit):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.init()

    def init(self):
        self.load_config()
        self.load_layout()

    def load_config(self):
        self.setStyleSheet("""
            background-color: #fff;
        """)
        self.resize(600, 600)

    def load_layout(self):
        pass


class ButtonBox:
    """
        按钮盒子？
    """

    def __init__(self):
        pass


class Button(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self.init()

    def init(self):
        self.load_config()

    def load_config(self):
        self.setStyleSheet("""
            background-color: #626262;
            color: #fff
        """)
