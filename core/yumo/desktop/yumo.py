import time
import cv2

from modules import *

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import (
    QIcon,
    QPalette,
    QPixmap,
    QBrush,
    QImage
)

from PyQt6.QtCore import Qt

simage = cv2.imread('image/preview.jpg')
ih, iw = simage.shape[0], simage.shape[1]


class YuMo(QWidget):
    """
        主窗口
    """
    # background-color: #626262;    后设置的布局会覆盖前面的效果
    style = """
        background-color: #333333
        color: #333;
        border: 3px solid lightblue;
    """

    def __init__(self):
        super().__init__()
        self.Init()
        self.show()
        sys.exit(APPLICATION.exec())

    def Init(self):
        self.load_config()
        self.load_event()

    def load_config(self):
        self.setGeometry(30, 30, 1024, 600)  # 设置窗口大小
        self.setLayout(MainPart(self))  # 导入UI布局    # 执行布局导入后就会MENU就会创建
        self.setWindowIcon(QIcon(r"image/back.jpg"))  # 设置图标
        self.setStyleSheet(self.style)  # 设置窗口样式
        self.setWindowTitle("Home")  # 设置窗口标题

    # signal slot 信号 槽
    def load_event(self):
        self.__load_menuEvent()

    def __load_menuEvent(self, data=MENU):
        for node in data.keys():
            if isinstance(data[node], dict):
                self.__load_menuEvent(data[node])
            else:
                if node in ACTION:
                    data[node].triggered.connect(ACTION[node])

    def eventFilter(self, a0, a1):  # 事件拦截器
        pass

    def paintEvent(self, a0):
        if self.width() > self.height():
            nw = self.width()

            scale = nw / iw
            nh = int(scale * ih)
        else:
            nh = self.height()
            scale = nh / ih
            nw = int(scale * iw)

        # 缺点，资源占用达，刷新速度慢
        image = cv2.resize(simage, (nw, nh), interpolation=cv2.INTER_LINEAR)
        _, data = cv2.imencode('.jpg', image)
        image = QImage.fromData(data)
        pixmap = QPixmap(image)
        #
        # pixmap = pixmap.scaled(nw, ih, Qt.AspectRatioMode.IgnoreAspectRatio,
        #               Qt.TransformationMode.FastTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

    def resizeEvent(self, a0):
        pass

    def moveEvent(self, a0):
        pass

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
    YuMo()  # 每次执行程序的id都不一样， 执行中id不变 del会删除内存分配

"""
iw, ih, nw, nh

i = n * j
i / j = n


序列化前后的地址一致吗

nw = iw * scale
nh = ih * scale

nh / ih = scale
nw = iw * scale
"""
