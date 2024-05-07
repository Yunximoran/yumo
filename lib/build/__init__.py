import os
import time
import xml.etree.ElementTree as et

__all__ = ['buildStructure', 'os', 'time']

tree = et.parse('../../yumo.xml')

root = tree.getroot()

projectInformation = root.find("project")
rootAbsPath = projectInformation.find("root-absPath")
BaseName = projectInformation.find("root")


def dirJoin(front, rear):
    JoinAfter = os.path.join(front, rear)
    return JoinAfter


# dirPath应该都是相对路径
def getInfo(dirPath):
    pass


def getAllChild(dirPath):
    child = os.listdir(dirPath)
