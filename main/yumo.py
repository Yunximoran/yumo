from PyQt6.QtWidgets import (
    QGridLayout,    # 是最常用的布局类，它能把空间分为多行多列。 矩阵
    QWidget,        # 部件基类
    QApplication,   # 应用管理
    QVBoxLayout,    # 垂直布局管理
    QHBoxLayout,    # 水平布局管理
    QLayout,    # 布局管理
    QPushButton,  # 按钮
    QTextEdit,  # 文本编辑框
)
from PyQt6.QtGui import QImage
from PyQt6.QtCore import Qt, QTime, QDate, QDateTime

import sys

APPLICATION = QApplication(sys.argv)


class Exampl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        sys.exit(APPLICATION.exec())

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        ok = QPushButton("ok", self)
        cancel = QPushButton("cancel", self)
        grid.addWidget(ok, *(1, 2))
        grid.addWidget(cancel, *(0, 0))



if __name__ == '__main__':
    Exampl()
