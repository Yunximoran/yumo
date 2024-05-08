from lib.build.buildStructure import BuildStructure

# 导入内置模块
from lxml import etree
import subprocess
import json
import sys
import os

args = sys.argv  # args获取参数

# 切换当前目录为工作目录
workPath = os.path.dirname(__file__)    # dirname获取文件所在目录， __file__获取文件绝对路径
                                        # dirname 包含 __file__
os.chdir(workPath)


class Run:
    __tree = etree.parse('yumo.xml')
    __root = __tree.getroot()

    def __init__(self, *args, attr="main"):     # 初始化进程， 定位启动目标
        # 输入项目名称， 怎样准确定位到文件所在为止
        self.config(attr)
        self.attr = attr
        label = input("启动项目分类: ")
        startproject = input("启动项目名称: ")
        print(f"running: {startproject}")
        self.start(startproject, label)

    def start(self, name, label, *args):  # 启动项目
        itemPath = f"{self.attr}\\{label}\\{name}\\yumo.py"
        print(f"project working {itemPath}")
        # self.__changeWorkEnvironment(itemPath)  # 切换工作环境
        OutPut = subprocess.Popen(['python', itemPath], shell=True, encoding='utf-8')
        print(OutPut.communicate()[0])  # 获取输出结果
        print("project finish")

    def close(self):
        pass

    def config(self, attr):
        # 获取项目配置
        Conf = self.__root.find()



    def UpdateProject(self):  # 更新项目
        self.__upxml()
        self.__getStructure()

    def __upxml(self):
        """
            更新项目配置文件
        :return:
        """

        project = self.__root.find("project")
        project.set('path', os.getcwd())
        self.__tree.write('yumo.xml', encoding='utf-8', method='xml')

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


Run()
