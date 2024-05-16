from PyQt6.QtWidgets import (
    QGridLayout,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLineEdit,
    QToolTip
)
from Global import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import QEvent


class MidPart(QGridLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_widgets()
        self.load_config()
        self.loading()

    def loading(self):
        # self.addWidget(self.textEdit, 0, 0)
        self.addWidget(self.lineEdit, 0, 1)

    def load_widgets(self):
        self.lineEdit = QLineEdit(self.parent())

    def load_config(self):
        pass


class TextEdit(QTextEdit):
    isRandOnly = True  # 进入编辑状态，初始化为只读， 点击编辑框进入编辑状态

    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.init()
        self.setReadOnly(self.isRandOnly)

    def init(self):
        self.load_config()
        self.load_event()

    def load_config(self):
        self.setStyleSheet("""
            background-color: #fff;
        """)
        self.setMaximumSize(500, 436)

    def load_event(self):
        self.textChanged.connect(self.SendText)

    def StartEdit(self):
        pass

    def EdnEdit(self):
        pass

    def SendText(self):
        print("HHHHHHH=========HHHHHHH")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.isRandOnly = not self.isRandOnly
            if self.isRandOnly:
                print("now, is only read")
            else:
                print("starting, edit")
            self.setReadOnly(self.isRandOnly)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Return:
            self.clear()

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key.Key_Enter and not self.isRandOnly:
            print("save text")


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
        self.setMaximumSize(200, 36)
