import sys
import os
import cv2

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

from lxml import etree

APPLICATION = QApplication(sys.argv)


def loadConf(label):
    # 导入配置文件
    xml = etree.parse('yumo.xml')
    print(etree.tostring(xml))
    style = None
    return style


def loadImg(iurl):
    img = cv2.imread(iurl)
    h, w = img.shape[0], img.shape[1]
    return img, h, w
