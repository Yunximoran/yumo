import sys

from PyQt6.QtWidgets import QVBoxLayout, QMenu, QMenuBar
from PyQt6.QtGui import QAction

from Global import *


class TopPart(QVBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.init()

    def init(self):
        self.load_widgets()
        self.load_config()
        self.loading()

    def loading(self):
        self.addWidget(self.menu)
        pass

    def load_widgets(self):
        self.menu = Menu(self.parent())
        # self.addWidget(self.menu)
        pass

    def load_config(self):
        self.setMenuBar(self.menu)
        pass


class Menu(QMenuBar):
    MENU = {
        "file": {
            "file attribute": {
                # message, actObj, func
                "encode": None,
                "add BOM": None,
            },
            "restruct": None
        },
        "edit": {
            "copy": None
        },
        'exit': (QApplication.instance().quit, "Ctrl+Q")
    }

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setParent(parent)
        self.init()

    def init(self):
        self.__init(self.MENU, self)
        self.load_config()

    def __init(self, struct, parent):
        for nextNode in struct:
            nextElem = struct[nextNode]
            if isinstance(nextElem, dict):
                childMenu = QMenu(nextNode, parent)
                parent.addMenu(childMenu)
                self.__init(nextElem, childMenu)
            else:
                childAct = QAction(nextNode, parent)
                parent.addAction(childAct)
                if nextElem is not None:
                    self.bandEvent(childAct, nextElem)

    def load_config(self):
        self.setStyleSheet("""
            color: #fff;
        """)

    @staticmethod
    def bandEvent(Act, args):
        try:
            func = args
            Act.triggered.connect(func)
        except TypeError:
            func, shortcut = args
            Act.setShortcut(shortcut)
            Act.triggered.connect(func)

    def exitBand(self):
        pass
