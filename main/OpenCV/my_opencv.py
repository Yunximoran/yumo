from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QCheckBox
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt

import sys
import cv2
import numpy as np

import layout

APPLICATION = QApplication(sys.argv)


class ShowImg(QWidget):
    # fileConText = QFileDialog()
    PIXMAP = QPixmap()

    def __init__(self):
        super().__init__()

        self.HEIGHT = self.height()
        self.WIDTH = self.width()

        self.init()
        self.show()
        sys.exit(APPLICATION.exec())

    def init(self):
        self.load_widgets()
        self.load_event()
        self.load_layout()
        self.load_config()

    def load_layout(self):
        self.MainLayout = QVBoxLayout(self)  # 两层结构

        self.TopLayout = QHBoxLayout(self)  # 上层
        self.ButLayout = QHBoxLayout(self)  # 下层

        self.__build_top_layout()
        self.__build_but_layout()

        self.MainLayout.addLayout(self.TopLayout, 3)
        self.MainLayout.addLayout(self.ButLayout, 1)

    def __build_but_layout(self):
        self.ButLayout.addWidget(self.b0)
        self.ButLayout.addWidget(self.b1)
        self.ButLayout.addWidget(self.b2)
        self.ButLayout.addWidget(self.b3)
        self.ButLayout.addWidget(self.b4)

    def __build_top_layout(self):
        self.TopLayoutRight = QVBoxLayout(self)  # 上层右

        self.TopLayoutRight.addWidget(self.R)
        self.TopLayoutRight.addWidget(self.B)
        self.TopLayoutRight.addWidget(self.G)

        self.TopLayout.addWidget(self.lab, 3)
        self.TopLayout.addLayout(self.TopLayoutRight, 0)

    # def reLayout(self):
    #     h = self.height()
    #     self.TopLayoutRight.setSpacing(15)
    #     self.TopLayoutRight.setContentsMargins(0, int(h * 0.3), 0, int(h * 0.4))

    def load_config(self):
        self.setGeometry(600, 200, 300, 300)
        self.setWindowTitle("Show Image")
        self.__config_display()
        self.__config_layout()

    def __config_layout(self):
        self.__config_layout_topRight()

    def __config_layout_topRight(self):
        self.TopLayoutRight.setContentsMargins(0, int(self.HEIGHT * 0.3), 0, int(self.HEIGHT * 0.3))
        self.TopLayoutRight.setSpacing(int(self.WIDTH * 0.01))

    def __config_display(self):
        self.lab.setStyleSheet("""
            background-color: #333;
        """)
        self.lab.setScaledContents(False)  # 自适应label窗口大小

    def load_widgets(self):
        self.lab = QLabel(self)

        self.__addAllButton()
        self.__addAllCheckBox()

    def __addAllCheckBox(self):
        self.R = QCheckBox("R", self)
        self.B = QCheckBox("B", self)
        self.G = QCheckBox("G", self)

    def __addAllButton(self):
        self.b0 = layout.Button("Open", self)
        self.b1 = layout.Button("Save", self)
        self.b2 = layout.Button("Close", self)
        self.b3 = layout.Button("拆分通道", self)  # 拆分通道是做什么的？？？
        self.b4 = layout.Button("灰度图像", self)

    def load_event(self):
        self.__band_Button()
        self.__band_CheckBox()

    def __band_Button(self):
        self.b0.clicked.connect(self.OpenSlot)
        self.b1.clicked.connect(self.SaveSlot)
        self.b2.clicked.connect(self.CloseSlot)
        self.b3.clicked.connect(self.SeparateSlot)
        self.b4.clicked.connect(self.GraySlot)

    def __band_CheckBox(self):
        self.R.toggled.connect(self.check_r_status)
        self.B.toggled.connect(self.check_b_status)
        self.G.toggled.connect(self.check_g_status)

    def OpenSlot(self):
        file = QFileDialog(self)

        filename, _ = file.getOpenFileName(None, "choose file")
        print(type(filename))
        # filename = filename.decode('utf-8')
        # Dialog 弹出一个对话框， FileDialog弹出资源管理器
        self.image = cv2.imread(filename)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   # 转灰度图

        ret, data = cv2.imencode('.png', self.image)
        # cv2.imshow("cv2show", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        self.qimg = QImage.fromData(data)  # opencv转QImage

        # qimg = QImage(filename)   # 读取图片方式 一
        # qimg = QImageReader(filename)  # 读取图片
        # # qimg.convertToFormat(QImage.Format.Format_RGB888)
        # qimg = qimg.read()
        # qimg.convertTo(QImage.Format.Format_RGB888)

        size = self.qimg.size()  # 获取图片尺寸
        w = size.width()  # 获取原图宽
        h = size.height()  # 获取原图高

        QImg = self.scale(h, w)

        self.PIXMAP.convertFromImage(QImg)
        self.lab.setPixmap(self.PIXMAP)
        self.lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def scale(self, h, w):
        if h > w:
            resize = self.lab.height()
            scale = h / resize
            rw = int(w / scale)
            QImg = self.qimg.scaled(rw, resize, Qt.AspectRatioMode.IgnoreAspectRatio,
                                    Qt.TransformationMode.FastTransformation)
        else:
            resize = self.lab.width()
            scale = w / resize
            rh = int(h / scale)
            QImg = self.qimg.scaled(resize, rh, Qt.AspectRatioMode.IgnoreAspectRatio,
                                    Qt.TransformationMode.FastTransformation)
        return QImg

    def SaveSlot(self):
        if not self.PIXMAP.isNull():
            file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "*.jpg *.png")
            self.PIXMAP.save(file_path)
        else:
            print("请先打开一个文件")

    def CloseSlot(self):
        self.lab.clear()

    def SeparateSlot(self):
        print(self.R.isChecked())
        r, g, b = cv2.split(self.image)
        # print(type(r), r) # OpenCv返回numpy数组
        showPassWay = []
        # print("Separate")
        if self.R.isChecked():
            # print("R")
            showPassWay.append(r)
        else:
            showPassWay.append(np.zeros_like(r))

        if self.B.isChecked():
            # print("B")
            showPassWay.append(b)
        else:
            showPassWay.append(np.zeros_like(b))

        if self.G.isChecked():
            # print("G")
            showPassWay.append(g)
        else:
            showPassWay.append(np.zeros_like(g))

        if showPassWay is not []:
            showImg = cv2.merge(showPassWay)
            _, data = cv2.imencode('.jpg', showImg)
            # rec, rd = cv2.imencode("", r)
            # rec, bd = cv2.imencode("", b)
            # rec, gd = cv2.imencode("", g)

            qimg = QImage.fromData(data)

            self.PIXMAP.convertFromImage(qimg)
            self.lab.setPixmap(self.PIXMAP)

    def GraySlot(self):
        gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        rec, data = cv2.imencode('.png', gray_img)
        qimg = QImage.fromData(data)
        self.PIXMAP.convertFromImage(qimg)
        self.lab.setPixmap(self.PIXMAP)

    def check_r_status(self):
        print(f"change check R; now status is {self.R.isChecked()}")
        # if self.R.isChecked():  # 勾选 return True
        #     print("showing R")

    def check_b_status(self):
        print(f"change check B; now status is {self.B.isChecked()}")

    def check_g_status(self):
        print(f"change check G; now status is {self.G.isChecked()}")

    def moveEvent(self, a0):  # 窗口移动时调用
        x = self.pos().x()
        y = self.pos().y()
        print(x, y)

    def resizeEvent(self, a0):  # 窗口尺寸变化时调用
        self.load_layout()


if __name__ == '__main__':
    layout.load_hello()
    ShowImg()
    # import pickle
    #
    # with open("person.txt", 'wb') as f:
    #     pickle.dump(ShowImg, f)
    #
    # with open("person.txt", 'rb') as f:
    #     show = pickle.load(f)

    # show()
    # from lxml import etree as ET
    #
    # # 创建一个Python字典
    # data = {
    #     'name': ShowImg,
    #     'age': '25',
    #     'city': '北京'
    # }
    #
    # # 将Python字典转换为XML格式的字符串
    # xml_data = ET.tostring(ET.Element('data', data))
    # print(xml_data.decode())
    #
    # # 将XML格式的字符串转换为Python字典
    # root = ET.fromstring(xml_data)
    # data = dict(root.attrib)
    # print(data)
