import lib.build
from lib.build.buildStructure import BuildStructure
# 导入内置模块
from lxml import etree
import subprocess
import json
import os

# 切换当前目录为工作目录
workPath = os.path.dirname(__file__)  # dirname获取文件所在目录， __file__获取文件绝对路径 *( dirname 包含 __file__ )
os.chdir(workPath)  # workPath: D:\Code\python\YuMo


class Run:
    __tree = etree.parse('yumo.xml')

    allConf = {}

    def __init__(self, *args, house="Core"):  # 初始化进程， 定位启动目标
        self.house = house

        # 输入项目名称， 怎样准确定位到文件所在为止
        self.UpdateProject()  # 更新项目信息
        self.__getAllConfInHouse()

    def start(self, startproject, label):  # 启动项目
        """
            启动项目
        :param startproject: 启动项目名称
        :param label: 启动项目类别
        :return:
        """
        projectConf = self.__getProjectConf(startproject, label)
        args = projectConf['args']
        path = projectConf['path']

        # print(args, path)

        shell = ['python', '0.QtWidgets.py']
        shell.extend(args)  # 将参数添加进命令

        print(f"project starting {startproject}")
        print(os.path.join(workPath, path))

        OutPut = subprocess.Popen(shell,  # 创建执行命令
                                  shell=True,
                                  cwd=os.path.join(workPath, path),  # 设置工作目录
                                  stdout=subprocess.PIPE,  # 子进程输出
                                  stderr=subprocess.PIPE,  # 子进程错误
                                  encoding="utf-8",
                                  )
        print(OutPut.stdout.read())  # return -> Out
        print(OutPut.stderr.read())  # return -> Err
        print("project finished")
        """
        PIPE 表示为子进程创建新的管道
        DEVNULL 表示使用os.devnull, 默认使用None，表示什么都不做

        stdin  子进程输入信息
        stdout 子进程输出信息
        stderr 子进程错误信息
        """

    def close(self):
        pass

    def __getAllConfInHouse(self):
        # 获取项目仓库下的所有项目配置信息

        allConf = self.__tree.xpath(
            f"//projectConf/nav[@house='{self.house}']/list"
        )
        # print(allConf)

        for conf in allConf:  # 将仓库下的所有配置文件切分存储在字典中
            label = conf.xpath('@class')[0]
            if label not in self.allConf:
                self.allConf[label] = conf

    def __getProjectConf(self, projectName, label):
        conf = self.allConf[label]

        args = conf.xpath(f"//project[@name='{projectName}']/args/li/text()")
        housePath = conf.xpath(f"address/text()")[0]
        projectPath = f"{housePath}\\{projectName}"

        projectConf = {
            "args": args,
            "path": projectPath
        }
        return projectConf

    @staticmethod
    def __changeWorkDir(path):
        os.chdir(path)

    def UpdateProject(self):  # 更新项目
        self.__upxml()
        self.__getStructure()

    def __upxml(self):  # 更新xml文件
        pass

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


yumo = Run()
yumo.start('demo', 'Crawler')

"""
参数应该以什么方式存放在xml中，有应该怎么准确解析？
参数应该作为索引进行定位？？
是否创建配置文件导航？？？
"""
