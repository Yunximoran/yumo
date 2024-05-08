import os
import time
import xml.etree.ElementTree as et

__all__ = ['buildStructure', 'os', 'time']

# xmlPath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'yumo.xml')  # 当前文件所在目录
#
# tree = et.parse(xmlPath)
# root = tree.getroot()
#
# projectRootPath = root.find("project").get('path')  # 项目根目录


def dirJoin(start, *args):
    JoinAfter = os.path.join(start, *args)
    return JoinAfter


def AbsolutePath():
    absolute = os.getcwd()
    return absolute


# dirPath应该都是相对路径
def getInfo(dirPath):
    """
        获取文件信息{创建时间、 数据大小}
    :param dirPath:
    :return:
    """
    os.path.getctime(__file__)  # __file__ 工作文件
    pass


def getAllChild(dirPath):

    child = os.listdir(dirPath)
    return child


if __name__ == '__main__':
    pass
