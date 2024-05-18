from PyQt6.QtWidgets import (
    QPushButton,
    QMenuBar,
    QMenu,
    QStatusBar,
    QLabel,
    QCheckBox
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

MENU = {
    "file": {
        "file attribute": {
            "encode": None,
            "add BOM": None,
        },
        "restruct": None
    },
    "edit": {
        "copy": None
    },
    'exit': None
}


class Label(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.init()

    def init(self):
        self.load_config()

    def load_config(self):
        self.setStyleSheet("""
            background-color: #fff;
        """)


class Menu(QMenuBar):
    def __init__(self, *args):
        super().__init__(*args)
        self.init()

    def init(self):
        self.__init(MENU, self)
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
                struct[nextNode] = childAct

    def load_config(self):
        pass

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


class Button(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)


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
