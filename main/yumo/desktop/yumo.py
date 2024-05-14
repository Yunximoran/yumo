from Global import *

from PyQt6.QtWidgets import (
    QApplication,  # 应用管理
    QWidget,  # 部件、窗口
    QMenuBar,  # 菜单栏
    QMenu,  # 菜单
    QTextEdit,  # 文本编辑器
    QLineEdit,
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
)

from top_part import TopPart, APPLICATION
from mid_part import MidPart
from but_part import ButPart

from lxml import etree


def load_config(label):
    xml = etree.parse('yumo.xml')
    style = None
    return style


class YuMo(QWidget):
    """
        主窗口
    """
    style = """
        background-color: #626262;
        background-image: url('image\\back.jpg');
        color: #333;
        radius: 50px;
    """

    def __init__(self):
        super().__init__()

        self.Init()

        self.setGeometry(30, 30, 1226, 648)
        self.setWindowTitle("Home")
        self.show()

        sys.exit(APPLICATION.exec())

    def Init(self):
        self.load_layout()
        self.load_config()

    def load_layout(self):
        self.MainLayout = QVBoxLayout(self)

        self.topPart = TopPart(self)
        self.midPart = MidPart(self)
        self.butPart = ButPart(self)

        self.MainLayout.addLayout(self.topPart)
        self.MainLayout.addLayout(self.midPart)
        self.MainLayout.addLayout(self.butPart)

    def load_config(self):
        self.setStyleSheet(self.style)
        self.setWindowOpacity(0.8)
        self.setWindowIcon(QIcon(r"image\\back.jpg"))  # 设置图标

    def keyPressEvent(self, a0):
        """
         ENTER == 16777220
        :param a0:
        :return:
        """
        self.Press_key = a0.key()
        print(self.Press_key)

    def keyReleaseEvent(self, a0):
        # print(type(a0))
        self.Release_key = a0.key()
        print(self.Release_key)

    def mousePressEvent(self, a0):
        # 鼠标点击事件
        # print(type(a0))
        pass

    def mouseReleaseEvent(self, a0):
        # 鼠标释放事件
        pass

    def mouseMoveEvent(self, a0):
        # 鼠标移动事件
        pass


# Qt.EnterKeyType.
if __name__ == '__main__':
    YuMo()
