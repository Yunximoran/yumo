import os
import time
import xml.etree.ElementTree as et

__all__ = ['buildStructure', 'os', 'time']

tree = et.parse('../../yumo.xml')

root = tree.getroot()

for config in root.findall('project'):
    rootDirName = config.find("root").text
    rootAbsPath = config.find("root-absPath").text
    print(rootDirName, rootAbsPath)


# dirPath应该都是相对路径
def getInfo(dirPath):
    pass


def getAllChild(dirPath):
    pass
