from .buildStructure import BuildStructure

import os

__all__ = ['buildStructure']

BuildStructure()


def makedir(Cpath):
    if not os.path.exists(Cpath):
        os.makedirs(Cpath)
        print(f"create directory {Cpath}, finish")


class Build:
    def __init__(self):
        pass

    def newProject(self, Name, attr):
        """
            创建新项目
        :param Name: 项目名
        :param attr: 创建地址
        :return:
        """
        self.__Init(None)

    @staticmethod
    def __Init(structure, main="yumonotes"):
        """
            初始化项目
        :param structure:  初始化项目结构
        :param main: 项目主要文件
        :return:
        """
        allTypeFile = ['.xml', '.py']
        files = [f"{main}{T}" for T in allTypeFile]


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
