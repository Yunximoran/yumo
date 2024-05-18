import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QSize

from .widgets import *

APPLICATION = QApplication(sys.argv)
ACTION = {'exit': APPLICATION.instance().quit}


class MainPart(QVBoxLayout):
    def __init__(self, *args):
        super().__init__(*args)
        self.init()

    def init(self):
        self.load_layout()
        self.load_config()

    def load_layout(self):
        self.addLayout(TopPart(self.parent()), 0)
        self.addLayout(MidPart(self.parent()), 4)
        self.addLayout(ButPart(self.parent()), 0)

    def load_config(self):
        self.setContentsMargins(0, 0, 0, 0)


class TopPart(QHBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_widgets()
        self.load_config()
        self.loading()

    def loading(self):
        self.addWidget(self.menu)  # 把控件导入布局

    def load_widgets(self):
        self.menu = Menu(self.parent())

    def load_config(self):
        pass


class MidPart(QGridLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_widgets()
        self.load_event()
        self.load_config()
        self.loading()

    def loading(self):
        # self.addWidget(self.textEdit, 0, 0)
        self.addWidget(self.label, 0, 0)
        self.marge_widgets((1, 0), self.lineEdit, self.sendButton, isHoria=True)

    def load_widgets(self):
        """
            将所有空间添加进布局
        :return:
        """
        self.label = Label(self.parent())

        self.sendButton = QPushButton("send", self.parent())
        self.lineEdit = QLineEdit(self.parent())

    def marge_widgets(self, pos, *widgets, isHoria=True):
        if isHoria:
            childLayout = QHBoxLayout()
        else:
            childLayout = QVBoxLayout()
        for widget in widgets:
            childLayout.addWidget(widget)
        self.addLayout(childLayout, *pos)

    def load_event(self):
        self.sendButton.clicked.connect(self.__band_send_linedit)

    def __band_send_linedit(self):
        self.label.clear()
        text = self.lineEdit.text()
        self.lineEdit.clear()
        self.label.setText(text)

    def load_config(self):
        pass


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
