import PySide6.QtCore

import sys
import random
from PySide6 import (
    QtCore,
    QtWidgets,
    QtGui
)

print(PySide6.__version__)
print(PySide6.QtCore.__version__)


# 创建一个简单的Qt Widgets程序
class MyWidgets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hallo = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton('Click me!')
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hallo))


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        # alignment=QtCore.Qt.AlignCenter

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def execute(label=0):
    if label == 0:
        app = QtWidgets.QApplication([])

        MyQt = MyWidgets()
        MyQt.resize(800, 600)
        MyQt.show()

        sys.exit(app.exec())
    else:
        app = QtWidgets.QApplication([])

        widget = MyWidget()
        widget.resize(800, 600)
        widget.show()

        sys.exit(app.exec())


if __name__ == '__main__':
    execute()
