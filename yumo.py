# 导入自建模块
from lib.build.buildStructure import BuildStructure

# 导入内置模块
import xml.etree.ElementTree as et
import json
import os


class Start:
    __tree = et.parse('yumo.xml')
    __root = __tree.getroot()

    def __init__(self):
        # 可以启动的程序应该都在main中
        self.UpdateProject()
        self.config()
        label = input("启动项目分类: ")
        # if label not in self.label:
        #     raise None

        startproject = input("启动项目名称: ")

    def start(self, name, label):
        pass

    def config(self):
        pass

    def UpdateProject(self):  # 更新项目
        self.__upxml()
        self.__getStructure()

    @staticmethod
    def __upxml():
        """
            更新项目配置文件
        :return:
        """
        tree = et.parse('yumo.xml')
        root = tree.getroot()
        project = root.find("project")
        project.set('path', os.getcwd())
        tree.write('yumo.xml', encoding='utf-8', method='xml')

    @staticmethod
    def __getStructure(loadPath=os.getcwd()):
        """
            获取项目结构
        :param loadPath: 指定保存路径， 默认保存在当前目录
        :return:
        """
        buildTool = BuildStructure()
        frame = buildTool.OutTreeFrame()

        with open(f'{loadPath}\\yumo.json', 'w', encoding='utf-8') as f:
            json.dump(frame, f, indent=4, ensure_ascii=False)

print("Hello world!")