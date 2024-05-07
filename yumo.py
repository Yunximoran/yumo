import os

from lib.build.buildStructure import BuildStructure

import xml.etree.ElementTree as et
import json


def upxml():
    tree = et.parse('yumo.xml')
    root = tree.getroot()
    project = root.find("project")
    project.set('path', os.getcwd())
    tree.write('yumo.xml', encoding='utf-8', method='xml')


def getStructure(loadPath=os.getcwd()):
    # 获取项目结构
    """

    :param loadPath: 指定保存路径， 默认保存在当前目录
    :return:
    """
    buildTool = BuildStructure()
    frame = buildTool.OutTreeFrame()

    with open(f'{loadPath}\\yumo.json', 'w', encoding='utf-8') as f:
        json.dump(frame, f, indent=4, ensure_ascii=False)


getStructure()



