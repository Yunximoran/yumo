import time

from Global import *

from PyQt6.QtWidgets import (
    QApplication,  # 应用管理
    QWidget,  # 部件、窗口
    QMenuBar,  # 菜单栏
    QMenu,  # 菜单
    QTextEdit,  # 文本编辑器
    QLineEdit,
    QLabel,
    QPushButton,  # 按钮
    QHBoxLayout,  # 水平布局管理
    QVBoxLayout,  # 垂直布局管理
    QGridLayout,  # 矩阵布局管理
    QBoxLayout,  # 布局管理： 水平 | 垂直
    QInputDialog,  # 输入框
    QCheckBox,  # 勾选框
    QStyle,
    QStatusBar,
)
from PyQt6.QtGui import (
    QAction,
    QIcon,
    QPalette,
    QPixmap,
    QBrush,
    QImage,
    QMouseEvent,
    QKeyEvent,
    QKeySequence,
    QFont,
    QColor
)
from PyQt6.QtCore import (
    Qt,
    QTime,
    QDate,
    QDateTime,
    QEvent
)
import cv2

from top_part import TopPart, APPLICATION
from mid_part import MidPart
from but_part import ButPart

from lxml import etree


class YuMo(QWidget):
    """
        主窗口
    """
    # background-color: #626262;
    style = """
        background-image: url('image\\back.jpg');
        color: #333;
        border: 3px solid lightblue;
    """

    def __init__(self):
        super().__init__()

        self.Init()
        self.show()

        sys.exit(APPLICATION.exec())

    def Init(self):
        self.load_widgets()
        self.load_layout()
        self.load_config()

    def load_widgets(self):
        pass

    def load_layout(self):
        self.MainLayout = QVBoxLayout(self)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)  # 设置布局页边距

        self.topPart = TopPart(self)
        self.midPart = MidPart(self)
        self.butPart = ButPart(self)

        self.MainLayout.addLayout(self.topPart)
        self.MainLayout.addLayout(self.midPart)
        self.MainLayout.addLayout(self.butPart)

    def load_config(self):
        # self.setWindowOpacity(0.8)    # 设置透明度
        self.setWindowIcon(QIcon(r"image\\back.jpg"))  # 设置图标
        # self.setLayout(self.MainLayout)  # 设置窗口基本布局
        self.setStyleSheet(self.style)  # 设置窗口样式
        self.setGeometry(30, 30, 1024, 600)  # 设置窗口大小
        self.setWindowTitle("Home")  # 设置窗口布局

    def eventFilter(self, a0, a1):
        pass

    def paintEvent(self, a0):
        pixmap = QPixmap("image\\preview.jpg")
        pixmap = pixmap.scaled(self.width(), self.height())  # param: width, height
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

    def mousePressEvent(self, a0):
        # 鼠标点击事件
        # print(type(a0))
        if a0.button() == Qt.MouseButton.LeftButton:
            self.s = time.time()
            print('click')

    def mouseReleaseEvent(self, a0):
        # 鼠标释放事件
        print("release")
        d = time.time()
        print(self.s - d)

    def mouseMoveEvent(self, a0):
        # 鼠标移动事件, 按住移动
        pos = a0.pos()
        print(pos)


# Qt.EnterKeyType.
if __name__ == '__main__':
    YuMo()
