import sys
import os

from PyQt6.QtWidgets import QApplication

from lxml import etree

APPLICATION = QApplication(sys.argv)


def loadConf(label):
    # 导入配置文件
    xml = etree.parse('yumo.xml')
    print(etree.tostring(xml))
    style = None
    return style
