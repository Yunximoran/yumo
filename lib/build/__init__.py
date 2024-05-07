import os
import time
import xml.etree.ElementTree as et

__all__ = ['buildStructure', 'os', 'time']

xmlPath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'yumo.xml')  # 当前文件所在目录
print(xmlPath)

tree = et.parse(xmlPath)
root = tree.getroot()

projectRootPath = root.find("project").get('path')  # 项目根目录


def dirJoin(start, *args):
    JoinAfter = os.path.join(start, *args)
    return JoinAfter


def AbsolutePath():
    absolute = os.getcwd()
    return absolute


# dirPath应该都是相对路径
def getInfo(dirPath):
    pass


def getAllChild(dirPath):
    child = os.listdir(dirPath)
    return child

child = getAllChild(os.getcwd())
print(child)
