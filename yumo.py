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

    def __init__(self, *args, attr="main"):  # 初始化进程， 定位启动目标
        # 输入项目名称， 怎样准确定位到文件所在为止
        self.UpdateProject()  # 更新项目信息

        self.label = input("启动项目分类: ")
        self.startproject = input("启动项目名称: ")
        self.attr = attr

        self.config(attr)
        print(f"running: {self.startproject}")
        self.start(self.startproject)

    def start(self, name):  # 启动项目
        print(f"project starting {name}")
        OutPut = subprocess.Popen(['python', f"yumo.py"],  # 创建执行命令
                                  shell=True,
                                  cwd=os.path.join(workPath, self.path),    # 设置工作目录
                                  stdout=subprocess.PIPE,  # 子进程输出
                                  stderr=subprocess.PIPE,  # 子进程错误
                                  encoding="utf-8",
                                  )
        print(OutPut.stdout.read())  # 输出info
        print(OutPut.stderr.read())  # 输出err
        """
        PIPE 表示为子进程创建新的管道
        DEVNULL 表示使用os.devnull, 默认使用None，表示什么都不做
        
        stderr 可以合并到 stdout 一起输出
        
        """
        print("project finished")

    def close(self):
        pass

    def config(self, attr):
        # 获取项目配置
        print(attr, self.label, self.startproject)  # 项目仓库， 项目分类， 项目民

        rootConf = self.__tree.xpath(  # 定位项目配置仓库
            f"//projectConf/nav[@house='{attr}']/list[@class='{self.label}']"
        )[0]

        rootPath = rootConf.xpath(  # 获取项目配置仓库地址
            f"address/text()"
        )[0]

        self.args = rootConf.xpath("projects/project/args/text()")[0].split(", ")  # 获取项目运行参数
        self.path = os.path.join(rootPath, self.startproject)  # 获取启动项目路径

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


Run()

